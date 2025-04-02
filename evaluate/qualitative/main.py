from pm4py import read_pnml, format_dataframe, discover_process_tree_inductive, convert_to_petri_net, discover_petri_net_inductive
import pm4py
import pandas as pd
from translucent_reachability_graph import TranslucentReachabilityGraph, TranslucentAlignmentStateGraph
from utils import create_translucent_trace

"""
if __name__ == '__main__':
    accepting_petri_net = read_pnml("./data/petri_net.pnml")
    translucent_trace = create_translucent_trace([("A", {"A", "B"}), ("B", {"B"}), ("C", {"C"})])
    from pm4py.algo.conformance.alignments.petri_net.algorithm import apply as alignments
    alignment = alignments(translucent_trace, *accepting_petri_net)
    trg = TranslucentReachabilityGraph(accepting_petri_net)
    #trg.view()
    tasg = TranslucentAlignmentStateGraph(TranslucentReachabilityGraph(accepting_petri_net), translucent_trace)
    #tasg.view()
    a = tasg.get_optimal_alignment()
    print(a)
"""
event_log = format_dataframe(pd.read_csv("ground_truth.csv"),
                                 case_id="case:concept:name",
                                 activity_key="concept:name",
                                 timestamp_key="time:timestamp",
                                 timest_format="%Y-%m-%d %H:%M:%S%z",
                                 )

net, im, fm = discover_petri_net_inductive(event_log)

pm4py.vis.view_petri_net(net, im, fm, format="svg")