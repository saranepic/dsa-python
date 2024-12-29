class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    def print_tree(self):
        for vertex in self.adjacency_list:
            print(f'{vertex} -> {self.adjacency_list[vertex]}')
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            self.adjacency_list.pop(vertex)
            for vertexes in self.adjacency_list:
                if vertex in self.adjacency_list[vertexes]:
                    self.adjacency_list[vertexes].remove(vertex)
            return True
        return False

g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_edge('C','A')
g.add_edge('A','B')
g.print_tree()
g.remove_vertex('B')
g.print_tree()