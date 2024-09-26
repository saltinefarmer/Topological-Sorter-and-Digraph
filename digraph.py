class Digraph:
    """

        The Digraph class creates a Digraph object. Vertices can be added, along with
        directed edges. It can also create a reverse Digraph from its own data.

    """
    __author__ = "Silver Lippert"
    __version__ = "2023.12.3"

    edges = {}

    # inserts a vertex into the digraph. raises value error
    # if a vertex by that name already exists
    def add_vertex(self, name: str):
        """
            The add-vertex method accepts a name as a string, and create a vertex
            in the digraph with that name. It will raise a value error if the
            vertex is already within the graph.
        """
        try:
            self.edges[name]
        except KeyError:
            self.edges[name] = set()
        else:
            raise ValueError("This vertex is already within the graph.")

    # Adds a new one way edge from first vertex to the second. raises
    # value error if the vertices DNE
    def add_edge(self, vertex1: str, vertex2: str):
        """
            The add_edge method accepts the names of two vertices. The edge will be directed
            from vertex1 to vertex2, and not the other way around. If one or both of
            the vertices are not within the graph, it will raise a value error.
        """
        try:
            self.edges[vertex1]
            self.edges[vertex2]
        except KeyError:
            raise ValueError("One or both of these vertices are not within the graph.")
        else:
            self.edges[vertex1].add(vertex2)

    # removes an edge from the first vertex to the second. Will not
    # affect edges going in other direction. Returns bool indicating
    # success. Raises value error if vertices DNE
    def delete_edge(self, vertex1: str, vertex2: str)-> bool:
        """
            The delete_edge method accepts two vertices as input. It will delete
            and edge from vertex1 to vertex2. If an edge exists from vertex2 to
            vertex1, that edge will remain intact. It will return a boolean indicating if
            the deletion was a success. It will return false if an edge did not exist,
            and will raise a value error if one or both of the vertices are
            not within the graph.
        """
        try:
            self.edges[vertex1]
            self.edges[vertex2]
        except KeyError:
            raise ValueError("One or both of these vertices are not within the graph.")
        else:
            if vertex2 in self.edges[vertex1]:
                self.edges[vertex1].remove(vertex2)
                return True
            else:
                return False

    # returns true if vertex exists, false otherwise
    def is_valid_vertex(self, vertex: str)-> bool:
        """
            The is_valid_vertex method accepts the name of a vertex as an input,
            and checks if the vertex is within the graph. It will return a 
            boolean indicating as such.
        """
        try:
            self.edges[vertex]
        except KeyError:
            return False
        else:
            return True

    # gets list of all other vertices that this vertex has an edge to/
    # may return list of len 0 if vertex has no outward edges
    def get_adjacency_list(self, vertex: str)-> []:
        """
            The get_adjacency_list method accepts the name of a vertex as input,
            and returns a list of all the vertices it has an edge leading out to.
            It will not return any vertices that have an edge leading into it.
        """
        return list (self.edges[vertex])

    # returns array of all vertices
    def get_vertices(self)-> []:
        """
            The get_vertices method returns a list of all the vertices
            within the graph.
        """
        return list(self.edges)

    # returns new digraph with same vertices but edges in 
    # opposite directions
    def make_reverse_graph(self):
        """
            The make_reverse_graph method takes the digraph and returns a new digraph
            with all the directions of the edges reversed.
        """
        rev_graph = Digraph()
        rev_graph.edges = self.edges.copy() # make it a copy so the changes wont affect the regular digraph
        rev_graph.edges.clear() # clear it now that it is its own list

        for item in list(self.edges):
            try:
                rev_graph.add_vertex(item)
            except ValueError:
                pass
            for item2 in list(self.edges[item]):
                try:
                    rev_graph.add_vertex(item2)
                except ValueError:
                    pass
                rev_graph.add_edge(item2, item)
        return rev_graph
    

    # returns number of vertices in the digraph
    def __len__(self)-> int:
        return len(self.edges)