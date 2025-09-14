#wap for traversal of a singly linked list

class Node:         #a class with parameter data
    def __init__(self,data):
        self.data = data
        self.next = None


def Traverse_and_print(head):       #a function for traversing linked list
    currentnode = head
    while currentnode:
        print(currentnode.data , end ="->")
        currentnode = currentnode.next
    print("Null")

#values of each node with a class data
node1 = Node(7)            
node2 = Node(11)
node3 = Node(8)
node4 = Node(9)
node5 = Node(12)

#setting the next node
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

Traverse_and_print(node1)