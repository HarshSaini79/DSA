# Problem Statement:
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than n/2 times.

def Major_el(nums):
    count = 0             #initial count of appearance of element
    candidate = 0         # candidate for majority
    for el in nums:       
        if count == 0:
            candidate = el   #set candidate as element
        count += (1 if el == candidate else - 1)    #increase count if same number else decrease
    return candidate 

print("Major element : ", Major_el([3,2,3,2,3]))
