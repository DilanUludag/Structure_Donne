#User function Template for python3
class Solution:

    def count(self,arr, n, x):
        time = 0
        for number in arr:
            if (number == x):
                time += 1
        return time

if __name__ == '__main__':
        ob = Solution()
        ans = ob.count([3,2,1,1,1,1], 7, 1)
        print(ans)

# } Driver Code Ends