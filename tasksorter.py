#!/usr/bin/python

"""
Loads up a .task file, that may or may not contain cycles. It sorts these
tasks. If there are no cycles, it will do a basic topological sort. However if
there is a cycle, it will first find the strong components, and then it will
sort those strong components topologically.

It relies on both a Digraph object, and a TopologicalSorter non-instantiable
class. The APIs for these are given in the assignment.

Note that because you will be probably be using recursive methods, that this
program might overrun the stack very easily. You may have to increase the stack
size in your code.
"""

__author__ = "Adam A. Smith"
__version__ = "2023.11.12"

from digraph import Digraph
import topologicalsorter

# load a rask file & make a Digraph from its lines
def make_digraph_from_task_file(filename):
    digraph = Digraph()

    # read the file
    with open(filename, 'r') as file:
        for line in file:
            tokens = line.strip().split("\t")
            tokens = [token.strip() for token in tokens]
            
            # make sure that all these vertices are added
            for token in tokens:
                if not digraph.is_valid_vertex(token): digraph.add_vertex(token)

            # scan thru again & add edges
            for i in range(1, len(tokens)):
                digraph.add_edge(tokens[i], tokens[0])
    
    return digraph

# find if it has cycles, and do 2 different approaches based on that
def sort_and_report(file_name, digraph):
    # has cycles
    if topologicalsorter.is_directed_cycle(digraph):
        print('The file "' + file_name + '" contains ' + str(len(digraph)) + ' tasks, some of which are mutually dependent. You must:')

        # sort & print the strong components
        strong_components = topologicalsorter.find_strong_components(digraph)
        for i in range(len(strong_components)):
            component = strong_components[i]
            print("  " + str(i+1) + ". " + component[0], end="")
            for j in range(1, len(component)):
                print(", " + component[j], end="")
            print()

    # no cycles--just a plain topological sort
    else:
        print('The file "' + file_name + '" contains ' + str(len(digraph)) + ' tasks, with no cycles. You must:')

        # get basic topo sort & print it
        order = topologicalsorter.sort_topologically(digraph)
        for i in range(len(order)):
            print("  " + str(i+1) + ". " + order[i])

# pseudo main() function
if __name__ == "__main__":
    # test command-line args
    from sys import argv, exit, stderr

    # make sure we have a file
    if len(argv) != 2:
        print("Please enter a file name!", file=stderr)
        exit(1)

    # make the graph, and print out the ordering  
    try:
        digraph = make_digraph_from_task_file(argv[1])
        sort_and_report(argv[1], digraph)
    except IOError:
        print("Couldn't open file \"" + argv[1] + "\".", file=stderr)
        exit(1)