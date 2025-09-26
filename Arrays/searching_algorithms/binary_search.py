"""Binary Search is much faster than Linear Search, but requires a sorted array to work.
Time complexity of binary search is O(log2 n)"""

def Binary_search(arr,target):
        left = 0
        right=len(arr)-1
        while left <= right:
            mid= (left+right)//2
            if arr[mid] == target:
                return mid
            if arr[mid] <target:
                left = mid+1
            else:
                right = mid -1
        return -1
print("array = [1,2,3,4,5,6,7,8,9,10]")
array = [1,2,3,4,5,6,7,8,9,10]
target = int(input("enter your search : "))
result = Binary_search(array,target)

if result != -1:
    print(f"value {target},found at index: {result}")
else:
    print("Target not found in array.")
