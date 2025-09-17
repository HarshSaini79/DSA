"""selection sort algorithm moves the lowest value of an array to the front its time complexity is also O(n^2)"""
my_array = [64,32, 34, 25, 5, 22, 11, 90, 12]
n = len(my_array)
for i in range(n):
    min_index = i    #currently first element is set to minimum
    for j in range (i+1,n):   #starts comparing from secod element
        if my_array[j] < my_array[min_index]:     #if second element is smaller than first element
            min_index= j      #changes min index
    my_array[i],my_array[min_index] = my_array[min_index], my_array[i]    #swaps min index with current index of array

print("Sorted array:", my_array)


