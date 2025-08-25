'''
1. Write a program using functions to find greatest of three numbers. 

'''
def greatestofthree ( num1,num2,num3):
    if (num1 > num2 and num1 > num3 ):
        print (f"{num1} is greatest ")
    if (num2 > num1 and num2 > num3 ):
        print (f"{num2} is greatest ")
    if (num3 > num2 and num3 > num1 ):
        print (f"{num3} is greatest ")
num1= int (input ("Enter the first number : "))
num2= int (input ("Enter the 2 nd number : "))
num3= int (input ("Enter the 3 rd number : "))

if (num1!=num2 and num1!=num3 and num3!=num2):
    greatestofthree(num1,num2,num3)
else :
    print ("Equal numbers given , please give 3 distinct numbers")