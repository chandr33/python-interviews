from collections import defaultdict
from typing import List


class Prerequisites:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(set)

    def add_edge(self, x, y):
        self.graph[x].add(y)

    def is_cycle(self, vertex, visited, parent) -> bool:
        visited[vertex] = True
        parent[vertex] = True

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                if self.is_cycle(neighbor, visited, parent):
                    return True
            elif parent[neighbor]:
                return True

        parent[vertex] = False
        return False

    def solve(self, prerequisites: List[List[int]]) -> bool:
        """
        This problem boils down to finding a cycle in a directed graph. If a cycle exists then return False else True
        To find a cycle you have to go through the list of edges and keep on doing a union
        :return:
        """
        for prerequisite in prerequisites:
            self.add_edge(prerequisite[1], prerequisite[0])  # Create the dependency graph

        visited = [False] * self.num_vertices
        parent = [False] * self.num_vertices

        for vertex in range(len(prerequisites)):
            if not visited[vertex]:
                if self.is_cycle(vertex, visited, parent):
                    return False

        return True


if __name__ == '__main__':
    """
    There are a total of N tasks, labeled from 0 to N-1. Some tasks may have prerequisites, for example to do task 0 
    you have to first complete task 1, which is expressed as a pair: [0, 1]
    Given the total number of tasks N and a list of prerequisite pairs P, find if it is possible to finish all tasks.
    """

    # prerequisite = Prerequisites(2)
    #
    # prereqs_1 = [[1, 0]]
    # prereqs_2 = [[1, 0], [0, 1]]

    # print(prerequisite.solve(prereqs_1))
    # print(prerequisite.solve(prereqs_2))

    prerequisite = Prerequisites(6)

    prereqs_3 = [[2, 0], [2, 1], [4, 2], [4, 3], [5, 4]]  # True
    prereqs_4 = [[2, 0], [2, 1], [4, 2], [4, 3], [5, 4], [3, 5]]  # False
    prereqs_5 = [[2, 0], [2, 1], [4, 2], [4, 3], [5, 4], [5, 3]]  # True

    print(prerequisite.solve(prereqs_3))
    print(prerequisite.solve(prereqs_4))
    print(prerequisite.solve(prereqs_5))
