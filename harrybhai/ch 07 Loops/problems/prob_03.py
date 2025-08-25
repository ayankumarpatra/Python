'''
Write a program to print multiplication table of a given number using wwhile loop now.
'''

num=int (input ("Enter the number : "))

multiplier =1
print (f"Here is the multiplication table of {num} : ")
while (multiplier<11):
    print(f"{num}*{multiplier}={num*multiplier}")
    multiplier+=1 