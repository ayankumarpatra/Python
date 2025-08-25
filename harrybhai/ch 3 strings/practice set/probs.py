# 1. Write a python program to display a user entered name followed by Good 
# Afternoon using input () function.
 
name=input("Enter name : ") 
print ("Good Afternoon",name)#no space given after ..noon as , will automatically give a space 

'''
fstring mark in python 
like to print name directly inside string 
print(f"Good Afternoon {name}")
give the vaiable name insidde {} and mention f before the string 

'''

# 2. Write a program to fill in a letter template given below with name and date. 
# letter Format 
# '''  
# Dear <|Name|>, 
# You are selected! 
# <|Date|> 
# ''' 

namel=input("Enter name for the letter : ")
date=input("Enter date in dd/mm/yyyy or ddd.mm.yyyy format : ")
# print("Dear<|",namel,"|>,\nYou are selected! \n<|",date,"|>")
letter="Dear <|Name|>,\n You are selected! \n<|Date|>"

#print(f"Dear <|{namel}|>,\nYou are selected!\n<|{date}|>")
#The f"" is called an f-string and is used to insert variables directly inside a string.

# also you can use . replace chanining 

print (letter.replace("Name","Ayan kumar Patra").replace("Date","On 3.5.2027 at Microsoft"))

# or we can use direct variables also like 

print (letter.replace("Name",namel).replace("Date",date))

# 3. Write a program to detect double space in a string. 

str=input("Enter the string : ")
index=str.find("  ")
if (index!=-1):
    print ("Double space is present at index ",index)
else :
    print("Double space isnt present\n")

# from c idea i tried if else , but dont know , compiler only warned to use : in if but code runs , 
# so i added : , but please check if i written anything more wrong 

# 4. Replace the double space from problem 3 with single spaces. 

str1=input("Enter the string : ")
newstr=str1.replace("  "," ")
print (newstr)

# just modified last q , only replaced "  " double space by " "single space


"""
    jusst a ultra important point , strings are immutable , 
    even after using the functions , replace etc , its only cchanging for printing only 
    main string remains as it is 

    like double space one , main string still contains the double space , but in print only we changed 
    double space to single .

"""

# 5. Write a program to format the following letter using escape sequence characters. 
# letter = "Dear Harry, this python course is nice. Thanks!" 

print ("Dear Harry,\nthis python course is nice.\nThanks!")

# i know about the escaape seq like \n for newline or \t for tab space etc , or // to print /
# but not sure actually what we have to do here 