"""The Linear Search algorithm searches through an array and returns the index of the value it searches for.
The time complexity for linear search is O(n)"""

def linear_search(array,n):
    for index, value in enumerate(array):    #using enumerate to get both index and value
        if value == n:
            print("found at index: ",index)
            return 
    print( "not found in array")

print("This the array : [11,22,33,44,55,66,77,88,99,111]")
array = [11,22,33,44,55,66,77,88,99,111]
n = int(input("enter the number to search :"))
linear_search(array,n)