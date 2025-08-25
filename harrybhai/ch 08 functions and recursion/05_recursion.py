# same as c idea 

def factorial (n):
    if (n==0 or n==1):
        return 1
    return n*factorial(n-1)

num= int (input ("Enter the number "))
if (num<0):
    print ("Invalid number to calculate factorial ")

else :
    factorial_value= factorial(num)
    print (f"Factorial value of {num} is {factorial_value}")