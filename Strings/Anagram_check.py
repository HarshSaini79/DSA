"""
Program :
Check whether a string is Anagram or not , also take input from user
An "Check Anagram" refers to the process of determining whether two strings are anagrams of each other.
Two strings are considered anagrams if they contain the same characters with the same frequencies,
but possibly in a different order."""

from collections import Counter  # for character frequency counting

def Anagram_check(Str1, Str2):

    if len(Str1) != len(Str2):  # check length
        return "Not a Anagram"

    else:
        if Counter(Str1) == Counter(Str2):  # compare character counts
            return "Yes it is an Anagram"
        else:
            return "Not a Anagram"

str1 = str(input("enter your 1st string: "))
str2 = str(input("enter your 2st string: "))
print(Anagram_check(str1,str2))

