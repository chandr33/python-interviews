from .print_graph import Graph
from collections import deque


class Provinces:
    def __init__(self, num_vertices: int = 0):
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.num_vertices = num_vertices
        for row in range(num_vertices):
            for col in range(num_vertices):
                if row == col:
                    self.matrix[row][col] = 1

    def add_edge(self, x, y):
        self.matrix[x][y] = 1
        self.matrix[y][x] = 1

    def num_provinces_dfs(self):
        def count_provinces(adj_matrix, curr_vertex, visited) -> None:
            visited[curr_vertex] = True
            for neighbor, val in enumerate(adj_matrix[curr_vertex]):
                if val == 1 and neighbor != curr_vertex and not visited[neighbor]:
                    count_provinces(adj_matrix, neighbor, visited)
        visited = [False]*self.num_vertices
        count = 0
        for i in range(len(self.matrix)):
            if not visited[i]:
                count_provinces(self.matrix, 0, visited)
                count = count + 1
        return count

    def num_provinces_bfs(self) -> int:
        queue = deque()
        visited = [False] * self.num_vertices
        count = 0
        for i in range(len(self.matrix)):
            if not visited[i]:
                queue.append(i)
                count += 1
                while queue:
                    curr_vertex = queue.popleft()
                    if not visited[curr_vertex]:
                        visited[curr_vertex] = True
                        for neighbor, val in enumerate(self.matrix[curr_vertex]):
                            if val == 1 and curr_vertex != neighbor and not visited[neighbor]:
                                queue.append(neighbor)

        return count


if __name__ == '__main__':
    """
    Given an undirected graph with V vertices. We say two vertices u and v belong to a single province if there is a 
    path from u to v or v to u. Your task is to find the number of provinces.

    Note: A province is a group of directly or indirectly connected cities and no other cities outside of the group.
    """

    graph_obj = Graph(3, False)

    provinces = Provinces(num_vertices=3)
    provinces.add_edge(0, 2)
    provinces.add_edge(1, 2)

    print(provinces.num_provinces_dfs())
    print(provinces.num_provinces_bfs())
