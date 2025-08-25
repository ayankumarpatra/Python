''' 
6. Write a python function which converts inches to cms. 
7. Write a python function to remove a given word from a list ad strip it at the same 
time. 
8. Write a python function to print multiplication table of a given number.
'''
def cmtoinch(length):
    z=float(length)
    value=z*2.54
    return value


length=float(input("Enter length in inch: "))
inchvalue=cmtoinch(length)

print(f"{length} inch is equal to {inchvalue} cm")