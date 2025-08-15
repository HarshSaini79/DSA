# Problem Statement:
# Given two sorted arrays nums1 and nums2, merge them into a single sorted array.

def merge_sort_array(nums1 , nums2):
    i , j = 0,0                     #initially indexed of both arrays are set 0
    merged = []                     #intial empty list
    while i< len(nums1) and j< len(nums2):       #while loop for iteration 
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])              #add nums1 (el) in empty list 
            i +=1
        else:
            merged.append(nums2[j])              #or add nums2 (el) in empty list
            j +=1
    
    merged.extend(nums1[i:])                     #if any of element is left add the remaining element in list
    merged.extend(nums2[j:])
    return merged
    
#Exapmle check:

print(merge_sort_array([1,2,4,8,10,11],[5,6,7,9,12]))
print(merge_sort_array([1, 3, 5], [2, 4, 6]))