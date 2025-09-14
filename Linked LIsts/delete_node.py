#Program : ask a user to delete a node and then delete a node while traversing the tree
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

choice = int(input("enter the node you want to delete :")) 
if choice == 1:
    node1 = deleteSpecificNode(node1, node1)
elif choice == 2:
    node1 = deleteSpecificNode(node1, node2)
elif choice == 3:
    node1 = deleteSpecificNode(node1, node3)
elif choice == 4:
    node1 = deleteSpecificNode(node1, node4)
elif choice == 5:
    node1 = deleteSpecificNode(node1, node5)
    
print("\nAfter deletion:")
traverseAndPrint(node1)