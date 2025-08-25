'''
6. Write a program to calculate the factorial of a given number using for loop. 
'''
num= int (input ("Enter the number : "))
if (num>0):
    factorialvalue=1
    for i in range (1,(num+1)):
     factorialvalue*=i
    print(f"Factorial value of {num} is {factorialvalue}")
elif(num==0):
   print(f"Factorial value of {num} is 0 ")
else :
   print(f"Sorry Factorial value of {num} cant be calculated")