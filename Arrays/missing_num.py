# Problem Statement:
# Given an array containing n distinct numbers taken from the range 0 to n,
# find the one number that is missing from the array.

def missing_num(nums):
    n = max(nums)      #cheking till the max value of nums
    full_set = set(range(1, n +1))        #making a complete sequence
    nums_set = set(nums)                   # making existing incomplete sequence
    missing = [(full_set - nums_set)]      #diff between full and nums set to find out which elements are missing
    return sorted (missing)              #at end returning missing elements in sorted manner
    

print(missing_num([3, 0,1,5,8]))