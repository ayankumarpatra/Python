# Write a program to find whether a given username contains less than 10 
# characters or not. 

username=input("Enter username : ")
length=len(username)

if (length<10):
    print ("Username contains less than 10 characters \n ")
else :
    print ("Username have more than 10 characters ")