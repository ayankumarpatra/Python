s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')

print (s)
'''
output will be like {'20', 20} 

reason is very intresting , in python 20 and 20.0 is same not like c , 
as value same so it treats 20.0 and 20 as same 
'''


# prob 5 ,s = {} 
# What is the type of 's'? 
'''
even you get confused and declare s as a set , but remember to declare an empty set , you need to declare like 

s= set()

s={} creates an empty dictionary 
'''