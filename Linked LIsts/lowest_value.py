#problem : find the lowest valu in linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#function to define lowest value while traversing
def Lowest_value(head):       
    minValue = head.data 
    currentnode = head.next
    while currentnode:
        if currentnode.data < minValue:
            minValue = currentnode.data
        currentnode = currentnode.next
    return minValue

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print("the lowest value in the linked list :", Lowest_value(node1))
