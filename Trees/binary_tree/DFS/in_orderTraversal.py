#DFS in-order traversal : it is called in-order because root is visited between left and right node(LNR)
class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end =" --> ")
    inOrderTraversal(node.right)

root = Tree('R')
nodeA = Tree('A')
nodeB = Tree('B')
nodeC = Tree('C')
nodeD = Tree('D')
nodeE = Tree('E')
nodeF = Tree('F')
nodeG = Tree('G')

root.left= nodeA
root.right= nodeB

nodeA.left= nodeC
nodeA.right= nodeD

nodeB.left= nodeE
nodeB.right= nodeF

nodeC.left = nodeG

#testing
inOrderTraversal(root)

