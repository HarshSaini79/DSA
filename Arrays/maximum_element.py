#question find the maximum element in a given Array.

def findMax(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

#Run Example:
array = [10,20,40,50,70,81,91]
print("maximum element : " , findMax(array))