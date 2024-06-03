import heapq

class Solution:
    #Function to return the sorted array.
    def nearlySorted(self, arr, n, k):
        # j'initialise un tableau pour stocker les éléments triés
        sorted_arr = []

        # j'initialise un min-heap c'est un tableau qui va mettre les chiffres les plus bas près de la racine.
        min_heap = []

        # j'insere les k+1 premiers éléments dans le min-heap

        for i in range(min(k + 1, n)): # on prends les k+1 elements pour etre sur que ca va jamais depasser
            heapq.heappush(min_heap, arr[i])


        # Pour chaque élément restant dans le tableau
        for i in range(k + 1, n):
            # On extrait le minimum du tas et l'ajouter au tableau trié
            sorted_arr.append(heapq.heappop(min_heap))
            # On ajoute le prochain élément du tableau dans le tas
            heapq.heappush(min_heap, arr[i])


        # On ajoute les éléments restants du tas et les ajouter au tableau trié
        while min_heap:
            sorted_arr.append(heapq.heappop(min_heap))

        return sorted_arr
    


# application d'utilisation
obj = Solution()
arr = [30, 10, 89, 11, 3, 4, 5]
n = 7
k = 3
result = obj.nearlySorted(arr, n, k)
print("Sorted array:", result)
