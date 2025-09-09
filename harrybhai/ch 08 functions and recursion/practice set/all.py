'''

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



def celtofah(far):
    cel=(5/9)*(far-32)
    print(f"corresponding farhenheit temperature will be {cel}")

ftemp=int(input("Enter thr farhenheit temperature : "))
celtofah(ftemp)



3. How do you prevent a python print() function to print a new line at the end.

print("Hello world",end=" ")
print("Hello world",end=" ")


4. Write a recursive function to calculate the sum of first n natural numbers.



def sumofn(n):
    sum=0
    for i in range (1,n+1):
        sum+=i
        i=i+1
    return sum

n=int(input("Enter the number till want you want sum : "))

sv=sumofn(n)

print(f"Sum will be {sv}")



5. Write a python function to print first n lines of the following pattern:
***
**
*


def pattern(n):
    for i in range (n,1,-1):
        temp=i
        while(temp>0):
            print("* ",end="")
            temp-=1
        print(" ")

num=int(input("Enter the number of rows : "))

pattern(num)



6. Write a python function which converts inches to cms.

'''

inc = float(input("Enter the length in inches "))

print("Entered length in cm will be  :  ",inc*1.0*2.54)