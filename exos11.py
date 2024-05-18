# User function Template for python3
class Solution:
    
    def matchPairs(self, nuts, bolts, n):
        # Predefined order
        order = ['!', '#', '$', '%', '&', '*', '@', '^', '~']
        
        # Dictionary to store the position of each character in the predefined order
        order_dict = {ch: i for i, ch in enumerate(order)}
        
        # Sort both nuts and bolts according to the predefined order
        nuts.sort(key=lambda x: order_dict[x])
        bolts.sort(key=lambda x: order_dict[x])

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