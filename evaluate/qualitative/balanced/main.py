import time
import statistics
import pm4py 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pm4py import read_pnml, format_dataframe, convert_to_event_log
from translucent_alignment import align
from translucent_reachability_graph import TranslucentReachabilityGraph
from utils import get_translucent_trace_variants, frequent_activity_weights, learn_activity_weights

def variant_to_latex(variant, count, label_map=None, with_exponent=True):
    """
    variant: tuple of (activity, enabled_set) pairs, e.g.
        (('Open', frozenset({'Open'})),
         ('Save', frozenset({'Save','Cancel','Fill','Support'})), ...)
    count: number of occurrences of this variant
    label_map: maps activity names (strings) to LaTeX symbols (e.g. 'Open' -> 'a')
    with_exponent: if True, append ^{count} to the sequence
    """
    if label_map is None:
        label_map = {}

    def lbl(act):
        # Map activity name to a short label; default: use the name itself
        return label_map.get(act, act)

    cells = []
    for act, enabled in variant:
        enabled_labels = sorted(lbl(a) for a in enabled)
        exec_label = lbl(act)
        # remove the executed label from the remaining enabled labels once
        rest = []
        used_exec = False
        for x in enabled_labels:
            if x == exec_label and not used_exec:
                used_exec = True
                continue
            rest.append(x)
        # \underline{A}BC
        cell = r"\underline{" + exec_label + "}" + "".join(rest)
        cells.append(cell)

    seq = r"\langle " + ", ".join(cells) + r"\rangle"
    if with_exponent and count is not None and count > 1:
        seq += f"^{{{count}}}"
    elif not with_exponent and count is not None:
        # alternative: append as plain number, like ⟨…⟩100 in your tables
        seq += f"{count}"

    return seq

def variant_to_github(variant, count, label_map=None):
    """
    variant: tuple of (activity, enabled_set) pairs
    count: number of occurrences
    label_map: optional mapping from internal labels to short ones (e.g. 'Open' -> 'a')
    """
    if label_map is None:
        label_map = {}

    def lbl(act):
        return label_map.get(act, act)

    cells = []
    for act, enabled in variant:
        enabled_labels = sorted(lbl(a) for a in enabled)
        exec_label = lbl(act)
        # remove one occurrence of exec_label from the rest
        rest = []
        used_exec = False
        for x in enabled_labels:
            if x == exec_label and not used_exec:
                used_exec = True
                continue
            rest.append(x)
        cell = f"<ins>{exec_label}</ins>" + "".join(rest)
        cells.append(cell)

    seq = "⟨" + ", ".join(cells) + "⟩"
    if count is not None and count > 1:
        seq += f" × {count}"
    return seq

label_map = {
    "Open":   "a",
    "Fill":   "b",
    "Attach": "c",
    "Review": "d",
    "Submit": "e",
    "Cancel": "f",
    "Support": "g",
    "Save":   "h",
}

# Define lists of PNML files and event logs
pnml_files = ["M1.pnml", "M2.pnml", "M3.pnml"]
event_logs = ["insurance_claim_translucent_log_3.csv"]

# Define the weight functions and their corresponding names
weight_functions = {
    'standard': None,
    'frequent': frequent_activity_weights,
    'sequence': learn_activity_weights
}

# Create a list to store results for the overview CSV
overview_results = []

# Collect timing rows across all combinations for the figure
all_timing_rows = []

