#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution:
    # Function to merge two sorted doubly linked lists.
    def merge(self, left, right, order):
        if not left:
            return right
        if not right:
            return left

        if order == "asc":
            if left.data <= right.data:
                left.next = self.merge(left.next, right, order)
                left.next.prev = left
                left.prev = None
                return left
            else:
                right.next = self.merge(left, right.next, order)
                right.next.prev = right
                right.prev = None
                return right
        else:
            if left.data >= right.data:
                left.next = self.merge(left.next, right, order)
                left.next.prev = left
                left.prev = None
                return left
            else:
                right.next = self.merge(left, right.next, order)
                right.next.prev = right
                right.prev = None
                return right

    # Function to split the doubly linked list into two halves.
    def split(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None
        middle.prev = None

        return head, middle

    # Function to perform Merge Sort on doubly linked list.
    def sortDoubly(self, head, order="asc"):
        if not head or not head.next:
            return head

        left, right = self.split(head)
        left = self.sortDoubly(left, order)
        right = self.sortDoubly(right, order)

        return self.merge(left, right, order)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def printList(self, node):
        while (node.next is not None):
            node = node.next
        while node.prev is not None:
            node = node.prev
        while (node is not None):
            print(node.data, end=" ")
            node = node.next
        print()


def printList(node):
    temp = node

    while (node is not None):
        print(node.data, end=" ")
        temp = node
        node = node.next
    print()
    while (temp):
        print(temp.data, end=" ")
        temp = temp.prev


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        llist = DoublyLinkedList()
        for e in arr:
            llist.append(e)
        ob = Solution()
        llist.head = ob.sortDoubly(llist.head)
        printList(llist.head)
        print()

# } Driver Code Ends