import heapq

class Solution:
    #Function to return the sorted array.
    def nearlySorted(self, arr, n, k):
        # Initialiser un tableau pour stocker les éléments triés
        sorted_arr = []

        # Initialiser un min-heap
        min_heap = []

        # Insérer les k premiers éléments dans le min-heap
        for i in range(min(k + 1, n)):
            heapq.heappush(min_heap, arr[i])

        # Pour chaque élément restant dans le tableau
        for i in range(k + 1, n):
            # Extraire le minimum du tas et l'ajouter au tableau trié
            sorted_arr.append(heapq.heappop(min_heap))
            # Ajouter le prochain élément du tableau dans le tas
            heapq.heappush(min_heap, arr[i])

        # Extraire les éléments restants du tas et les ajouter au tableau trié
        while min_heap:
            sorted_arr.append(heapq.heappop(min_heap))

        return sorted_arr

# Exemple d'utilisation
obj = Solution()
arr = [30, 10, 89, 11, 3, 4, 5]
n = 7
k = 3
result = obj.nearlySorted(arr, n, k)
print("Sorted array:", result)
