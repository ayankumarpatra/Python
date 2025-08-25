'''
7. Write a program to print the following star pattern. 
  * 
 *** 
***** like this , eg this is for n = 3 
'''
num= int (input ("Enter the number of lines : "))

for i in range (1,num+1):
    sp = num-i
    while (sp>0):
        print(" ",end="")
        sp-=1
    stars=2*i-1
    while (stars>0):
        print("*",end="")
        stars-=1
    print("\n",end="")
    

# or we may do by for loop (better)

for i in range (1,num+1):
    print(" "*(num-i),end="")
    print("*"*(2*i-1),end="")
    print("")
