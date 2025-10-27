'''
string is a data type in python 

we can initialize string in 3 ways 

a ='harry'       
# Single quoted string 
b = "harry"      
# Double quoted string 
c = ' ''harry' ''  # Triple quoted string , ' or " is usually for single line string

the triple quote string is usually for multi line strings 


strings in python are immutable , means you cant change the string or its elements 

eg if 
name ="harry"
we cant change r or a with anything other 

if we wish to change we have to create another variable 
like 

'''
name ="Harry"

"""
inndexing is of 2 type , positive and negetive indexing 
Indexing is done like 
              name ="H  a  r  r  y" 
positive indexing    0  1  2  3  4
negetive indexing   -5 -4 -3 -2 -1

positive indexing starts with 0 and goes till the last 
negetive indexing starts with -1 and from the last and goes till first

"""

print("Length of string is : ",len(name))

shortname= name [0:3]
# syntax is stringname [startposition : till position ]
# start position is included in the new string but the end position will not so we mentioned it as till position 
# eg if we givw 0,3 , it will include elements feom index 0 , 1,2 but not 3 , till 3

print(shortname)

intname=name[2:4]
print (intname)

#positive we already done in c , now think if ask for -ve , like
print(name[-4:-1])

'''
in east wa-3 y just replace the values and remove -ve and print 
like -12 -7 then positions after replacing will be 7 to 12 


like here given -4 -1 
so will print from 1 to 4 , to for , not 4 , upto 3

like for Harry , 
1 , 2 , 3 arr will be printed 

some other questions ...
'''
# advanced slicing
print(name[:])#nothing given means start position and end position given eg here 0 , 5
print(name[:5])# start position not given means , start position 0 automatically taken 
print(name[0:])# End position not given means , end position length automatically taken 

# other slicing

numbers="0123456789"

print(numbers[1:5:2])

'''
numbers[1:5:2] 
first 1:5 it will slice the numbers string from 1 to till 5 , means 1,2,3,4

now the last 2 it will skip every 2nd iretion eg 1 taken , then 2nd pos , 2 skipped , 3 taken 4 removed
5 is out of bounds ...

'''

print(numbers[1:7:3])