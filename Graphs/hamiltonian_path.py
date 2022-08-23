from collections import defaultdict


class Hamiltonian:
    def __init__(self, edges, num_vertices, num_edges):
        self.edge_list = edges
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.graph = defaultdict(set)
        self.add_edge()

    def add_edge(self):
        for edge in self.edge_list:
            self.graph[edge[0]].add(edge[1])

    def check(self) -> bool:
        def util(vertex, visited, path) -> bool:
            if len(path) == self.num_vertices:  # Found the hamiltonian path
                return True
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    if util(neighbor, visited, path + [neighbor]):
                        return True
                    visited[neighbor] = False  # back-tracking step
            return False

        for start in range(self.num_vertices):
            path = [start]
            visited = [False] * self.num_vertices
            visited[start] = True
            if util(start, visited, path):
                return True
        return False


if __name__ == '__main__':
    """
    A Hamiltonian path, is a path in an undirected or directed graph that visits each vertex exactly once. 
    Given an undirected graph the task is to check if a Hamiltonian path is present in it or not.
    Input:
    N = 4, M = 4
    Edges[][]= { {1,2}, {2,3}, {3,4}, {2,4} }
    Output:
    1 
    Explanation: 
    There is a hamiltonian path: 
    1 -> 2 -> 3 -> 4 
    """

    edge_list_1 = [[0, 1], [1, 2], [2, 3], [1, 3]]
    edge_list_2 = [[0, 1], [1, 2], [1, 3]]
    hamiltonian = Hamiltonian(edge_list_2, 4, 3)
    print(hamiltonian.check())
