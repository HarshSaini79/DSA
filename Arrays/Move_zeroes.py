"""Move Zeroes
Statement:
Given an integer array nums, move all 0's to the end of the array 
while maintaining the relative order of the non-zero elements"""

def MoveZeroes(nums):
    pos = 0           #it is a pointer for setting index of elements
    for num in nums:   
        if num !=0:
            nums[pos] = num #setting num at "pos " index 
            pos += 1 
    while pos< len(nums):   #if all the pos(index) is  not containg elements
        nums[pos] = 0      #then set the remaining pos as zero until all the indexes are covered
        pos+=1

    return nums


print(MoveZeroes([1,2,3,4,0,5]))
print(MoveZeroes([1,0,7,0,8,19,2,3,4,0,5]))
