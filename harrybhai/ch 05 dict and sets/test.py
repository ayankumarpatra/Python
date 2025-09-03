'''


a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=a+b
print("Asdria Suuummmm is ",c)


1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up! create a dictionary with some keywords and 
their english meaning , user will input same word , snd get english meaning 




hntoen ={
    "cat":"billi",
    "mouse":"cuhiya",
    "banana":"kela"
}

word=input("Enter the word: ")

word=word.lower()

if word in hntoen :
    print("Hindi word of the entered word is ",hntoen[word])
else :
    print("Word isnt in dictionary")


print(hntoen.get(word,"Word isnt in dictionary"))



Write a program to input eight numbers from the user and display all the unique
numbers (once).

'''
st=set()

for i in range (7):
    st.update(int(input("Enter the number : ")))

print (st)
