import os
from utils import get_translucent_trace_variants
from pm4py import format_dataframe, discover_process_tree_inductive, convert_to_petri_net, convert_to_event_log, get_variants
import pandas as pd
from translucent_alignment import align
from translucent_reachability_graph import TranslucentReachabilityGraph, TranslucentAlignmentStateGraph
import time
import statistics

skip_file = "original_translucent_event_log_04.csv"
event_log = format_dataframe(pd.read_csv(skip_file, sep=","),
                             case_id="case:concept:name",
                             activity_key="concept:name",
                             timestamp_key="time:timestamp",
                             timest_format="%Y-%m-%d %H:%M:%S%z",
                             )
event_log = convert_to_event_log(event_log)
process_tree = discover_process_tree_inductive(event_log)
trg = TranslucentReachabilityGraph(convert_to_petri_net(process_tree))

current_directory = os.getcwd()
for file in os.listdir(current_directory):
    if file.endswith(".csv") and file != skip_file:  # Check if it's a CSV and not the one to skip
        event_log = format_dataframe(pd.read_csv(file, sep=";"),
                                     case_id="case:concept:name",
                                     activity_key="concept:name",
                                     timestamp_key="time:timestamp",
                                     timest_format="%Y-%m-%d %H:%M:%S%z",
                                     )
        event_log = convert_to_event_log(event_log)
        # Convert enabled activities to sets
        for trace in event_log:
            for event in trace:
                event["enabled"] = {ea.strip() for ea in str(event["enabled_activities"]).split(",")}
        variants = get_translucent_trace_variants(event_log)

        results_of_variants = {}
        for variant in variants:
            times = []
            for _ in range(5):
                start_time = time.perf_counter()
                translucent_alignment = align(variants[variant][0], trg, ignore_translucent=True)
                end_time = time.perf_counter()
                times.append(end_time - start_time)
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
            results_of_variants[variant]["time"] = statistics.median(times)
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
        new_filename = f"{os.path.splitext(file)[0]}_translucent.csv"
        df.to_csv(new_filename, index=False, sep=";")
        variants = get_variants(event_log)
        results_of_variants = {}
        for variant in variants:
            times = []
            for _ in range(5):
                start_time = time.perf_counter()
                translucent_alignment = align(variants[variant][0], trg)
                end_time = time.perf_counter()
                times.append(end_time - start_time)
            results_of_variants[variant] = {}
            results_of_variants[variant]["alignment"] = translucent_alignment["alignment"]
            results_of_variants[variant]["cost"] = translucent_alignment["cost"]
            results_of_variants[variant]["visited_states"] = translucent_alignment["visited_states"]
            results_of_variants[variant]["queued_states"] = translucent_alignment["queued_states"]
            results_of_variants[variant]["traversed_arcs"] = translucent_alignment["traversed_arcs"]
            results_of_variants[variant]["lp_solved"] = translucent_alignment["lp_solved"]
            results_of_variants[variant]["fitness"] = translucent_alignment["fitness"]
            results_of_variants[variant]["translucent_alignment"] = translucent_alignment["translucent_alignment"]
            results_of_variants[variant]["number_occurrence"] = len(variants[variant])
            results_of_variants[variant]["length_variant"] = len(variant)
            results_of_variants[variant]["time"] = statistics.median(times)
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
        new_filename = f"{os.path.splitext(file)[0]}_classic.csv"
        df.to_csv(new_filename, index=False, sep=";")
        print(str(file)+" done!")
