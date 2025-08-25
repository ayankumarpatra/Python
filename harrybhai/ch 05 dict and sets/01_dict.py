'''
marks are just like structures in the c language , it just provide some basic details 
associated with the key , but rememebrr , we cant get the value by indexing like 

arr[0] we get first element but here marks [0] will throw an error as here indexing here is 
donr by the name ( only here ), 
incase you done by 1 , 2 , then you can give marks[1] , it will print the corresponding details
associated with it 

like 
'''

marks ={
    "harry": 100,
    "subham": 56,
    "Rohan": 54,
}

print (marks["harry"])
# this will only print marks of harry , 100 here , not the name harry again 

'''
by nested listss we also can do similar kind of things , just like 
marks =[ ["Harry",100],]
first , marks is a list , then inside it harry and 100 is list .

now if we print marks[0] , it will print like 
['Harry', 100] 

properties of python dict 

1. its unordered , means order matter nehi karta
2. mutable , means modifiable , modify kiya ja sakta hai 
            also by key value you can add , remove or modify something 
3. indexed ,  means , just here , name list is harry ,subham ,rohan 
        so now if you give rohan , it will jump to rohan like switch case , 
        will not check each index like by if else .. like if harry , not rohan , go to next ...
        will not like that , will go to rohan directly 
4. cant contain duplicate key values 


to create an empty dictionary , just assign empty like
'''
d={}#empty dictionary