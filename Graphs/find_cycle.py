from graph_traversals import Graph
from typing import List


class DetectCycle:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.parents = {node: node for node in range(self.graph.num_nodes)}

    def find_parent(self, x):
        return x if self.parents[x] == x else self.find_parent(self.parents[x])

    def union(self, x, y):
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)
        if parent_x != parent_y:
            self.parents[parent_x] = parent_y

    def solve(self) -> bool:
        """
        Process all the edges one by one and unionize them if they belong to different subsets otherwise there's a cycle
        :return:
        """
        for edge in self.graph.edges:
            parent_x = self.find_parent(edge[0])
            parent_y = self.find_parent(edge[1])
            if parent_x == parent_y:
                return True
            self.union(parent_x, parent_y)
        return False

    def find_cycle_dfs(self, adjacencies: List[List[int]]) -> bool:
        adj_list = {i: adjacencies[i] for i in range(len(adjacencies))}
        visited = [False] * len(adj_list)

        def dfs_util(graph, vertex, visited, parent) -> bool:
            visited[vertex] = True
            for neighbor in graph[vertex]:
                if neighbor == parent:
                    continue
                if visited[neighbor]:
                    return True
                elif dfs_util(graph, neighbor, visited, vertex):
                    return True
            return False

        for vertex, adj in adj_list.items():
            if not visited[vertex]:
                if dfs_util(adj_list, vertex, visited, None):
                    return True

        return False


if __name__ == '__main__':
    """
    Given an undirected graph with V nodes and E edges. The task is to check if there is any cycle in undirected graph.
    Note: Solve the problem using disjoint set union(dsu).
    """
    graph_obj = Graph(5, False)

    graph_obj.add_edge((0, 2))
    graph_obj.add_edge((0, 3))
    graph_obj.add_edge((0, 4))
    graph_obj.add_edge((1, 3))
    graph_obj.add_edge((2, 4))

    isCycle = DetectCycle(graph=graph_obj)
    print(isCycle.solve())

    graph = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
    print(isCycle.find_cycle_dfs(graph))
