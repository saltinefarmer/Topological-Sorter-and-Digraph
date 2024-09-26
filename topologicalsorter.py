"""
    The topological sorter imports the Digraph object, and defines methods
    that can be used to manipulate the data from the digraph. It can check
    for cycles, sort the digraph topologically, and find strongly
    connected components.
"""

__author__ = "Silver Lippert"
__version__ = "2023.12.3"

from digraph import Digraph

# returns true if there is at least one cycle in the graph
def is_directed_cycle(digraph: Digraph)-> bool:
    """
        The is_directed_cycle method accepts a digraph as input, and will 
        figure out if the graph is acyclic or not. It will return a boolean
        as such.
    """
    open_list = list(digraph.edges.keys())
    closed_list = set()
    found = False
    for item in open_list:
            if item not in closed_list:
                found = __find_cycle(digraph, open_list, closed_list, set(), item) # recursive helper method
                if found == True:
                    return True
            
    return False

# returns a sorted array of all the vertices, so that each
# vertex is listed before all the others to which it has an edge
def sort_topologically(digraph: Digraph)-> []:
    """
        The sort_topologically method accepts a digraph as input, and will return a list of
        all the vertices sorted in topological order.
    """
    marked = dict([(x, False) for x in digraph.get_vertices()])
    list = [None] * len(digraph)
    index = [len(digraph)-1]

    for item in digraph.get_vertices():
        if marked[item] == True:
            continue
        __topo_sort(digraph, item, marked, list, index) # recursive helper method

    return list

# returns 2D sorted list of all the vertices. Every elem of the list
# is an list of vertices in one strongly connected component
def find_strong_components(digraph: Digraph)-> []:
    """
        The find_strong_components method accepts a digraph as input, and returns a 2D list
        containing all of the strongly connected components. Each list is its own
        strongly connected component.
    """
    rev_graph = digraph.make_reverse_graph()

    topo_rev = sort_topologically(rev_graph)

    return_list = []
    rev_marked = dict([(x, False) for x in topo_rev])
    for item in topo_rev:
        if not rev_marked[item]:
            return_list.append(__do_DFT(digraph, rev_marked, [], item)) # recursive helper method
    return_list = return_list[::-1]
    return return_list

# return list of strong components
def __do_DFT(digraph: Digraph, rev_marked: {}, strong_comp_list: [], vertex)-> []:
    strong_comp_list.append(vertex)
    rev_marked[vertex] = True
    adjacent = digraph.get_adjacency_list(vertex)
    
    for item in adjacent:
        if rev_marked[item]:
            continue
        __do_DFT(digraph, rev_marked, strong_comp_list, item)
        rev_marked[item] = True
    return strong_comp_list

# recursive function for topological sorting
def __topo_sort(digraph: Digraph, vertex, marked: {}, list: [], index: []):

    marked[vertex] = True

    for item in digraph.get_adjacency_list(vertex):
        if not marked[item]:
            __topo_sort(digraph, item, marked, list, index)

    list[index[0]] = vertex
    index[0]-= 1

# recursive function for finding cycles
def __find_cycle(digraph: Digraph, open: [], closed: {}, stack: {}, vertex)-> bool:

    stack.add(vertex)
    for item in digraph.get_adjacency_list(vertex):
            if item in stack:
                return True
            if item in closed:
                continue
            succ = __find_cycle(digraph, open, closed, stack, item)
            if succ:
                return succ
            else:
                stack.remove(item)
                closed.add(item)
    
    return False
