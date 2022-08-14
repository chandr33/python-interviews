class Solution:
    def __init__(self, num_sets):
        self.parent = {x: x for x in range(1, num_sets+1)}

    def find_parent(self, node) -> int:
        return node if self.parent[node] == node else self.find_parent(self.parent[node])

    def union(self, x, y):
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)
        if parent_x != parent_y:
            self.parent[parent_x] = parent_y

    def is_connected(self, x, y):
        return self.find_parent(x) == self.find_parent(y)


if __name__ == '__main__':
    '''
    This problem is to implement disjoint set union. There will be 2 incomplete functions namely union and find. 
    You have to complete these functions. 

    Union: Join two subsets into a single set.
    isConnected: Determine which subset a particular element is in. This can be used for determining if two elements are
    in same subset.
    '''
    union_find = Solution(5)
    union_find.union(1, 2)
    union_find.union(1, 3)
    union_find.union(1, 4)
    print(union_find.is_connected(3, 4))
    union_find.union(1, 5)
    print(union_find.is_connected(3, 5))
