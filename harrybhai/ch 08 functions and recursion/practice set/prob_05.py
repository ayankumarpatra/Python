''' 
5. Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3 
6. Write a python function which converts inches to cms. 
7. Write a python function to remove a given word from a list ad strip it at the same 
time. 
8. Write a python function to print multiplication table of a given number.
'''

def starprinter (line_numbers):
    temp= int (line_numbers)
    for i in range (1,temp+1):
        ln=i
        while (ln>0):
            print ("*",end="")
            ln-=1
        print("")



num= int (input ("Enter the number of lines : "))
starprinter(num)