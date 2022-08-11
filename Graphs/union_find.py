class Solution:
    def __init__(self, num_sets):
        self.parent = {x: x for x in range(1, num_sets+1)}

    def findParent(self, node) -> int:
        if self.parent[node] == node:
            return node
        return self.findParent(self.parent[node])

    def union(self, x, y):
        parent_x = self.findParent(x)
        parent_y = self.findParent(y)
        self.parent[parent_x] = parent_y

    def isConnected(self, x, y):
        parent_x = self.findParent(x)
        parent_y = self.findParent(y)

        return parent_y == parent_x


if __name__ == '__main__':
    '''
    This problem is to implement disjoint set union. There will be 2 incomplete functions namely union and find. 
    You have to complete these functions. 

    Union: Join two subsets into a single set.
    isConnected: Determine which subset a particular element is in. This can be used for determining if two elements are
    in same subset.
    '''
    union_find = Solution(5)
    union_find.union(1, 3)
    print(union_find.isConnected(1, 2))
    union_find.union(1, 5)
    print(union_find.isConnected(3, 5))
