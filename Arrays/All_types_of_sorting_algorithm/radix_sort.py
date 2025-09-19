"""Radix Sort is a non-comparison based sorting algorithm that processes numbers digit by digit,
starting from the least significant digit (LSD) to the most significant digit (MSD).
It uses a stable sorting technique (like counting sort) at each digit position,
making it efficient for large numbers. 
Its time complexity is O(n·k), where k is the number of digits."""

my_array = [11,2,3,66,77,898,720,123,158,432,234,567,23,43,56] 
print("\nOriginal array: ",my_array) #first showing original array
radixArray = [[],[],[],[],[],[],[],[],[],[],] #A 2D array works as bucket for sorting
maxVal = max(my_array). #accessing and storing the maximum value of array
exp = 1     #exponent function to access every element digit by digit

while maxVal // exp >0:    #works until max value is greater than 0
    
    while len(my_array)>0:        #works until the last element of array
        val = my_array.pop()       #pops and store array element in val variable
        radix_index = (val//exp)%10  #deciding index of bucket
        radixArray[radix_index].append(val)      #adding element in bucket at bucket index

    for bucket in radixArray:             #loop to store bucket elment again in array
        while len(bucket) > 0:   
            val = bucket.pop()           #pops value from bucket 
            my_array.append(val)             #stores sorted value again in bucket
    
    exp *=10                #after every loop exp * by 10 means more digits for ex: exp=1(1 digit), exp*10 =10(2digit)

print("\nSorted array:",my_array)