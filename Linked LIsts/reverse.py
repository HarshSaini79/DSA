class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverese_linked_list(head):
    curr = head
    prev = None

    while curr is not None:
        nextnode= curr.next
        curr.next = prev

        prev = curr
        curr = nextnode
    return prev

def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)    
head = reverese_linked_list(head)
printList(head)
