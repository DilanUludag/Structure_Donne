#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''


class Solution:


    # fonction pour fusionner deux chaines listés
    def merge(self, left, right):
        dummy = LinkedList()
        curr = dummy


        #tant que ya une file de gauche et droite
        while left and right:
            if left.data < right.data:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        curr.next = left or right
        return dummy.next



    # Fonction pour split en deux parties
    def split(self, head):
        #on retourne le head si c'est vide ou si on est a la fin on retourne la tete
        if not head or not head.next:
            return head

        # on prend un premier noeud
        slow = head

        # on prend le noeud suivant
        fast = head.next

        # tant que FAST et le noeuds d'apres n'est pas vide
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # ca ressort d'office la moitié
        mid = slow.next
        slow.next = None #sert a stoper la liste pour séparer vraiment la liste en 2

        #retourne le millieu
        return mid




    # fonction principal pour faire le merge sort
    def mergeSort(self, head):
        # si c'est la fin de la liste ou si il n'y a pas de head alors on retourne le head qu'on a recu
        if not head or not head.next:
            return head

        # on fait appel à la fonction self.split qui retourne le noeud qui sépare en deux la liste
        mid = self.split(head)


        # on separe la liste de gauche en deux encore
        left = self.mergeSort(head)

        # on separe la liste de droite encore a deux
        right = self.mergeSort(mid)

        # on retourne le resultat de la fusion droite et gauche qui sera une chaine listée
        return self.merge(left, right)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node #CA DIT A LANCIEN NOEUF DE METTRE UN POINTEUR VERS LE NVX NOEUDS QUI EST LE DERNIER DUCOUP
        self.tail = new_node # AJOUT DU NOUVEAUX NOEUD COMME DERNIER

# prints the elements of linked list starting with head
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
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends