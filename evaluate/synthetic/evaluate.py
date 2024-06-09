import pm4py
import time
from utils import create_translucent_trace
from pm4py.algo.conformance.alignments.petri_net.algorithm import Variants
from translucent_reachability_graph import TranslucentReachabilityGraph
from translucent_alignment import TranslucentAlignmentStateGraph
import matplotlib.pyplot as plt

def run_pm4py_state_equation_a_star(trace, net, im, fm):
    times = []
    i = 0
    while i < 5:
        start_time = time.time()
        pm4py.algo.conformance.alignments.petri_net.algorithm.apply_trace(trace, net, im, fm,
                                                                          variant=Variants.VERSION_STATE_EQUATION_A_STAR)
        end_time = time.time()
        times.append(end_time-start_time)
        i += 1
    return sum(times)/len(times)


def run_pm4py_tweaked_state_equation_a_star(trace, net, im, fm):
    times = []
    i = 0
    while i < 5:
        start_time = time.time()
        pm4py.algo.conformance.alignments.petri_net.algorithm.apply_trace(trace, net, im, fm,
                                                                          variant=Variants.VERSION_TWEAKED_STATE_EQUATION_A_STAR)
        end_time = time.time()
        times.append(end_time-start_time)
        i += 1
    return sum(times)/len(times)


def run_pm4py_dijkstra_no_heuristic(trace, net, im, fm):
    times = []
    i = 0
    while i < 5:
        start_time = time.time()
        pm4py.algo.conformance.alignments.petri_net.algorithm.apply_trace(trace, net, im, fm,
                                                                          variant=Variants.VERSION_DIJKSTRA_NO_HEURISTICS)
        end_time = time.time()
        times.append(end_time-start_time)
        i += 1
    return sum(times)/len(times)


def run_pm4py_dijkstra_less_memory(trace, net, im, fm):
    times = []
    i = 0
    while i < 5:
        start_time = time.time()
        pm4py.algo.conformance.alignments.petri_net.algorithm.apply_trace(trace, net, im, fm,
                                                                          variant=Variants.VERSION_DIJKSTRA_LESS_MEMORY)
        end_time = time.time()
        times.append(end_time-start_time)
        i += 1
    return sum(times)/len(times)


def run_translucent_alignment(trace, net, im, fm):
    times = []
    i = 0
    while i < 5:
        start_time = time.time()
        trg = TranslucentReachabilityGraph((net, im, fm))
        tasg = TranslucentAlignmentStateGraph(trg, trace)
        tasg.get_optimal_alignment()
        end_time = time.time()
        times.append(end_time-start_time)
        i += 1
        print(i)
    return sum(times)/len(times)


