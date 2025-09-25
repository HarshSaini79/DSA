"""Merge Sort is a divide-and-conquer sorting algorithm that recursively splits the array into halves,
sorts each half until there is no sub array left (only a single element left in each array), 
and then merges them back together in order. 
It guarantees a time complexity of O(n log n) and is a stable sorting method."""
def mergeSort(arr):
    if len(arr) <= 1:     #checking if array is not empty or have only one value.
        return arr

    mid = len(arr) // 2    #dividng the array
    leftHalf = arr[:mid]   #the concept of slicing is used here
    rightHalf = arr[mid:]   

    sortedLeft = mergeSort(leftHalf)    #here recursion is used to create more sub arrays of left side
    sortedRight = mergeSort(rightHalf)  #again recursion is used to create sub array of right side

    return merge(sortedLeft, sortedRight)      #calling the merge function here

def merge(left, right):               #a function to merge the left ands right sub array with sequence
    result = []                       #empty array
    i = j = 0                         #left and right sub - array index set to 0 

    while i < len(left) and j < len(right):        #checking which sub array element is smaller 
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])        
    result.extend(right[j:])

    return result

my_array = [15,89,23,44,21,13,17,26,98,76,57,48,34,46,93]
sortedArr = mergeSort(my_array)
print("Sorted array:", sortedArr)