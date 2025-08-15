"""
Program:
Count vowels and consonants in a string."""

def Count_vowels_consonant(Str):
    vowels = "aeiouAEIOU"             # defining vowels 
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"        # defining consonants 
    vowel_count = 0           #counting vowels (initially zero)
    consonants_count = 0      #counting vowels (initially zero)
    for i in Str:
        if i in vowels:         #condition if i matches vowels 
            vowel_count +=1
        if i in consonants:     #condition if i matches consonants
            consonants_count += 1
    return f"no of consonants are : {consonants_count} \nno of vowels are : {vowel_count}\n"

print(Count_vowels_consonant("harsh saini"))  
print(Count_vowels_consonant("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))      