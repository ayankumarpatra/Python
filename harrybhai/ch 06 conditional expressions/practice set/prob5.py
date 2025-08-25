# Write a program which finds out whether a given name is present in a list or not. 

name_list=["harry",'rahul','dv']
name=input("Enter the name : ").lower()

if (name in name_list):
    print ("name is in the list ")
else :
    print ("name is not in the list ")

'''
also we can try to do like

in case the list contain mix capitalization names like Rahul,HArry

 name = input("Enter the name: ").lower()

# Create a lowercased version of name_list
lower_list = [n.lower() for n in name_list]

if name in lower_list:
    print("✅ Name is in the list.")
else:
    print("❌ Name is not in the list.")

'''