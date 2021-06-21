import heapq


class MaxHeap:

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)

    def top(self):
        return -self.data[0]

    def push(self, item):
        heapq.heappush(self.data, -item)

    def pop(self):
        return -heapq.heappop(self.data)

    def replace(self, item):
        return heapq.heapreplace(self.data, -item)


def find_kth_smallest(A, k):

    priority_queue = MaxHeap(A[0:k])

    for i in range(k, len(A)):
        if A[i] < priority_queue.top():
            priority_queue.replace(A[i])

    return priority_queue.top()
