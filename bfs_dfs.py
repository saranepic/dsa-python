class graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex]=[]
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])
    
    def add_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self,vertex1,vertex2):
        try:
            if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            return False
        except ValueError as e:
            print(f"No edge between {vertex1} and {vertex2}")
    
    def remove_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            self.adjacency_list.pop(vertex)
            print("Done")
            for vertexes in self.adjacency_list:
                if vertex in self.adjacency_list[vertexes]: 
                    self.adjacency_list[vertexes].remove(vertex)
            return True
        return False

    def bfs(self,vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
        print(visited)
    def dfs(self,vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop()
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
        print(visited)

custom_graph = graph()
custom_graph.add_vertex("A")
custom_graph.add_vertex("B")
custom_graph.add_vertex("C")
custom_graph.add_edge("A","B")
custom_graph.add_edge("A","C")
custom_graph.print_graph()
print("---------")
custom_graph.bfs("A")
print("---------")
custom_graph.dfs("A")
