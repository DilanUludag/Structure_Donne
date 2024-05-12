'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        total_petrol = 0
        total_distance = 0
        start_index = 0
        current_petrol = 0

        for i in range(n):
            petrol, distance = lis[i]
            total_petrol += petrol
            total_distance += distance
            current_petrol += petrol - distance

            # If current petrol becomes negative, it means starting from
            # the current petrol pump, the truck cannot reach the next one.
            # Therefore, we update the start index to the next pump.
            if current_petrol < 0:
                start_index = i + 1
                current_petrol = 0

        # If total petrol is less than total distance, it's impossible
        # to complete the circle. Otherwise, return the start index.
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