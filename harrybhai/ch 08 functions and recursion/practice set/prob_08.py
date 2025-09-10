# a func to print multiplication of a given number 


def tab1to10(num):
    for i in range (1,11):
        print(f"{i}*{num} = {i*num}")

n=int(input("Enter the number you want to get the table "))

tab1to10(n)