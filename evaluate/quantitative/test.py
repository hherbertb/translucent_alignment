from utils import get_translucent_trace_variants
from pm4py import read_pnml, format_dataframe, discover_process_tree_inductive, convert_to_petri_net, discover_petri_net_inductive, convert_to_event_log
import pm4py
import pandas as pd
from translucent_alignment import align
from translucent_reachability_graph import TranslucentReachabilityGraph, TranslucentAlignmentStateGraph


event_log = format_dataframe(pd.read_csv("../qualitative/ground_truth.csv"),
                                 case_id="case:concept:name",
                                 activity_key="concept:name",
                                 timestamp_key="time:timestamp",
                                 timest_format="%Y-%m-%d %H:%M:%S%z",
                                 )
event_log = convert_to_event_log(event_log)
process_tree = discover_process_tree_inductive(event_log)
trg = TranslucentReachabilityGraph(convert_to_petri_net(process_tree))
# Convert enabled activities to sets
for trace in event_log:
    for event in trace:
        event["enabled"] = {ea.strip() for ea in str(event["enabled_activities"]).split(",")}
variants = get_translucent_trace_variants(event_log)
running_fitness = 0
number_traces = 0
for variant in variants:
    translucent_alignment = align(variants[variant][0], trg)
    running_fitness += translucent_alignment["fitness"]*len(variants[variant][1])
    number_traces += len(variants[variant][1])
print(running_fitness/number_traces)