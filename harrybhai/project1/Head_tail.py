'''
1 for head 
0 for tail
'''
import random
compuer=random.choice([1,0])
you=int(input("0. for head \n1.for tail \nEnter your choice "))

if compuer==you:
    print("\nCongratulations you win :) ")
else :
    print("\nSorry ! you lost ")
