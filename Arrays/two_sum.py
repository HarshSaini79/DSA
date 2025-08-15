"""Given an array of integers nums and an integer target, return the indices of the two numbers
#such that their sum equals the target. You may assume each input has exactly one solution, 
and you may not use the same element twice."""

def twoSum(nums, target):
    num_map = {}                       # an empty dictionary which will store element and its index. 

    for i, num  in enumerate(nums):      #enumerate is the function which will give us the element and its indfex in a loop
        diff = target - num

        if diff in num_map:
            return [num_map[diff], i ]

        num_map[num] = i
    return  [], "not found"

#examples

print("Indexs are : ", twoSum([1,2,3,4,5], 9))
print("Indexs are : ", twoSum([15,16,24,8,10],40))
print("Indexs are : ", twoSum([10,10,5,8,10],30))