# Iterate over each combination of PNML file and event log
for pnml_file in pnml_files:
    accepting_petri_net = read_pnml(f"evaluate/qualitative/insurance/{pnml_file}")
    trg = TranslucentReachabilityGraph(accepting_petri_net)

    for log_file in event_logs:
        # Read the event log
        event_log = convert_to_event_log(format_dataframe(pd.read_csv(f"evaluate/qualitative/insurance/{log_file}"),
                                                          case_id="case",
                                                          activity_key="activity",
                                                          timestamp_key="timestamp"))

        # Process each trace in the event log to extract enabled activities
        for trace in event_log:
            for event in trace:
                event["enabled"] = {ea.strip() for ea in str(event["enabled_activities"]).split(",")}

        variants = get_translucent_trace_variants(event_log)

        print("")
        print(len(variants))
        print("")
        print(len(pm4py.get_variants(event_log)))
        print("")

        #for variant, (trace, idx_set) in variants.items():
        #    count = len(idx_set)
        #    github_seq = variant_to_github(variant, count, label_map)
        #    print(f"- {github_seq}")
        # Iterate over each weighting function
        for weight_name, weight_function in weight_functions.items():
            print(weight_name)
            if weight_function is not None:
                weights = weight_function(event_log)  # Call the appropriate weight function
                print(weights)
            # Set ignore_translucent options (False and True)
            for ignore_translucent in [False, True]:
                results_of_variants = {}

                # Align each variant with the translucent reachability graph using weights if applicable
                for variant in variants:
                    times = []
                    for _ in range(10):
                        start_time = time.perf_counter()
                        if weight_function is None:  # No weights used
                            translucent_alignment = align(variants[variant][0], trg, ignore_translucent=ignore_translucent)
                        else:  # Weights are used
                            translucent_alignment = align(variants[variant][0], trg, activity_weights=weights, ignore_translucent=ignore_translucent)
                        end_time = time.perf_counter()
                        times.append(end_time - start_time)

                    results_of_variants[variant] = {
                        "alignment": translucent_alignment["alignment"],
                        "cost": translucent_alignment["cost"],
                        "visited_states": translucent_alignment["visited_states"],
                        "queued_states": translucent_alignment["queued_states"],
                        "traversed_arcs": translucent_alignment["traversed_arcs"],
                        "lp_solved": translucent_alignment["lp_solved"],
                        "fitness": translucent_alignment["fitness"],
                        "translucent_alignment": translucent_alignment["translucent_alignment"],
                        "number_occurrence": len(variants[variant][1]),
                        "length_variant": len(variant),
                        "time": min(times)*1000,
                        **translucent_alignment  # unpack remaining values directly into results_of_variants dictionary
                    }

                total_occurrences = sum(result['number_occurrence'] for result in results_of_variants.values())
                weighted_fitness_total = round((sum(result['fitness'] * result['number_occurrence']
                                                for result in results_of_variants.values()) / total_occurrences
                                          if total_occurrences > 0 else 0), 3)

                # Store overview result with relevant details.
                overview_results.append({
                    'Model': pnml_file.split('.')[0],
                    'Log': log_file.split('.')[0],
                    'Weight Function': weight_name,
                    'Ignore Translucents': ignore_translucent,
                    'Weighted Fitness': weighted_fitness_total,
                })

                # Create DataFrame from results and save it to a CSV file with a descriptive name including weights used and ignore flag.
                df = pd.DataFrame([
                    {"Variant": variant, **values}
                    for variant, values in results_of_variants.items()
                ])

                ignore_flag_str = "_ignored" if ignore_translucent else "_translucent"
                new_filename = f"evaluate/qualitative/insurance/r2/results_{pnml_file}_{weight_name}{ignore_flag_str}.csv"
                df.to_csv(new_filename, index=False, sep=";")

                # Accumulate timing rows for figure
                method = "non_translucent" if ignore_translucent else weight_name
                for variant, values in results_of_variants.items():
                    all_timing_rows.append({
                        "length_variant": values["length_variant"],
                        "time": values["time"],
                        "method": method,
                        "model": pnml_file.split(".")[0],
                    })

# Create DataFrame from overview results and save it as a CSV file.
overview_df = pd.DataFrame(overview_results)
overview_filename = (
    "evaluate/qualitative/insurance/r2/overview_weighted_fitness.csv"
)
overview_df.to_csv(overview_filename, index=False)

print("Overview CSV created successfully.")

# --- Trendline comparison and per-method figure ---
from scipy.optimize import curve_fit

# Okabe-Ito palette — works in greyscale and for colorblind viewers
style = {
    "standard":        {"color": "#0072B2", "marker": "s", "label": "Equal"},
    "frequent":        {"color": "#D55E00", "marker": "^", "label": "Frequency"},
    "sequence":        {"color": "#009E73", "marker": "D", "label": "Sequence"},
    "non_translucent": {"color": "#000000", "marker": "o", "label": "Non-translucent"},
}

timing_df = pd.DataFrame(all_timing_rows)
X_all = timing_df["length_variant"].values.astype(float)
Y_all = timing_df["time"].values

def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_true.mean()) ** 2)
    return 1.0 - ss_res / ss_tot

def adj_r2_score(y_true, y_pred, n_params):
    n = len(y_true)
    r2 = r2_score(y_true, y_pred)
    return 1.0 - (1.0 - r2) * (n - 1) / (n - n_params - 1)

def nlogn_func(x, a, b):
    return a * x * np.log(x) + b

def exp_func(x, a, b):
    return a * np.exp(b * x)

# Fit each candidate trendline to the pooled data
candidate_models = {}

for deg, name in [(1, "Linear"), (2, "Quadratic"), (3, "Cubic")]:
    coeffs = np.polyfit(X_all, Y_all, deg)
    poly = np.poly1d(coeffs)
    y_pred = poly(X_all)
    n_params = deg + 1  # polynomial coefficients
    candidate_models[name] = {
        "predict": poly,
        "r2": r2_score(Y_all, y_pred),
        "adj_r2": adj_r2_score(Y_all, y_pred, n_params),
    }

for fname, func, p0 in [
    ("n*log(n)", nlogn_func, [1e-4, 0.0]),
    ("Exponential", exp_func, [1e-4, 0.1]),
]:
    try:
        popt, _ = curve_fit(func, X_all, Y_all, p0=p0, maxfev=5000)
        y_pred = func(X_all, *popt)
        candidate_models[fname] = {
            "predict": lambda xs, f=func, p=popt: f(xs, *p),
            "r2": r2_score(Y_all, y_pred),
            "adj_r2": adj_r2_score(Y_all, y_pred, len(popt)),
        }
    except Exception as e:
        print(f"Could not fit {fname}: {e}")

