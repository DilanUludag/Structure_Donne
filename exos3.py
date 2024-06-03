import heapq

class Solution:
    # Function to return k largest elements from an array.
    def kLargest(self, arr, N, k):
        # Initialize a min heap
        heap = []

        # on ajoute les k premiers elements au heap
        for i in range(k):
            heapq.heappush(heap, arr[i])

        # on itere sur les elements restants
        for i in range(k, N):
            # si il est plus grand que le plus petit élément
            if arr[i] > heap[0]:
                # on supprime le plus petit element
                heapq.heappop(heap)
                # on ajoute l'élément au heap
                heapq.heappush(heap, arr[i])

        # Return them in descending order
        return sorted(heap, reverse=True)


# {
# Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n = li[0]
    k = li[1]
    li = [int(x) for x in input().strip().split()]
    ob = Solution()
    k_largest_list = ob.kLargest(li, n, k)

    for element in k_largest_list:
        print(element, end=' ')
    print('')
# } Driver Code Ends