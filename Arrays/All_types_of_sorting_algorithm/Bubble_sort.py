"""Bubble sort algorithm sorts the array in ascending order and its time complexity is O(n^2)
it bubble ups the largest element at the end """

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(my_array)      #easy way to count the elements of array
for i in range(n-1):   #outer loop for controlling no of iterations of inner loop for array with n values it must run n-1 times
    swapped = False    #currently swap = false so that we can break the loop once the array is completed
    for j in range(n-i-1):    #inner loop for swapping elements of array, n-i-1 this codition ensure avoiding last element which are only sorted after first pass
        if my_array[j]>my_array[j+1]:      #checks if current element is greater than next element this condition wont run if array is sorted
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j] #swaps element
            swapped = True
    if not swapped:   #if not swap value becomes true then this loop will break    
        break

print("Sorted array : ", my_array)