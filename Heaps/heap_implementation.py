from typing import Optional


class Heaps:
    def __init__(self):
        self.heap = []

    def get_parent(self, index):
        if index == 0:
            return 0
        elif (index-1)//2 >= 0:
            return (index-1)//2
        raise Exception("Parent does not exist")

    def has_left_child(self, index):
        return (2*index) + 1 <= len(self.heap) - 1

    def has_right_child(self, index):
        return (2*index) + 2 <= len(self.heap) - 1

    def get_smaller_child_index(self, index) -> int:
        if self.has_right_child(index) and self.heap[(2*index)+2] < self.heap[(2*index)+1]:
            return (2*index)+2
        return (2*index)+1

    def heapify_down(self):
        curr_index = 0
        while self.has_left_child(curr_index):
            smaller_child_index = self.get_smaller_child_index(curr_index)
            if self.heap[curr_index] < self.heap[smaller_child_index]:
                break
            else:
                temp = self.heap[curr_index]
                self.heap[curr_index] = self.heap[smaller_child_index]
                self.heap[smaller_child_index] = temp

            curr_index = smaller_child_index

    def heapify_up(self):
        curr_index = len(self.heap)-1
        while self.heap[self.get_parent(curr_index)] > self.heap[curr_index]:
            temp = self.heap[curr_index]
            self.heap[curr_index] = self.heap[self.get_parent(curr_index)]
            self.heap[self.get_parent(curr_index)] = temp
            curr_index = self.get_parent(curr_index)

    def heap_pop(self) -> Optional[int]:
        if len(self.heap) == 0:
            return None
        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down()
        return item

    def heap_push(self, element):
        self.heap.append(element)
        self.heapify_up()

    def get_bigger_child_index(self, arr, index, size) -> int:
        if (2*index) + 2 < size and arr[(2*index) + 2] > arr[(2*index) + 1]:  #  If right child exists and is bigger than left child
            return (2*index) + 2
        return (2*index) + 1

    def build_max_heap(self, arr):  # Heapify Up
        n = len(arr)
        for i in range(n):
            if arr[i] > arr[int((i-1)/2)]:  # Check if child is greater than parent
                curr_index = i
                while arr[curr_index] > arr[int((curr_index-1)/2)]:  # Heapify Up
                    (arr[curr_index], arr[int((curr_index-1)/2)]) = (arr[int((curr_index-1)/2)], arr[curr_index])
                    curr_index = int((curr_index-1)/2)

    def heap_sort(self, arr):
        self.build_max_heap(arr)
        n = len(arr)

        for i in range(n-1, 0, -1):
            (arr[0], arr[i]) = (arr[i], arr[0])  # Swap to get the largest element at the last position

            # Heapify Down to maintain heap property
            curr_index = 0

            while (2*curr_index)+1 < i:  # Loop until there's a left child
                larger_child_index = self.get_bigger_child_index(arr, curr_index, i)
                if arr[larger_child_index] <= arr[curr_index]:  # If children are smaller than the parent then heap property is restored
                    break
                else:
                    temp = arr[curr_index]
                    arr[curr_index] = arr[larger_child_index]
                    arr[larger_child_index] = temp

                curr_index = larger_child_index

        return arr


if __name__ == '__main__':
    heap = Heaps()
    heap.heap_push(1)
    heap.heap_push(-1)
    heap.heap_push(4)
    heap.heap_push(-10)
    heap.heap_pop()
    heap.heap_push(-14)
    heap.heap_push(0)
    heap.heap_pop()

    array = [10, 9, 13, -1, -8, 0, 12, 13, 14, 15]
    print(heap.heap_sort(array))

