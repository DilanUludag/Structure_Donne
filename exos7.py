
from typing import List
from collections import deque


class Solution:
    def rearrangeQueue(self, N: int, q: List[int]) -> List[int]:
        dq = deque(q) # on créé une queue de "q" qui est une liste de base de int
        firstpart = deque()  # On créé une autre liste d'attente vide
        rearranged = [] # c'est un tableau vide réarrangé
        
        # on divise dq en deux, la premiere moitié dans firstpart et l'autre reste la
        for i in range(N // 2):
            firstpart.append(dq.popleft())

        # on ajoute a réarranger d'abord un element de firstpart et puis de dq jusque quand dq soit vide
        while dq:
            rearranged.append(firstpart.popleft())
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