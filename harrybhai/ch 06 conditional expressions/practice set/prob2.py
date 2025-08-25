'''
2. Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks out of 100 as an input from the user. 
'''

i=1
n1=int (input (f"Enter marks for subject {i} out of 100: "))
i+=1
n2=int (input (f"Enter marks for subject {i} out of 100: "))
i+=1
n3=int (input (f"Enter marks for subject {i} out of 100: "))

if (n1<33 or n2<33 or n3<33 ):
    print ("Sorry you arent qualified ")
elif ((n1+n2+n3)/3 < 40):
    print ("Sorry you arent qualified ")
else : 
    print ("Qualified ")