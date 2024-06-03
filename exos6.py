#User function Template for python3

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
'''

class Solution:

    # Fonction principale
    def sortDoubly(self, head):
        if not head or not head.next:
            return head

        # sépare la liste en 2
        mid = self.split(head)

        # On le fait pour chaque moitié
        left = self.sortDoubly(head)
        right = self.sortDoubly(mid)

        # on fusionne les deux bouts
        return self.merge(left, right)

    # fonction qui sépare en deux bouts
    def split(self, head):
        fast = slow = head

        # pour trouver le milieu
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        #quand on est sorti de la boucle on a trouvé le milieu

        second = slow.next
        slow.next = None # pour couper le liste chainée
        if second:
            second.prev = None # pour couper egalement

        return second # on retourne la moitié

    # Pour fusionner

    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first

        # si a gauche est plus petit que a droite
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first

        # si a droite est plus petit que a gauche
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second




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