# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner. 

marks=[] 
a= input ("Enter the marks : ")
marks.append (a)
b= input ("Enter the marks : ")
marks.append (b)
a= input ("Enter the marks : ")
marks.append (a)
b= input ("Enter the marks : ")
marks.append (b)
a= input ("Enter the marks : ")
marks.append (a)
a= input ("Enter the marks : ")
marks.append (a)
b= input ("Enter the marks : ")
marks.append (b)
marks.sort()
'''
you may see that the sort function is sorting the string , actually it works on the basis of ascii value 
so after sorting you still can look good or you may manually covert it to integer aafter the input was given like
a=int(input("Enter the marks: "))
it will convert the input to integer and done , perfect sorting 

and also note as we didnt make the value a integer , so the o/p is like 

 ['2', '3', '4', '5', '6', '7', '8'] 

 see a ' ' , single quote is there , as even its number , still the input is taken and stored 
 as a string .. 

but if you change it to integer then o/p will be like 
Sorted Marks are  [2, 4, 5, 5, 8, 9, 10]

means see no single quote , mean they are integer , you can add them or do any operations too if need 
but if they were taken as string , it will not possible 

'''
print ("Sored marks are ",marks)