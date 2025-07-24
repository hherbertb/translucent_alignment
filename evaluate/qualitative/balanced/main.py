import pandas as pd
from pm4py import read_pnml, PetriNet, format_dataframe, discover_process_tree_inductive, convert_to_petri_net, \
    convert_to_event_log

from translucent_alignment import align
from translucent_reachability_graph import TranslucentReachabilityGraph
from utils import get_translucent_trace_variants


accepting_petri_net = read_pnml("evaluate/qualitative/balanced/n1.pnml")
trg = TranslucentReachabilityGraph(accepting_petri_net)


event_log = convert_to_event_log(format_dataframe(pd.read_csv("evaluate/qualitative/balanced/L1_1.csv"),
                                                      case_id="case",
                                                      activity_key="activity",
                                                      timestamp_key="timestamp",
                                                      ))



for trace in event_log:
    for event in trace:
        event["enabled"] = {ea.strip() for ea in str(event["enabled_activities"]).split(",")}
variants = get_translucent_trace_variants(event_log)




results_of_variants = {}
for variant in variants:
    translucent_alignment = align(variants[variant][0], trg)
    results_of_variants[variant] = {}
    results_of_variants[variant]["alignment"] = translucent_alignment["alignment"]
    results_of_variants[variant]["cost"] = translucent_alignment["cost"]
    results_of_variants[variant]["visited_states"] = translucent_alignment["visited_states"]
    results_of_variants[variant]["queued_states"] = translucent_alignment["queued_states"]
    results_of_variants[variant]["traversed_arcs"] = translucent_alignment["traversed_arcs"]
    results_of_variants[variant]["lp_solved"] = translucent_alignment["lp_solved"]
    results_of_variants[variant]["fitness"] = translucent_alignment["fitness"]
    results_of_variants[variant]["translucent_alignment"] = translucent_alignment["translucent_alignment"]
    results_of_variants[variant]["number_occurrence"] = len(variants[variant][1])
    results_of_variants[variant]["length_variant"] = len(variant)
    results_of_variants[variant]["move_cost"] = len(translucent_alignment["move_cost"])
    results_of_variants[variant]["n_sync"] = translucent_alignment["n_sync"]
    results_of_variants[variant]["n_log"] = translucent_alignment["n_log"]
    results_of_variants[variant]["n_model"] = translucent_alignment["n_model"]
    results_of_variants[variant]["n_silent"] = translucent_alignment["n_silent"]
    results_of_variants[variant]["n_enabled_change"] = translucent_alignment["n_enabled_change"]
    results_of_variants[variant]["n_execution_change"] = translucent_alignment["n_execution_change"]
    results_of_variants[variant]["n_execution_enabled_change"] = translucent_alignment["n_execution_enabled_change"]
df = pd.DataFrame([
    {"Variant": variant, **values}  # Add 'Variant' column and unpack dictionary values
    for variant, values in results_of_variants.items()
])
new_filename = "evaluate/qualitative/balanced/results_1_translucent.csv"
df.to_csv(new_filename, index=False, sep=";")

total_occurrences = df["number_occurrence"].sum()
weighted_fitness = (df["fitness"] * df["number_occurrence"]).sum() / total_occurrences
print(weighted_fitness)