'''
* * * 
*   *   for n = 3 
* * * 

structure like , start and end lines with no of stars , remaing , only with stars at start and end position 
'''
num= int (input ("Enter the number of lines : "))
for i in range (1,num+1):
    if (i==1):
        print("* "*num,end="")
    if (i>1 and i<num):
        print("* ",end="")# to print fist * after the 1 st line 
        space=num-2
        print ("  "*space,end="")# to print mid spaces 
        print("* ",end="") # to print * at the last , num pos
    if (i==num):
        print("* "*num,end="")
    print ("")# didnt modify end as defaulr \n worked 
'''
efficient way 

for i in range(1, num + 1):
    if i == 1 or i == num:
        print("* " * num, end="")
    else:
        print("* " + "  " * (num - 2) + "* ", end="")  # one print for middle row
    print()

'''