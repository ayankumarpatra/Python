def goodbye (name,ending="Visit Again"):
    print(f"Thank you {name} \n{ending} ")

name =input("Enter name")

goodbye (name)
goodbye(name,"hello world")

# so now see if you only give name , it will print the default ending value but if you give any 
# other value , it will use the value instead 