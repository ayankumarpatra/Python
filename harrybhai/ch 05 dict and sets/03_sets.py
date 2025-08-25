s={1,2,3}
# s is a set here containing 1,2,3
'''
Dont create set by s={ }, it will create an empty dictionary , not set 
so to create an empty set 
'''
st = set()# set is pre defined , you cant give name of a variable as set 

'''
set features 

1. no repeated elements , even if you give 
2. sets are unsorted , if you give 3,6,2,7 it will store as it is without sorting  
3. unindexed , cant access element by index , like str[0] first element , nothing such in set 
4. no way to change items in the sets  , but you can remove
'''
s= {1,2,3,4,4,4,5,5,6}
print (s)
#output will be like {1, 2, 3, 4, 5, 6} , even 4 , 5 repetive given it will be ommitted 
'''
to add any element , you can choose to do like ..
'''
s.add(456)
print (s)
# s.add(456,110,3,3,4,5)
# print (s) , cant add more than 1 elment 


'''
similarly s.remove(x) ,Removes element `x`, error if not found 
also cant remove multiple elements 

'''
s.remove(3)
print(s)

'''
s.update([x, y]) ,Adds multiple elements  
also as set caant contain repetative element , so any repetative element will be removed 
'''

s.update([4,5,66,7,8,88])
print(s)


'''
| Operation        | Syntax                | Description / Use Case                  | Example Output                  |
| ---------------- | --------------------- | --------------------------------------- | ------------------------------- |
| **Add**          | `s.add(x)`            | Adds one element `x`                    | `{1, 2} → add(3) → {1, 2, 3}`   |
| **Update**       | `s.update([x, y])`    | Adds multiple elements                  | `{1} → update([2,3]) → {1,2,3}` |
| **Remove**       | `s.remove(x)`         | Removes element `x`, error if not found | `{1,2,3} → remove(2) → {1,3}`   |
| **Discard**      | `s.discard(x)`        | Removes `x`, no error if not found      | `{1,2} → discard(5) → {1,2}`    |
| **Pop**          | `s.pop()`             | Removes a random element                | `{10,20,30} → pop() → {20,30}`  |
| **Clear**        | `s.clear()`           | Removes all elements                    | `{1,2,3} → clear() → set()`     |
| **Union**        | `s1.union(s2)`        | Combines both sets without duplicates   | `{1,2}.union({2,3}) → {1,2,3}`  |
| **Intersection** | `s1.intersection(s2)` | Common elements from both sets          | `{1,2,3} ∩ {2,3,4} → {2,3}`     |
| **Difference**   | `s1.difference(s2)`   | Elements in s1 but not in s2            | `{1,2,3} - {2,4} → {1,3}`       |
| **Subset**       | `s1.issubset(s2)`     | True if all s1 in s2                    | `{1,2} ⊆ {1,2,3} → True`        |
| **Superset**     | `s1.issuperset(s2)`   | True if s1 has all elements of s2       | `{1,2,3} ⊇ {2} → True`          |
| **Copy**         | `s.copy()`            | Creates a new copy of the set           | `{1,2} → copy() → {1,2}`        |


'''