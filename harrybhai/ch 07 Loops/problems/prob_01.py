'''
1. Write a program to print multiplication table of a given number using for loop. 

'''

num=int (input ("Enter the number : "))
print (f"Heres the multiplication table of {num}")
for i in range (1,11) :
    print (f"{num}*{i}={num*i}")