'''  
4. Write a program to find whether a given username contains less than 10 
characters or not. 
5. Write a program which finds out whether a given name is present in a list or not. 
6. Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50        
=> F 
7. Write a program to find out whether a given post is talking about “Harry” or not. 
'''

# 1. Write a program to find the greatest of four numbers entered by the user.
i=1
n1=int (input (f"Enter number {i} : "))
i+=1
n2=int (input (f"Enter number {i} : "))
i+=1
n3=int (input (f"Enter number {i} : "))
i+=1
n4=int (input (f"Enter number {i} : "))



if (n1<n2):
    big1=n2
else :
    big1=n1
if (n3>n4):
    big2=n3
else :
    big2=n4
if (big1>big2):
    print (f"greatest number is {big1}")
else :
    print (f"greatest number is {big2}")


"""
also we can do like 

if (n1>n2 and n1>n3 and n1>n4) :
        print ("greatest number is : ",n1)
    ... similarly for n2 , n3 ,n4 
"""