'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):

        # initialisation des données
        total_petrol = 0
        total_distance = 0
        start_index = 0
        current_petrol = 0

        #boucle sur le nombre de station
        for i in range(n):
            petrol, distance = lis[i] #prends l'essence disponible et la distance jusqu"au prochain
            total_petrol += petrol
            total_distance += distance
            current_petrol += petrol - distance

            # Si le current_petrol est négatif c'est a dire qu'on peut pas démarrer de la. On augmente l'indexe
            if current_petrol < 0:
                start_index = i + 1
                current_petrol = 0

        # si total essence est plus petit que la distance total alors impossible. sinon on retourne juste le start_index
        return start_index if total_petrol >= total_distance else -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends