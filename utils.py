from copy import deepcopy
from typing import Optional

from pm4py import PetriNet, Marking
from pm4py.objects.log.obj import Trace, Event
from pm4py.objects.petri_net.utils.petri_utils import add_place, add_transition, add_arc_from_to, place_set_as_marking

ARTIFICIAL_END_TRANSITION_NAME = "END"
ARTIFICIAL_END_TRANSITION_LABEL = "END"
ARTIFICIAL_END_PLACE_NAME = "FINAL"


def create_translucent_trace(translucent_events: list[tuple[str, set[str, ...]]], name: Optional[str] = None) -> Trace:
    trace = Trace()
    if name is not None:
        trace.attributes["concept:name"] = name
    for translucent_event in translucent_events:
        event = Event()
        event["concept:name"] = translucent_event[0]
        event["enabled"] = translucent_event[1]
        trace.append(event)
    return trace


def add_artificial_end_transition(accepting_petri_net: tuple[PetriNet, Marking, Marking]) -> tuple[PetriNet, Marking, Marking]:
    accepting_petri_net = deepcopy(accepting_petri_net)
    artificial_end_transition = add_transition(accepting_petri_net[0], name=ARTIFICIAL_END_TRANSITION_NAME, label=ARTIFICIAL_END_TRANSITION_LABEL)
    for place in accepting_petri_net[2]:
        add_arc_from_to(place, artificial_end_transition, accepting_petri_net[0])
    artificial_final_place = add_place(accepting_petri_net[0], name=ARTIFICIAL_END_PLACE_NAME)
    add_arc_from_to(artificial_end_transition, artificial_final_place, accepting_petri_net[0])
    return accepting_petri_net[0], accepting_petri_net[1], place_set_as_marking([artificial_final_place])
