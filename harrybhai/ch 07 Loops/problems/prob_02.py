'''
Write a program to greet all the person names stored in a list ‘l’ and which starts 
with or contains S. 
l = ["Harry", "Soham", "Sachin", "Rahul"] 
'''
l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l :
    temp=i.lower()
    if ("s" in temp):
        print (f"Welcome {i}")
for i in l :
    if ((i.lower()).startswith("h")):
        print(f"Welcome {i}")