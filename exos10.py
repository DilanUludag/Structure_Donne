class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Base case: If stack is empty or has only one element, it is already sorted
        if len(s) <= 1:
            return
        
        # Remove the top element
        top_element = s.pop()
        
        # Recursively sort the remaining stack
        self.Sorted(s)
        
        # Insert the popped element back in the sorted stack
        self.insert_sorted(s, top_element)
    
    def insert_sorted(self, stack, element):
        # If the stack is empty or the element is greater than the top element, push the element
        if not stack or element > stack[-1]:
            stack.append(element)
        else:
            # Remove the top element
            top_element = stack.pop()
            
            # Recursively call insert_sorted to place the element
            self.insert_sorted(stack, element)
            
            # Put back the top element
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
