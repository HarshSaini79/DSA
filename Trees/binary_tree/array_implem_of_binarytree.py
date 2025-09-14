# we will implement binary tree usong array
binary_tree_array = ['R','A','B','C','D','E','F',None,None,None,None,None,None,'G']

def left_child_index(index):
    return 2 * index +1

def right_child_index(index):
    return 2* index + 2

def get_data(index):
    if 0 <= index <len(binary_tree_array):
        return binary_tree_array[index]
    return None

root = binary_tree_array[0] #R

left_child = left_child_index(0) #A
left_child_of_left_child = left_child_index(left_child)#C
data2 = get_data(left_child_of_left_child)
right_child_of_left_child = right_child_index(left_child)#D
data3 = get_data(right_child_of_left_child)


right_child = right_child_index(0)#B
left_child_of_right_child = left_child_index(right_child) #E
data1 = get_data(left_child_of_right_child)
right_child_of_right_child = right_child_index(right_child)#F
data4 = get_data(right_child_of_right_child)
left_child_of_right_child_of_right_child = left_child_index(right_child_of_right_child)#G
data5 = get_data(left_child_of_right_child_of_right_child)

#test
print("root.right.left.data: ",data1)
print("root.left.left.data: ",data2)
print("root.left.right.data: ",data3)
print("root.right.right.data: ",data4)
print("root.left.right.data: ",data5)
