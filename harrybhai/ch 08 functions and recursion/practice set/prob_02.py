'''
2. Write a python program using function to convert Celsius to Fahrenheit. 
3. How do you prevent a python print() function to print a new line at the end. 
4. Write a recursive function to calculate the sum of first n natural numbers. 
5. Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3 
6. Write a python function which converts inches to cms. 
7. Write a python function to remove a given word from a list ad strip it at the same 
time. 
8. Write a python function to print multiplication table of a given number.
'''
def farheheit_converter (temperature):
    #c/5=(f-32)/9
    f=(temperature*9/5)+(32)
    return f

temperature = float (input ("Enter the temperature : "))

farnheit_temperature = farheheit_converter(temperature)

print (f"{temperature} celcious in farhenheit will be {round(farnheit_temperature,2)}")

#round (float name , upto decimal you need to round it)
#round(farnheit_temperature,2)
# you can use it in fstrings also 
#print (f"{temperature} celcious in farhenheit will be {round(farnheit_temperature,2)}")
