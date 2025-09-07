'''
3. How do you prevent a python print() function to print a new line at the end.
4. Write a recursive function to calculate the sum of first n natural numbers.
5. Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
6. Write a python function which converts inches to cms.
7. Write a python function to remove a given word from a list ad strip it at the same
time.
8. Write a python function to print multiplication table of a given number.




#1 Write a program using functions to find greatest of three numbers.

def Greatestofthree(a,b,c):
    if (a>b and a>c):
        print(f"{a} is greatest")
    if (b>a and b>c):
        print(f"{b} is greatest")
    if (c>a and c>b):
        print(f"{c} is greatest")

x,y,z=map(int,input("Enter thr 3 number seperated by space : ").split())

Greatestofthree(x,y,z)

2. Write a python program using function to convert Celsius to Fahrenheit.
'''