# Report R² and adjusted R² for all candidates
print("\nTrendline comparison (all methods pooled):")
print(f"  {'Model':12s}  {'R²':>8}  {'Adj. R²':>10}")
for name, res in sorted(candidate_models.items(), key=lambda kv: -kv[1]["adj_r2"]):
    print(f"  {name:12s}  {res['r2']:8.4f}  {res['adj_r2']:10.4f}")
# Best by adjusted R² (penalises extra parameters)
best_name = max(candidate_models, key=lambda k: candidate_models[k]["adj_r2"])
print(f"Best trendline: {best_name} (R²={candidate_models[best_name]['r2']:.4f}, "
      f"Adj. R²={candidate_models[best_name]['adj_r2']:.4f})")

xs_fine = np.linspace(X_all.min(), X_all.max(), 200)

# Increase all font sizes by 4pt from matplotlib defaults
plt.rcParams.update({
    "font.size":        16,   # default 10
    "axes.titlesize":   20,   # default 12  (unused but consistent)
    "axes.labelsize":   20,   # default 12  (x/y axis labels)
    "xtick.labelsize":  16,   # default 10
    "ytick.labelsize":  16,   # default 10
    "legend.fontsize":  16,   # default 10
})

# Figure 1: trendline comparison — pooled scatter + all candidate curves
trend_colors = {
    "Linear":      "#E69F00",
    "Quadratic":   "#56B4E9",
    "Cubic":       "#CC79A7",
    "n*log(n)":    "#F0E442",
    "Exponential": "#999999",
}
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(X_all, Y_all, color="lightgrey", alpha=0.4, s=10, rasterized=True, label="Data")
for name, res in candidate_models.items():
    ys = res["predict"](xs_fine)
    marker = " *" if name == best_name else ""
    ax.plot(xs_fine, ys,
            color=trend_colors.get(name, "#333333"),
            linewidth=2,
            label=f"{name}{marker} (R²={res['r2']:.3f}, adj.={res['adj_r2']:.3f})")
ax.set_xlabel("Variant Length")
ax.set_ylabel("Computation Time (s)")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)
fig.tight_layout()
fig.savefig("evaluate/qualitative/insurance/r2/variant_time_trendlines.pdf",
            format="pdf", bbox_inches="tight")
plt.close()
print("Trendline comparison figure saved.")

# Figure 2: per-method scatter + best trendline refitted per method, one subplot per model
models_in_data = sorted(timing_df["model"].unique())  # e.g. ['M1', 'M2', 'M3']
n_models = len(models_in_data)
fig, axes = plt.subplots(1, n_models, figsize=(6 * n_models, 6), sharey=True)
if n_models == 1:
    axes = [axes]

for ax, model_name in zip(axes, models_in_data):
    model_df = timing_df[timing_df["model"] == model_name]
    for method, group in model_df.groupby("method"):
        s = style[method]
        ax.scatter(group["length_variant"], group["time"],
                   color=s["color"], marker=s["marker"],
                   alpha=0.6, label=s["label"], rasterized=True)
        if len(group) >= 3:
            X_m = group["length_variant"].values.astype(float)
            Y_m = group["time"].values
            xs_m = np.linspace(X_m.min(), X_m.max(), 100)
            try:
                if best_name in ("Linear", "Quadratic", "Cubic"):
                    deg = {"Linear": 1, "Quadratic": 2, "Cubic": 3}[best_name]
                    poly_m = np.poly1d(np.polyfit(X_m, Y_m, deg))
                    ax.plot(xs_m, poly_m(xs_m), color=s["color"], linestyle="--")
                elif best_name == "n*log(n)":
                    popt_m, _ = curve_fit(nlogn_func, X_m, Y_m, p0=[1e-4, 0.0], maxfev=5000)
                    ax.plot(xs_m, nlogn_func(xs_m, *popt_m), color=s["color"], linestyle="--")
                elif best_name == "Exponential":
                    popt_m, _ = curve_fit(exp_func, X_m, Y_m, p0=[1e-4, 0.1], maxfev=5000)
                    ax.plot(xs_m, exp_func(xs_m, *popt_m), color=s["color"], linestyle="--")
            except Exception:
                pass

    ax.set_title(model_name)
    ax.set_xlabel("Variant Length")
    ax.set_ylabel("Computation Time (ms)")
    ax.grid(True, linestyle="--", alpha=0.6)

# Single shared legend placed outside the rightmost subplot, ordered by style dict
import matplotlib.lines as mlines
legend_handles = [
    mlines.Line2D([], [], color=s["color"], marker=s["marker"],
                  linestyle="None", markersize=8, label=s["label"])
    for s in style.values()
]
fig.legend(handles=legend_handles,
           loc="lower center",
           ncol=len(style),
           bbox_to_anchor=(0.5, -0.12))
fig.tight_layout()
fig.savefig("evaluate/qualitative/insurance/r2/variant_time.pdf",
            format="pdf", bbox_inches="tight")
plt.close()
print("Per-method timing figure saved.")
