class Solution:
    def reverse(self, stack):
        # Créé une copie de la pile
        aux_stack = stack[:]

        # nettoyer le stack
        while stack:
            delete = stack.pop()

        # ajouter a stack le auxiliere, ca sera dans l'ordre inverse ducoup
        while aux_stack:
            stack.append(aux_stack.pop())

# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        St = list(map(int, input().split()))
        ob = Solution()
        ob.reverse(St)
        print(*St)
