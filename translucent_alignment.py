from pm4py import PetriNet, Marking
from pm4py.objects.log.obj import Trace

from translucent_reachability_graph import TranslucentReachabilityGraph, TranslucentAlignmentStateGraph


def align(translucent_trace: Trace, translucent_reachability_graph: TranslucentReachabilityGraph):
    # Check if the trace is enriched with translucent information
    if not all('enabled' in event for event in translucent_trace):
        raise ValueError("The trace is not enriched with translucent information")
    return TranslucentAlignmentStateGraph(translucent_reachability_graph, translucent_trace).get_optimal_alignment()


def align_to_petri_net(translucent_trace: Trace, accepting_petri_net: tuple[PetriNet, Marking, Marking]):
    # Check if the trace is enriched with translucent information
    if not all('enabled' in event for event in translucent_trace):
        raise ValueError("The trace is not enriched with translucent information")
    return align(translucent_trace, TranslucentReachabilityGraph(accepting_petri_net))
