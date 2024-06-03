#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:

    def insertionSort(self, head):
        #si ya pas de queue ou si on est a la fin
        if not head or not head.next:
            return head

        dummy = Node(0)  # Création d'un nœud fictif pour faciliter les insertions
        dummy.next = head #on a donc 0 --> Head --> ...

        curr = head  # Pointeur pour traverser la liste

        while curr and curr.next: # tant qu'on est pas à la fin de la liste
            if curr.data > curr.next.data: #si la valeur actuel est plus grande que la valeure suivant alors ca veut dire qu'on doit le faire avancer dans la liste
                prev = dummy  #prev initialisé au début de la liste (0)

                while prev.next.data < curr.next.data: # tant que la valeur suivante est plus petite que la valeur de curr.next
                    prev = prev.next # ca veut dire on est pas au bon emplacement pour le placer donc on avance le prev


                #insertion de la donnée
                temp = curr.next #selectionne la donnée qu'on veut replacer
                curr.next = curr.next.next #on coupe cette donné
                #on regroupe la file
                temp.next = prev.next
                prev.next = temp




            else: #ca veut dire que curr est bien placé donc on avance dans la liste
                curr = curr.next

        return dummy.next #.next car la liste commence par le noeud 0




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