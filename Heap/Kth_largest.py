import heapq


def find_kth_largest(arr, k):

    priority_queue = arr[0:k]
    heapq.heapify(priority_queue)

    for i in range(k, len(arr)):
        if arr[i] > priority_queue[0]:
            heapq.heapreplace(priority_queue, arr[i])

    return priority_queue[0]


print(find_kth_largest([7, 4, 6, 3, 9, 1], 2))
