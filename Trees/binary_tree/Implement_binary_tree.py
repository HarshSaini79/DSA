#binary tree is a type of tree which has only two childrens (left child and right child) 
class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Tree('13')
node7 = Tree('7')
node3 = Tree('3')
node8 = Tree('8')
node15 = Tree('15')
node14 = Tree('14')
node18 = Tree('18')
node19 = Tree('19')

root.left= node7
root.right= node14

node7.left= node8
node7.right= node3

node14.left= node15
node14.right= node18

node18.left = node19

#testing
print("lets access element 15 :",root.right.left.data)

#this tree is also a blanced binary tree since the atmost difference is 1
x