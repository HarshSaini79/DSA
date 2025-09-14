#DFS  pre-order traversal : it is called pre-order because root is visited before left and right node(NLR)
class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end ="-->")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

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
preOrderTraversal(root)