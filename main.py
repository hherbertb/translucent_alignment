from pm4py import read_pnml

from translucent_reachability_graph import TranslucentReachabilityGraph, TranslucentAlignmentStateGraph
from utils_graphs import create_translucent_trace


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
