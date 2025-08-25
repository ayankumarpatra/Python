'''
chapter q questions 

1. Write a python program to add two numbers. 
2. Write a python program to find remainder when a number is divided by another. 
3. Check the type of variable assigned using input () function. 
4. Use comparison operator to find out whether a given variable a is greater than 
    b or not. Take a = 34 and b = 80 
5. Write a python program to find an average of two numbers entered by the user. 
6. Write a python program to calculate the square of a number entered by the user.

'''
#1
a=int (input ("Enter the first number : "))
b=int (input ("Enter the second number : "))
print ("sum is : ",a+b)

#2
c=int (input ("Enter the first number : "))
d=int (input ("Enter the second number : "))
print ("Remainder is : ",c%d)

#3
'''
i think any input we take by the input function is string by default , we can change it by 
typecasting 
'''

#4
e =34
f =80
# already taken a and b so taken e , f
print ("a is greater than b is ",e>f)

'''
i remember if else in c , but dont know same condition in python , please let me know if something 
is like present in python also
'''

#5
g =int (input ("Enter the first number : "))
h =int (input ("Enter the second number : "))
print ("Average is ",((g+h)/2))

#6
i = int (input ("Enter the number : "))
print ("Sqare value is ",i**2)

'''
i remember pow in c , but dont know same condition in python , i know by a**b in be we can give anything
like i think we can calculate square root also by giving b =1/2 , please correct me if i am wrong 
 please let me know if something  is like present in python also
'''