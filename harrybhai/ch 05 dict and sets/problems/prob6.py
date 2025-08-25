'''
Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique. 
'''
d ={}

for i in range (4):
    name= input ("Enter the name of the friend : ")
    lang= input ("Enter the preffered language : ")
    d.update({name:lang})

print (d)

'''
If the names of 2 friends are same; what will happen to the program in problem 

as name is same means the key will be same , so when we will use d. update , the value assigned to the
key will be updated to the current one and previous value will be removed


If languages of two friends are same; what will happen to the program in problem
no problem in this case , values may be same , but key shouldnt be same 
'''