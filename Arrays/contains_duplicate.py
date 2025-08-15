"""if an array Contains duplicate element
Given an integer array nums, 
determine if any value appears at least twice in the array. Return True if any duplicate exists, otherwise False."""
def CD(nums):
    return len(nums) != len(set(nums)). #set(nums) this function reduces the length coz it removes duplicate 
                                         #if original length and len set(nums) is equal then there is no duplicate
print(CD([1,2,3,4,5]))
print(CD([12,4,5,6,8,3,4,5]))
