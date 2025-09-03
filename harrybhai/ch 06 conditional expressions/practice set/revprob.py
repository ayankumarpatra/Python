'''
1.Write a program to find the greatest of four numbers entered by the user.
2. Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
4. Write a program to find whether a given username contains less than 10
characters or not.
5. Write a program which finds out whether a given name is present in a list or not.
6. Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
7. Write a program to find out whether a given post is talking about “Harry” or not.


# greatest of 4 num

greatest=0

nums=[]

for i in range (0,4):
    TempNum=int(input(f"Enter the {i+1} number : "))
    # if (TempNum<0):
    #     print("-ve numbers detected , but program can handle it , no problem")
    nums.append(TempNum)
    if (TempNum>greatest):
        greatest=TempNum

# for i in range (4):
#     if (nums[i]>greatest):
#         greatest=nums[i]
print(f"Greatest number is {greatest}")



#student pass

 Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.
'''
tries=0
Marks=[]

for i in range (0,3):
    if (tries==3):
        print("Maximum retry limit reached , please try again after sometime ")
        break
    tempnum=int(input("Enter marks for subject ",i+1," : "))
    if(tempnum<0 or tempnum>100):
        print("Invalid marks entered \nIf you wish to retry, type yes, else to exit, type any key : ")
        choice=input()
        if(choice.lower()=="yes"):
