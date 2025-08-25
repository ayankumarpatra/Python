'''
Write a program to input eight numbers from the user and display all the unique
numbers (once).
'''
"""
for i in range (9) :
    n=int(input("Enter the",i," th number")) 
    nums.add(n)
print (nums)

for loop is good , but error at input("Enter the", i, " th number")  ❌
as You're using input() with multiple arguments like in C-style printf():

also "Enter the " + i + " th number" fails because i is an integer, and you can't directly add (+) str + int.


other ways to correct do 

    n = int(input("Enter the " + str(i+1) + "th number: "))

    converted the i+1 as string , so it can concatinate 

or  n = int(input(f"Enter the {i+1}th number: "))  # f-string

convert it as f string , so {i} automatically denote to i

"""
nums= set ()
for i in range (9):
    n = int (input ("Enter the "+str(i+1)+" th number"))
    nums.add(n)
print(nums)