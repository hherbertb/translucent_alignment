from pm4py import read_pnml
from pm4py.objects.petri_net.obj import PetriNet
from translucent_reachability_graph import TranslucentReachabilityGraph, TranslucentAlignmentStateGraph
from utils import create_translucent_trace
import pm4py

if __name__ == '__main__':
    accepting_petri_net = read_pnml("./data/running_example.pnml")

    #translucent_trace = create_translucent_trace([("A", {"A", "B"}), ("B", {"B"}), ("C", {"C"})])

    # find places for modification
    source_place = [place for place in accepting_petri_net[0].places if place.name == "n4"][0]
    silent_transition = [transition for transition in accepting_petri_net[0].transitions if transition.name == "n19"][0]
    joint_place = [place for place in accepting_petri_net[0].places if place.name == "n1"][0]

    # create new places and transitions
    place1 = PetriNet.Place("p1")  # Create a place named "p1"
    accepting_petri_net[0].places.add(place1)  # Add place1 to the net
    transition = PetriNet.Transition("t1", "A")  # Create a transition named "t1"
    accepting_petri_net[0].transitions.add(transition)


    arc1 = PetriNet.Arc(source_place, transition)
    accepting_petri_net[0].arcs.add(arc1)

    arc2 = PetriNet.Arc(transition, place1)
    accepting_petri_net[0].arcs.add(arc2)

    arc3 = PetriNet.Arc(transition, joint_place)
    accepting_petri_net[0].arcs.add(arc3)

    arc4 = PetriNet.Arc(place1, silent_transition)
    accepting_petri_net[0].arcs.add(arc4)

    #translucent_trace = create_translucent_trace([("A", {"A"}), ("B", {"B"}), ("D", {"D"}), ("E", {"E", "F", "G"}), ("G", {"G"})])
    #translucent_trace = create_translucent_trace([("A", {"A"}), ("B", {"B", "C"}), ("D", {"D"}), ("E", {"E", "F", "G"}), ("G", {"G"})])
    #translucent_trace = create_translucent_trace([("A", {"A"}), ("B", {"B"}), ("D", {"D"}), ("E", {"E", "G"}), ("G", {"G"})])
    translucent_trace = create_translucent_trace([("A", {"A"}), ("B", {"B"}), ("D", {"D"}), ("X", {"X", "E", "G"}), ("G", {"G"})])
    #translucent_trace = create_translucent_trace([("A", {"A"}), ("B", {"B"}), ("E", {"E", "F", "G"}), ("G", {"G"})])
    from pm4py.algo.conformance.alignments.petri_net.algorithm import apply as alignments
    alignment = alignments(translucent_trace, *accepting_petri_net)
    trg = TranslucentReachabilityGraph(accepting_petri_net)
    #trg.view()
    tasg = TranslucentAlignmentStateGraph(TranslucentReachabilityGraph(accepting_petri_net), translucent_trace)
    #tasg.view()
    a = tasg.get_optimal_alignment()
    print(a)
