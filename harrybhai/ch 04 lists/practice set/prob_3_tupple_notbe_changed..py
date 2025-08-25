'''
3. Check that a tuple type cannot be changed in python. 
4. Write a program to sum a list with 4 numbers. 
5. Write a program to count the number of zeros in the following tuple: 
a = (7, 0, 8, 0, 0, 9) 
'''

a=("Hello",48,"World",84)
print ("First element is ",a[0])
print ("First 2 elemt is ",a[0:2])
a[0]="acer"
print ("Tple contents are ",a)
'''
First element is  Hello
First 2 elemt is  ('Hello', 48)
Traceback (most recent call last):
  File "d:\Code Playground\pithon\harrybhai\ch 04 lists\practice set\prob_3_tupple_notbe_changed..py", line 11, in <module>
    a[0]="acer"
    ~^^^
TypeError: 'tuple' object does not support item assignment

so while a[0], sucesfully printed first element 
but a[0]= something throw an error , so something cant be assigned to that place 

'''