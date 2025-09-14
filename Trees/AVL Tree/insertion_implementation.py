class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1
def getheight(node):
    if not node:
        return 0
    return node.height

def getbalance(node):
    if not node:
        return 0
    return getheight(node.left) - getheight(node.right)

def rightrotate(y):
    print('rotate right on node: ', y.data)
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 +max(getheight(y.left),getheight(y.right))
    x.height = 1 +max(getheight(x.left),getheight(x.right))
    return x

def leftrotate(x):
    print('rotate left on node: ',x.data)
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1+ max(getheight(x.left), getheight(x.right))
    y.height = 1+ max(getheight(y.left), getheight(y.right))  
    return y

def insert(node , data):
    if not node:
        return TreeNode(data)
        
    #normal binary tree insertion
    if data < node.data:
        node.left = insert(node.left , data)
    elif data > node.data:
        node.right = insert(node.right, data)

    #updating the balance factor and  balance the tree
    node.height = 1+ max(getheight(node.left),getheight(node.right))
    balance = getbalance(node)
    
    #balancing the tree:
    #1.left left
    if balance > 1 and getbalance(node.left) >= 0:
        return rightrotate(node)
    #2. left right
    if balance > 1 and getbalance(node.left) < 0:
        node.left = leftrotate(node.left)
        return rightrotate(node)
    #3. right right
    if balance <-1 and getbalance(node.right) <=0 :
        return leftrotate(node)
    #4. right left
    if balance <-1 and getbalance(node.right) > 0:
        node.right = rightrotate(node.right)
        return leftrotate(node)

    return node
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=", ")
    inOrderTraversal(node.right)

root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
    root = insert(root, letter)
inOrderTraversal(root)
