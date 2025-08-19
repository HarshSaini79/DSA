#Problem given a array reverse its element

def reverse_array(arr):
    
    for i in arr:
       
        arr[:] = arr[::-i]
    
        return arr


ck = [1,2,3,4,5,6,7,8]
print(reverse_array(ck))