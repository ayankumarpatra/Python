marks ={
    "harry": 100,
    "subham": 56,
    "Rohan": 54,
    # not only by strings , we can make keys by integers too like
    0:"Acer",
    1:"samsung",
}

# .items()  list all items in the directory syntax dictname.items()

print (marks.items())
'''
o/p will be like dict_items([('harry', 100), ('subham', 56), ('Rohan', 54), (0, 'Acer'), (1, 'samsung')])

means each key and corresponding values will be returned as a tupple 
'''  

# .keys , only return the key values ,syntax dictname.keys()

print (marks.keys())
'''
o/p like dict_keys(['harry', 'subham', 'Rohan', 0, 1]) , only keys returned
'''

# .values , only return the key values ,syntax dictname.values()

print (marks.values())
'''
o/p like dict_values([100, 56, 54, 'Acer', 'samsung']) , only values returned

'''


# .update
'''
will update if any key is present , 
if the given key is not present , it will be added ..
'''

print ("BEfore update ",marks)
marks.update({ "harry":99,"Raunak":56})
# it will update harry value and add raunak 
print ("After update ",marks)

# .get , returns null if key not present , if key present , returns vlaue 

print (marks.get("harry"))
print (marks["harry"])
'''
here both will give same value 99 , but if the key not present , let harry 2 
print (marks.get("harry2"))  this will print none
print (marks["harry2"]) but this will throw an error 


.get(key)	Safe way to access a value. Returns None if key not found
.update()	Add or update one or more key value pairs
.pop(key)	Removes a key and returns its value
.items()	Returns all (key, value) pairs as tuples
.keys()	    Returns all keys in the dictionary
.values()	Returns all values in the dictionary
.clear()	Empties the whole dictionary
.copy() 	Makes a shallow copy of the dictionary
in operator	Example: "harry" in marks → checks if key exists (returns True)


you can get string length 
len (d)

will return dictionary key length , like if 3 keys , length will be 3 
'''

