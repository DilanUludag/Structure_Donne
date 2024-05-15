class Solution:
    def reverse(self, stack):
        # Create a copy of the original stack
        aux_stack = stack[:]

        # Transfer all elements from the original stack to the auxiliary stack
        while stack:
            delete = stack.pop()

        # Transfer all elements from the auxiliary stack back to the original stack
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
