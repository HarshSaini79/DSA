""" Problem :
 Check whether a string is palindrome or not.
 Palindrome means a string will be same in forward or backward spelling 
 example : "madam" , civic ,MOM , Level  """

def Palindrome(Str):
    reverse = Str[::-1 ]
    if reverse == Str:
        return f"Given string : {Str} ,is a Palindrome. " 
    else:
        return f"Given string : {Str} , is not a Palindrome."
    
#Code TEsting
word1 = "civic"
word2 = "madam"
word3 = "level"
word4 = "king"
word5 = "kill"
print(Palindrome(word1))
print(Palindrome(word2))
print(Palindrome(word3))
print(Palindrome(word4))
print(Palindrome(word5))