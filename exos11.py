# User function Template for python3
class Solution:
    def matchPairs(self, nuts, bolts, n):
        # On appelle la fonction de tri QuickSort pour trier les écrous et les boulons et du début à la fin du tableau
        self.quickSort(nuts, bolts, 0, n - 1)


    def quickSort(self, nuts, bolts, low, high):


        #condition pour arreter la récursivité
        if low < high:
            # on utilise le dernier element de bolts pour partitionner nuts, elle renvoie la position du pivot dans nuts
            pivot_index = self.partition(nuts, low, high, bolts[high])

            # Partitionner bolts autour du pivot de nuts
            self.partition(bolts, low, high, nuts[pivot_index])

            # récursivité sur les partitions gauche et droite

            self.quickSort(nuts, bolts, low, pivot_index - 1) # début jusqu'au pivot
            self.quickSort(nuts, bolts, pivot_index + 1, high) # a droite du pivot jusque la fin



    def partition(self, arr, low, high, pivot):
        # Trouver l'index où le pivot est dans arr
        pivot_index = arr.index(pivot)

        # Placer le pivot à la fin
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        left = low # on se mets au début

        # permets de placer correctement les elements en fonction du pivot
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1

        #left est l'index ou le premier element plus grand que le pivot se situe, on le place donc correctement car le pivot est à la fin de base
        arr[left], arr[high] = arr[high], arr[left]
        return left


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends