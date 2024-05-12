#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Solution:
    # Function to perform insertion sort on the linked list.
    def insertionSort(self, head):
        if not head or not head.next:
            return head

        dummy = LinkedList()  # Dummy node to handle the case where head needs to be updated
        dummy.next = head
        curr = head  # Pointer to traverse the list

        while curr and curr.next:
            # If the current node's value is greater than the next node's value, we need to insert it
            if curr.data > curr.next.data:
                # Initialize prev to the beginning of the list
                prev = dummy
                # Find the correct position to insert the current node
                while prev.next.data < curr.next.data:
                    prev = prev.next
                # Store the next node of the current node
                temp = curr.next
                # Update the next pointer of the current node to skip the next node
                curr.next = curr.next.next
                # Insert the current node after prev
                temp.next = prev.next
                prev.next = temp
            else:
                # If the current node is in order, move to the next node
                curr = curr.next

        return dummy.next

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
INF = float("inf")
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        a = Node(INF)
        nodes = list(map(int, input().strip().split()))
        ptr = a
        for x in nodes:
            ptr.next = Node(INF)
            ptr = ptr.next
            ptr.data = x
        a = a.next
        ob=Solution()
        head = ob.insertionSort(a)
        printList(head)
# } Driver Code Ends