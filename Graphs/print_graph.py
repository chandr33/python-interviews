from typing import List
from collections import deque


class Graph:
    def __init__(self, num_nodes: int, directed: bool = False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.adj_list = {node: set() for node in range(self.num_nodes)}
        self.adj_matrix = [[0 for _ in range(self.num_nodes)] for _ in range(self.num_nodes)]
        self.edges = []

    def add_edge(self, edge: tuple):
        self.edges.append(edge)
        self.adj_list[edge[0]].add(edge[1])
        row, col = edge
        self.adj_matrix[row][col] = 1
        if not self.directed:
            self.adj_list[edge[1]].add(edge[0])
            self.adj_matrix[edge[1]][edge[0]] = 1

    def print_graph_dfs_recursive(self, starting_node: int, visited: List[bool]):
        print(starting_node)
        visited[starting_node] = True
        for neighbor in self.adj_list[starting_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                self.print_graph_dfs_recursive(neighbor, visited)

    def print_graph_dfs_stack(self, starting_node: int, visited: List[bool]):
        stack = list()
        stack.append(starting_node)

        while len(stack) != 0:
            curr_node = stack.pop()
            if not visited[curr_node]:
                visited[curr_node] = True
                print(curr_node)
                for neighbor in self.adj_list[curr_node]:
                    stack.append(neighbor)

    def print_graph_bfs(self, starting_node: int, visited: List[bool]):
        queue = deque()
        queue.append(starting_node)

        while queue:
            curr_node = queue.popleft()
            if not visited[curr_node]:
                visited[curr_node] = True
                print(curr_node)
                neighbors = self.adj_list[curr_node]
                for neighbor in neighbors:
                    queue.append(neighbor)


if __name__ == '__main__':
    num_edges = 5
    graph_obj = Graph(num_edges)
    graph_obj.add_edge((0, 1))
    graph_obj.add_edge((0, 4))
    graph_obj.add_edge((1, 2))
    graph_obj.add_edge((1, 3))
    graph_obj.add_edge((1, 4))
    graph_obj.add_edge((2, 3))
    graph_obj.add_edge((3, 4))

    node_visited = [False]*num_edges
    # graph_obj.print_graph_dfs_recursive(1, node_visited)

    # graph_obj.print_graph_bfs(0, node_visited)

    graph_obj.print_graph_dfs_stack(1, node_visited)
