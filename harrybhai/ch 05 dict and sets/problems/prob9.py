'''
Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]} 

1.  s = {8, 7, 12, "Harry", [1,2]}
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    s = {8, 7, 12, "Harry", [1,2]}
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'  

fo firstly , you cant add the list in a set becuase sets in python requires to be all the elements are 
hashable and immutable 

2. even think we added , still list doesnt have indexing , so how can we point towards 1 or 2 
'''