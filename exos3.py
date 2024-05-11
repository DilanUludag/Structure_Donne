import heapq

def kLargest(arr, N, k):
    # Initialize a min heap
    heap = []

    # Push first k elements into the heap
    for i in range(k):
        heapq.heappush(heap, arr[i])

    # Iterate over the remaining elements in the array
    for i in range(k, N):
        # If the current element is larger than the smallest element in the heap
        if arr[i] > heap[0]:
            # Pop the smallest element from the heap
            heapq.heappop(heap)
            # Push the current element into the heap
            heapq.heappush(heap, arr[i])

    # The k largest elements will be present in the heap
    # Return them in descending order
    return sorted(heap, reverse=True)

# Example usage:
arr1 = [12, 5, 787, 1, 23]
N1 = 5
k1 = 2
print(kLargest(arr1, N1, k1))  # Output: [787, 23]

arr2 = [1, 23, 12, 9, 30, 2, 50]
N2 = 7
k2 = 3
print(kLargest(arr2, N2, k2))  # Output: [50, 30, 23]
