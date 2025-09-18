"""Quicksort is a divide-and-conquer sorting algorithm that selects a pivot and partitions the array around it.
It is very fast on average case with O(n log n) time, works in-place with low memory usage, 
but can degrade to O(n²) in the worst case if pivots are chosen poorly."""

def partition(array,low,high):     #defining a function which will ensure correct pivot index 
    pivot = array[high]            #last element of array
    i = low -1                     #i = -1

    for j in range(low,high):     #loop from 0 to pivot_index-1
        if array[j] <= pivot:          #if element is smaller than pivot
            i +=1                      # increment 
            array[i],array[j] = array[j],array[i]  #swap element at i index and element of j index    
        array[i+1],array[high] = array[high], array[i+1] #brings pivot back to correct index
        return i+1         #returns the pivot index

def quicksort(array, low =0, high=None): #this function recursively divides the array into sub array and sorts them.
    if high is None:           
        high = len(array)-1               #high is defined here
    if low < high:
        pivot_index = partition(array,low,high)   #selecting pivot 
        quicksort(array,low,pivot_index-1)       #sorting left side of pivot by recursion 
        quicksort(array,pivot_index+1,high)      #sorting right side of pivot by recursion

#testing time
my_array = [64,34,25,12,22,11,90,5]
quicksort(my_array)
print("Sorted aray:" , my_array)