
from typing import List
from collections import deque


class Solution:
    def rearrangeQueue(self, N: int, q: List[int]) -> List[int]:
        dq = deque(q)
        second = deque()  # Initialize second deque
        rearranged = []
        
        # Dequeue and enqueue the first half of elements to second deque
        for i in range(N // 2):
            second.append(dq.popleft())

        # Interleave elements from dq and second deques
        while dq:
            rearranged.append(second.popleft())
            rearranged.append(dq.popleft())

        
        return rearranged


#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        q=IntArray().Input(N)
        
        obj = Solution()
        res = obj.rearrangeQueue(N, q)
        
        IntArray().Print(res)
        

# } Driver Code Ends