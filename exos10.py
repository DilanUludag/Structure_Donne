class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack


    def Sorted(self, s):
        # Si il y a que 1 element ou aucun alors on renvoie
        if len(s) <= 1:
            return
        
        # enleve le top element
        top_element = s.pop()
        
        # on re-appel la fonction jusque quand il restera 1 element
        self.Sorted(s)

        # ajoute l'élément dans la pile via la fonction qui remets dans l'ordre, il y a 1 element dans la pile toujours
        self.insert_sorted(s, top_element)
    
    def insert_sorted(self, stack, element):
        # Si c'est vide ou bien si l'element à ajouter est plus grand que le dernier de la pile alors l'ajouter a la pile
        if not stack or element > stack[-1]:
            stack.append(element)

        else: #si c'est plus petit que le dernier element

            # On enleve le top
            top_element = stack.pop()
            
            # on re appelle jusque quand il reste 1 ou que l'element est plus grand que le dernier
            self.insert_sorted(stack, element)
            
            # on re-ajoute à la pile ce qu'on avait enelevé
            stack.append(top_element)

# Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.Sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()
# Driver Code Ends
