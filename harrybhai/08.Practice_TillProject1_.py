'''
friends=[]

for i in range (5):
    name=input("Enter the name: ")
    friends.append(name)

print(friends)


Write a python program to add two numbers.


a=int(input("Enter value 1 : "))
b=int(input("Enter value 2 : "))

print("Sum is : ",a+b)


2. Write a python program to find remainder when a number is divided by z.
a=int(input("Enter Main Number : "))
b=int(input("Enter Number to devide with: "))

print("Remainder will be : ",a%b)

3. Check the type of variable assigned using input () function.
'''


'''

strings 


str="Hello world"

print(len(str))
print(str.endswith('d'))
print(str.startswith('5'))
print(str.count('l'))
print('hello\' world')

list 

random=[]

random.append('good but')
random.append('\ncan be done better\n')
print(random)

print(random[0].strip(),random[1])


Write a python program to display a user entered name followed by Good
Afternoon using input () function.


name = input("Enter the name : ")

print(f"Good morning {name}, Have a great day ahead")


Write a program to fill in a letter template given below with name and date.
letter =
Dear <|Name|>,
You are selected!
<|Date|>



def Selection_Letter(name):
    print(f"""Dear {name},
                We are pleased to inform you that 
                You Are Selected :) you did it ! """)
name = input("Enter the name : ")
Selection_Letter(name)


dict 
'''
marks={
    "Ayan":87,
    "Raj":82,
}

print(marks["Ayan"])