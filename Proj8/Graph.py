import random
import copy


class Graph(object):
    class Edge(object):
        def __init__(self, source, destination, weight):
            """
            DO NOT EDIT!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: Vertex where this edge ends
            :param weight: Value associated with this edge
            """
            self.source = source
            self.destination = destination
            self.weight = weight

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination} Weight: {self.weight}"

        __str__ = __repr__

    class Path(object):
        def __init__(self, vertices=list(), weight=0):
            """
            DO NOT EDIT!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            :param weight: Total weight of the path
            """
            self.vertices = vertices
            self.weight = weight

        def __eq__(self, other):
            return self.vertices == other.vertices and self.weight == other.weight

        def __repr__(self):
            return f"Weight:{self.weight} Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add a vertex id to the path
            :param vertex: id of a vertex
            :return: None
            """
            self.vertices.append(vertex)

        def add_weight(self, weight):
            """
            Add weight to the path
            :param weight: weight
            :return: None
            """
            self.weight += weight

        def remove_vertex(self):
            """
            Remove the most recently added vertex from the path
            :return: None
            """
            if not self.is_empty():
                self.vertices.pop()

        def is_empty(self):
            """
            Check if the path object is empty
            :return: True if empty, False otherwise
            """
            return len(self.vertices) == 0

    class Vertex(object):
        def __init__(self, number):
            """
            Class representing a vertex in the graph
            :param number: Unique id of this vertex
            """
            self.edges = []
            self.id = number
            self.visited = False

        def __repr__(self):
            return f"Vertex: {self.id}"

        __str__ = __repr__

        def add_edge(self, destination, weight):
            """
            function to add an edge to the Vertex
            :param destination: Ending vertex of edge
            :param weight: Weight of edge
            :return: None
            """
            self.edges.append(Graph.Edge(self.id, destination, weight))  # append edge object to end of list

        def degree(self):
            """
            Number of edges of a vertex
            :return: Number of edges connected to vertex
            """
            return len(self.edges)

        def get_edge(self, destination):
            """
            Find specified edge of vertex
            :param destination:
            :return: Edge
            """
            for elm in self.edges:
                if elm.destination == destination:
                    return elm
            return None

        def get_edges(self):
            """
            All the edges of the vertex
            :return: list of Edges
            """
            return self.edges

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: List of edges
        """
        random.seed(10)
        edges = []
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    edges.append([i, j, random.randint(-10, 50)])
        return edges

    def __init__(self, size=0, connectedness=0):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        """
        assert connectedness <= 1
        self.adj_map = {}
        self.size = size
        self.connectedness = connectedness
        self.construct_graph()

    def construct_graph(self):
        """
        Create graph
        :return: None
        """
        edges = self.generate_edges()  # create a set of edges
        for i in range(self.size):
            self.adj_map[i] = Graph.Vertex(i)  # initialize adj_map with vertices
        for elm in edges:  # update adj_map with edge information
            self.insert_edge(elm[0], elm[1], elm[2])


    def vertex_count(self):
        """
        Specify the amount of vertices in graph
        :return: number of vertices
        """
        return self.size

    def vertices(self):
        """
        Display a list of vertices
        :return: list of vertices
        """
        return self.adj_map.values()

    def insert_edge(self, source, destination, weight):
        """
        Inserts an edge into the graph between vertices
        :param source: origin vertex
        :param destination: destination vertex
        :param weight: weight of edge between origin and destination
        :return: None
        """
        edge = self.adj_map[source].get_edge(destination)
        if edge:  # if edge exist, update weight
            edge.weight = weight
            return  # return after update to not make new edge object
        self.adj_map[source].add_edge(destination, weight)  # add new edge to graph

    def find_valid_paths(self, source, destination, limit):
        """
        List of all valid paths in the graph
        :param source: origin vertex
        :param destination: destination vertex
        :param limit: weight limit of valid paths
        :return: List of valid paths
        """
        if source == destination:  # condition if source and destination is the same
            return
        paths = []
        new_paths = []
        trans_path = Graph.Path([], 0)  # initialize path object
        vertex = self.adj_map[source]  # initialize vertex
        vertex.visited = True  # visit vertex
        trans_path.add_vertex(source)    # add vertex to path
        for edge in vertex.edges:  # transverse through edges
            if not self.adj_map[edge.destination].visited:
                trans_path.add_weight(edge.weight)  # add edge weight to path
                self.find_valid_helper(edge.destination, destination, trans_path, paths)  # recur into helper function
                trans_path.add_weight(edge.weight*-1)  # remove weight of edge
                trans_path.remove_vertex()  # remove vertex
                self.adj_map[edge.destination].visited = False  # allow vertex to be visited
        for path in paths:  # remove all paths over limit
            if path.weight < limit:
                new_paths.append(path)
        return new_paths

    def find_valid_helper(self, helper_source, helper_destination, path, paths):
        """
        Helper function to aid in recursion of original find_valid_paths function
        :param helper_source: Origin vertex
        :param helper_destination: Destination vertex
        :param path: path object to manipulate
        :param paths: list of paths to append too
        :return: None
        """
        current = self.adj_map[helper_source]  # initialize current vertex
        path.add_vertex(current.id)  # add current vertex to path
        current.visited = True  # visit current vertex
        if helper_source == helper_destination:  # append path to list of paths when at destination
            target_path = copy.deepcopy(path)
            paths.append(target_path)
        else:
            for edge in self.adj_map[helper_source].edges:  # transverse through edges of next vertex
                if not self.adj_map[edge.destination].visited:  # if vertex hasn't been visited
                    edge_des = self.adj_map[edge.destination]
                    path.add_weight(edge.weight)  # add edge weight
                    self.find_valid_helper(edge_des.id, helper_destination, path, paths)  # recur through helper function
                    path.add_weight(edge.weight * -1)  # remove weight of edge
                    path.remove_vertex()  # remove vertex
                    edge_des.visited = False  # allow vertex to be visited



    def find_shortest_path(self, source, destination, limit):
        """
        shortest path in graph
        :param source: origin vertex
        :param destination: destination vertex
        :param limit: weight limit
        :return: shortest path
        """
        paths = self.find_valid_paths(source, destination, limit)
        _min = limit
        shortest = None
        for path in paths:
            if path.weight < _min:  # condition to find min_weight path
                _min = path.weight
                shortest = path
        return shortest

    def find_longest_path(self, source, destination, limit):
        """
        longest path in graph
        :param source: origin vertex
        :param destination: destination vertex
        :param limit: weight limit
        :return: longest path
        """
        paths = self.find_valid_paths(source, destination, limit)
        _max = 0
        longest = None
        for path in paths:
            if path.weight > _max:  # condition to find max_weight path
                _max = path.weight
                longest = path
        return longest

    def find_most_vertices_path(self, source, destination, limit):
        """
        path with most vertex in graph
        :param source: origin vertex
        :param destination: destination vertex
        :param limit: weight limit
        :return: path with most vertex
        """
        paths = self.find_valid_paths(source, destination, limit)
        vertex_max = 0
        most = None
        for path in paths:
            v_amount = len(path.vertices)
            if v_amount > vertex_max:  # condition to find most vertex path
                vertex_max = v_amount
                most = path
        return most


    def find_least_vertices_path(self, source, destination, limit):
        """
        path with least vertex in graph
        :param source: origin vertex
        :param destination: destination vertex
        :param limit: weight limit
        :return: path with least vertex
        """
        paths = self.find_valid_paths(source, destination, limit)
        vertex_min = 1000000000
        least = None
        for path in paths:
            v_amount = len(path.vertices)
            if v_amount < vertex_min:  # condition to find min vertex path
                vertex_min = v_amount
                least = path
        return least