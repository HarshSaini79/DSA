"""Insertion sort is a type of sorting algorithm which also sorts array in ascending order but it shifts value one by one,
it sorts array iteratively and its time complexity is also O(n^2)"""

my_array = [11,4,3,12,18,9,10,45,66]
n = len(my_array)
for i in range(1,n):   #loop from index 1 to n
    insert_index = i   #currently assuming the. insert position as i 
    current_value = my_array[i]  #storing element i in variable named as current value
    for j in range(i-1,-1,-1):   #this loop will work from right to left 
        if my_array[j]> current_value: 
            my_array[j+1] = my_array[j] #j and i both will become same element as j+1 index is = index of i
            insert_index = j  #now position to insert the element will be updated as j
        else:
            break
    my_array[insert_index]= current_value #here it will insert element i at position j if j is > than i

print("Sorted array: ", my_array)