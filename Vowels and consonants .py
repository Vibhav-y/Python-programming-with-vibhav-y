#input a string fron the user
a=input("word: ").lower()

#create a list of vowels to be matched with
list_vowel=['a', 'e', 'i', 'e', 'o', 'u']

#Initialize the values of values and consonants
vowel=0
consonant=0

#in the for loop it checks if a letter in the string is a vovel or not by comparing it with the list
for letter in a:

    # If the letter is in the list it counts it as a vowel and adds 1 to the list of vowels
    if letter in list_vowel:
        vowel+=1

# if the letter is not in the list and is a space " " that is added by the user it will go to another letter
    if letter == " ":
        continue

# If the letter is not in the list in vowel and is also not a space " " it will be counted as a consonant
    elif letter not in list_vowel:
        consonant+=1

# now print the output
print("Vowels:",vowel)
print("Consonants:",consonant)
