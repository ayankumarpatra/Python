randomlist=["hello","world",3.34,5,False]

# not syntax is name =[ add the datatypes as you wish ]
#access as like randomlist[1]or 2, .... 

# also note as you cant change the existing string , but you can change the list like array 
# eg randomlist [2]=("hello"), it will replace the 2nd position with hello 

print (randomlist)

# slicing is as like as strings ...
print (randomlist[:])
print (randomlist[:4])
print (randomlist[1:3])

"""
#nothing given means start position and end position given eg here 0 , 5 or 4 , dekh lena
# start position not given means , start position 0 automatically taken 
# End position not given means , end position length automatically taken 

"""

#append , add anything at last of the list 
# usually its recomeneded not to use name like list , data etc as some of them are in the 
# pre defined library so it may create comfusion 
randomlist.append("\nYou did great , next time need more better ")
print (randomlist)

# sorting , a list with numbers use listname.sort() to sort the list eg..

nums=[5,3,22,48,4,8,56]
print(nums)
nums.sort()
print(nums)

# reverse use listname.reverse() to reverse the contents 

nums.reverse()
print (nums)

# works on any list , here we just applied it on the sorted string 
# but it works on sorted unsorted string all..

#insert ...
# insert any element at the specific position ... and note 
# Append adds the element at last but insert at any index ...eg.
# syntaxis listname.insert (index,element )

nums.insert(3,123)
print(nums)

# not it can insert any type of element at the index . like you can write 
# nums.insert(3,"Hello world") , will add hello world at 3 , but here maybe we working with numbers so...


"""
pop listname.pop(index) , remove element at the index 
it actually do 2 works  

1. return the element that is poped out , removed eg if you print the listname.pop(index)
it will print the element removed 

2.remove the element at the index

eg here we added at 123 at index 3 , so lets remove it 
"""

print ("removed element : ",nums.pop(3))

print (nums)

'''
stringname.remove(element): Will remove 21 from the list. (if present )
heere in list , suppose lets remove 22,
'''
print ("Before numbers are ",nums)
nums.remove(22)
print ("after numbers are ",nums)

"""
lets insert back 22

"""

nums.insert(3,22)
print (nums)

nums.sort()
print (nums)