def state_equation_a_star(trace):
    runtimes = []
    net, initial_marking, final_marking = pm4py.read_pnml("a.pnml")
    runtimes.append(run_pm4py_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("ab.pnml")
    runtimes.append(run_pm4py_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abc.pnml")
    runtimes.append(run_pm4py_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcd.pnml")
    runtimes.append(run_pm4py_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcde.pnml")
    runtimes.append(run_pm4py_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdef.pnml")
    runtimes.append(run_pm4py_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefg.pnml")
    runtimes.append(run_pm4py_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefgh.pnml")
    runtimes.append(run_pm4py_state_equation_a_star(trace, net, initial_marking, final_marking))
    return runtimes


def tweaked_state_equation_a_star(trace):
    runtimes = []
    net, initial_marking, final_marking = pm4py.read_pnml("a.pnml")
    runtimes.append(run_pm4py_tweaked_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("ab.pnml")
    runtimes.append(run_pm4py_tweaked_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abc.pnml")
    runtimes.append(run_pm4py_tweaked_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcd.pnml")
    runtimes.append(run_pm4py_tweaked_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcde.pnml")
    runtimes.append(run_pm4py_tweaked_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdef.pnml")
    runtimes.append(run_pm4py_tweaked_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefg.pnml")
    runtimes.append(run_pm4py_tweaked_state_equation_a_star(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefgh.pnml")
    runtimes.append(run_pm4py_tweaked_state_equation_a_star(trace, net, initial_marking, final_marking))
    return runtimes


def dijkstra_no_heuristic(trace):
    runtimes = []
    net, initial_marking, final_marking = pm4py.read_pnml("a.pnml")
    runtimes.append(run_pm4py_dijkstra_no_heuristic(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("ab.pnml")
    runtimes.append(run_pm4py_dijkstra_no_heuristic(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abc.pnml")
    runtimes.append(run_pm4py_dijkstra_no_heuristic(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcd.pnml")
    runtimes.append(run_pm4py_dijkstra_no_heuristic(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcde.pnml")
    runtimes.append(run_pm4py_dijkstra_no_heuristic(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdef.pnml")
    runtimes.append(run_pm4py_dijkstra_no_heuristic(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefg.pnml")
    runtimes.append(run_pm4py_dijkstra_no_heuristic(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefgh.pnml")
    runtimes.append(run_pm4py_dijkstra_no_heuristic(trace, net, initial_marking, final_marking))
    return runtimes


def dijkstra_less_memory(trace):
    runtimes = []
    net, initial_marking, final_marking = pm4py.read_pnml("a.pnml")
    runtimes.append(run_pm4py_dijkstra_less_memory(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("ab.pnml")
    runtimes.append(run_pm4py_dijkstra_less_memory(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abc.pnml")
    runtimes.append(run_pm4py_dijkstra_less_memory(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcd.pnml")
    runtimes.append(run_pm4py_dijkstra_less_memory(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcde.pnml")
    runtimes.append(run_pm4py_dijkstra_less_memory(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdef.pnml")
    runtimes.append(run_pm4py_dijkstra_less_memory(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefg.pnml")
    runtimes.append(run_pm4py_dijkstra_less_memory(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefgh.pnml")
    runtimes.append(run_pm4py_dijkstra_less_memory(trace, net, initial_marking, final_marking))
    return runtimes


def translucent_alignment(trace):
    runtimes = []
    net, initial_marking, final_marking = pm4py.read_pnml("a.pnml")
    runtimes.append(run_translucent_alignment(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("ab.pnml")
    runtimes.append(run_translucent_alignment(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abc.pnml")
    runtimes.append(run_translucent_alignment(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcd.pnml")
    runtimes.append(run_translucent_alignment(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcde.pnml")
    runtimes.append(run_translucent_alignment(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdef.pnml")
    runtimes.append(run_translucent_alignment(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefg.pnml")
    runtimes.append(run_translucent_alignment(trace, net, initial_marking, final_marking))
    net, initial_marking, final_marking = pm4py.read_pnml("abcdefgh.pnml")
    runtimes.append(run_translucent_alignment(trace, net, initial_marking, final_marking))
    return runtimes


def main():
    translucent_trace = create_translucent_trace(
        [
            ("a", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("b", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("c", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("d", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("e", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("f", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("g", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("h", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("i", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("j", {"a", "b", "c", "d", "e", "f", "g", "h", "end"}),
            ("end", {"a", "b", "c", "d", "e", "f", "g", "h", "end"})
         ]
    )
    times_state_equation_a_star = state_equation_a_star(translucent_trace)
    times_tweaked_state_equation_a_star = tweaked_state_equation_a_star(translucent_trace)
    times_dijkstra_no_heuristic = dijkstra_no_heuristic(translucent_trace)
    times_dijkstra_less_memory = dijkstra_less_memory(translucent_trace)
    print("Start translucent")
    times_translucent = translucent_alignment(translucent_trace)
    print("Stop")
    print(times_state_equation_a_star)
    print(times_tweaked_state_equation_a_star)
    print(times_dijkstra_no_heuristic)
    print(times_dijkstra_less_memory)
    print(times_translucent)

    # List of all time lists
    all_times = [times_state_equation_a_star, times_tweaked_state_equation_a_star, times_dijkstra_no_heuristic, times_dijkstra_less_memory, times_translucent]
    labels = ["State Equation A*", "Tweaked State Equation A*", "Dijkstra No Heuristic", "Dijkstra Less Memory", "Translucent"]
    # Colors for the plots
    colors = ['b', 'g', 'r', 'c', 'm']  # Blue, Green, Red, Cyan, Magenta

    # X-axis values
    x = range(1, len(times_state_equation_a_star) + 1)

    # Create the plot
    plt.figure(figsize=(10, 6))

    # Plot each time list with a different color
    for i, times in enumerate(all_times):
        plt.plot(x, times, color=colors[i], label=labels[i])

    # Customize the legend
    plt.legend(fontsize=16)

    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.tick_params(axis='both', which='minor', labelsize=14)
    # Customize axis labels
    plt.xlabel('Number of Blocks', fontsize=18)
    plt.ylabel('Time (seconds)', fontsize=18)

    # Title (if needed)

    # Grid (optional)
    plt.grid(True)

    # Show the plot
    plt.savefig('measured_times_bigger.pdf', format='pdf', bbox_inches='tight')


main()