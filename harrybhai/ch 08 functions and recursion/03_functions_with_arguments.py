'''

'''
def greet_user (name):
    print (f"Hello user \nWelcome {name}")
    # also we can concatinate the strings like 
    print ("Hello"+name)

name =(input ("Enter the name : "))
greet_user(name)

'''
also wew can pass multiple arguments by comma , 
'''
def entry (name , time):
    print (f"{name} Entered at {time} hrs")

time = input ("Enter the time in 24 hrs foramt ")

entry(name,time)

