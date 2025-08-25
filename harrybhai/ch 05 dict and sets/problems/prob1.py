'''
CHAPTER PRACTICE SET
1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up! create a dictionary with some keywords and 
their english meaning , user will input same word , snd get english meaning 
'''

wordset={
    "billi":"cat",
    "mera":"mine",
    "tera":"your"
}

str1=input("Enter the hindi word : ")
# print (wordset[str1])

# if str1 in wordset :
#     print (wordset[str1])
# else :
#     print("Sorry entered word isnt in dictionary")

print (wordset.get(str1,"Sorry entered word isnt in dictionary"))