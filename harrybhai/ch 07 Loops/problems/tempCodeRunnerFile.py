'''
5. Write a program to find the sum of first n natural numbers using while loop. 

'''

num= int (input ("Enter the number : "))
print (f"The sum of natural numbers upto {num} is ")
adder =1
sum=0
while(adder<=num) :
   sum+=adder
   adder+=1
print (sum)
