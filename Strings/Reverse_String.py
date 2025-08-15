#Prblem 
# Given a String , print the reverse of that string
# Example: hello -> olleh.

def reverse_str(Str):
    reverse = " "      #basic step of initializing empty string to store elements of original string
    for i in Str: 
        reverse = Str[::-1]     #string slicing
    return reverse

#Runing examples
string = "Harsh"
print(reverse_str(string))

surname = "Saini"
print(reverse_str(surname))