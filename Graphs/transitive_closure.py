from .print_graph import Graph
from collections import deque
from typing import List


class Solution:
    def __init__(self, graph: Graph):
        self.graph = graph

    def solution(self) -> List[List[int]]:
        rows, cols = len(self.graph.adj_matrix), len(self.graph.adj_matrix[0])
        result = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = [False] * cols
        for i in range(rows):
            self.bfs_on_adj_matrix(i, visited, result)
            visited = [False] * cols
        return result

    def bfs_on_adj_matrix(self, starting_vertex, visited: List[bool], result: List[List[int]]):
        queue = deque()
        queue.append(starting_vertex)

        while queue:
            curr_index = queue.popleft()
            if not visited[curr_index]:
                visited[curr_index] = True
                for index, element in enumerate(self.graph.adj_matrix[curr_index]):
                    if element == 1 and index != curr_index:
                        queue.append(index)
                        result[starting_vertex][index] = 1
                    elif element == 1:
                        result[starting_vertex][index] = 1


if __name__ == '__main__':
    '''
    Given a directed graph, find out if a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the 
    given graph. Here reachable mean that there is a path from vertex i to j. The reach-ability matrix is called 
    transitive closure of a graph. The directed graph is represented by adjacency list graph where there are N vertices.
    '''

    graph_obj = Graph(4, directed=True)

    graph_obj.add_edge((0, 0))
    graph_obj.add_edge((0, 1))
    graph_obj.add_edge((0, 3))
    graph_obj.add_edge((1, 1))
    graph_obj.add_edge((1, 2))
    graph_obj.add_edge((2, 2))
    graph_obj.add_edge((2, 3))
    graph_obj.add_edge((3, 3))

    transitive_closure = Solution(graph=graph_obj)
    print(transitive_closure.solution())
