# -*- coding: utf-8 -*-



# Min heap data structure
# with decrease key functionality - in O(log(n)) time


class MinHeap:

    def __init__(self, array):
        self.idx_of_element = {}
        self.heap_dict = {} #
        self.heap = self.build_heap(array)

    def __getitem__(self, key): #
        return self.heap_dict[key]

    def insert(self, node):
        self.heap.append(node)
        self.idx_of_element[node[0]] = len(self.heap) - 1
        self.heap_dict[node[0]] = node[1]  #
        self.sift_up(len(self.heap) - 1)

    def build_heap(self, array):
        lastIdx = len(array) - 1
        startFrom = (lastIdx - 1) // 2

        for idx, i in enumerate(array):
            self.idx_of_element[i[0]] = idx
            self.heap_dict[i[0]] = i[1]

        for i in range(startFrom, -1, -1):
            self.sift_down(i, array)
        return array

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.idx_of_element[self.heap[0][0]], self.idx_of_element[self.heap[-1][0]] = (
            self.idx_of_element[self.heap[-1][0]],
            self.idx_of_element[self.heap[0][0]],
        )

        x = self.heap.pop()
        del self.idx_of_element[x[0]]
        del self.heap_dict[x[0]]
        self.sift_down(0, self.heap)
        return x

    def increase_key(self, name, newValue):
        assert (
                self.heap[self.idx_of_element[name]][1] <= newValue
        ), "newValue must be larges that current value"
        self.heap[self.idx_of_element[name]][1] = newValue
        self.heap_dict[name] = newValue  #
        self.sift_down(self.idx_of_element[name], self.heap)

    def decrease_key(self, name, newValue):
        assert (
                self.heap[self.idx_of_element[name]][1] >= newValue
        ), "newValue must be less that current value"
        self.heap[self.idx_of_element[name]][1] = newValue
        self.heap_dict[name] = newValue  #
        self.sift_up(self.idx_of_element[name])

    # this is min-heapify method
    def sift_down(self, idx, array):
        while True:
            l = idx * 2 + 1
            r = idx * 2 + 2

            smallest = idx
            if l < len(array) and array[l][1] < array[idx][1]:
                smallest = l
            if r < len(array) and array[r][1] < array[smallest][1]:
                smallest = r

            if smallest != idx:
                array[idx], array[smallest] = array[smallest], array[idx]
                (
                    self.idx_of_element[array[idx][0]],
                    self.idx_of_element[array[smallest][0]],
                ) = (
                    self.idx_of_element[array[smallest][0]],
                    self.idx_of_element[array[idx][0]],
                )
                idx = smallest
            else:
                break

    def sift_up(self, idx):
        p = (idx - 1) // 2
        while p >= 0 and self.heap[p][1] > self.heap[idx][1]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            self.idx_of_element[self.heap[p][0]], self.idx_of_element[self.heap[idx][0]] = (
                self.idx_of_element[self.heap[idx][0]],
                self.idx_of_element[self.heap[p][0]],
            )  # 
            idx = p
            p = (idx - 1) // 2

    def peek(self):
        return self.heap[0]


class MaxHeap:

    def __init__(self, array):
        self.idx_of_element = {}
        self.heap_dict = {} #
        self.heap = self.build_heap(array)
    #def __getitem__(self, key): #
    #    return self.heap_dict[key]
    def insert(self, node):
        self.heap.append(node)
        self.idx_of_element[node[0]] = len(self.heap) - 1
        self.heap_dict[node[0]] = node[1] #
        self.sift_up(len(self.heap) - 1)

    def build_heap(self, array):
        lastIdx = len(array) - 1
        startFrom = (lastIdx - 1) // 2

        for idx, i in enumerate(array):
            self.idx_of_element[i[0]] = idx
            self.heap_dict[i[0]] = i[1]

        for i in range(startFrom, -1, -1):
            self.sift_down(i, array)
        return array

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.idx_of_element[self.heap[0][0]], self.idx_of_element[self.heap[-1][0]] = (
            self.idx_of_element[self.heap[-1][0]],
            self.idx_of_element[self.heap[0][0]],
        )

        x = self.heap.pop()
        del self.idx_of_element[x[0]]
        del self.heap_dict[x[0]]
        self.sift_down(0, self.heap)
        return x

    def increase_key(self, name, newValue):
        assert (
                self.heap[self.idx_of_element[name]][1] <= newValue
        ), "newValue must be less that current value"
        self.heap[self.idx_of_element[name]][1] = newValue
        self.heap_dict[name] = newValue  #
        self.sift_up(self.idx_of_element[name])

    def decrease_key(self, name, newValue):
        assert (
                self.heap[self.idx_of_element[name]][1] >= newValue
        ), "newValue must be less that current value"
        self.heap[self.idx_of_element[name]][1] = newValue
        self.heap_dict[name] = newValue #
        self.sift_down(self.idx_of_element[name], self.heap)

    # this is max-heapify method
    def sift_down(self, idx, array):
        while True:
            l = idx * 2 + 1
            r = idx * 2 + 2

            largest = idx
            if l < len(array) and array[l][1] > array[idx][1]:
                largest = l
            if r < len(array) and array[r][1] > array[largest][1]:
                largest = r

            if largest != idx:
                array[idx], array[largest] = array[largest], array[idx]
                (
                    self.idx_of_element[array[idx][0]],
                    self.idx_of_element[array[largest][0]],
                ) = (
                    self.idx_of_element[array[largest][0]],
                    self.idx_of_element[array[idx][0]],
                )
                idx = largest
            else:
                break

    def sift_up(self, idx):
        p = (idx - 1) // 2
        while p >= 0 and self.heap[p][1] < self.heap[idx][1]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            self.idx_of_element[self.heap[p][0]], self.idx_of_element[self.heap[idx][0]] = (
                self.idx_of_element[self.heap[idx][0]],
                self.idx_of_element[self.heap[p][0]],
            )  # 
            idx = p
            p = (idx - 1) // 2

    def peek(self):
        return self.heap[0]


if __name__ == "__main__":
    a = ["10", 10]
    r = ["16", 16]
    b = ["14", 14]
    x = ["8", 8]
    e = ["7", 7]
    # Use one of these two ways to generate Min-Heap
    # Generating Min-Heap from array
    # myMaxHeap=MaxHeap([a,b,x,r,e])

    # Generating Min-Heap by Insert method

    myMaxHeap = MaxHeap([])
    myMaxHeap.insert(a)
    myMaxHeap.insert(b)
    myMaxHeap.insert(x)
    myMaxHeap.insert(r)
    myMaxHeap.insert(e)
    print("............")
    print(myMaxHeap.heap_dict['8'])
    print("..............")
    # Before
    print("Max Heap - before increase key")
    for i in myMaxHeap.heap_dict:
        print(i)

    print("Max Heap - After increase key of node")
    myMaxHeap.decrease_key("7", -17)
    print("............")
    print(myMaxHeap.heap_dict['7'])
    print("..............")
    # After
    for i in myMaxHeap.heap_dict:
        print(i)

    print(myMaxHeap.remove())
    for i in myMaxHeap.heap:
        print(i)
