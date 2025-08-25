''' 
7. Write a python function to remove a given word from a list and strip it at the same 
time. 
'''

def removestrip (friends,word):
    tempfriends = []
    for item in friends :
        if not (item==word):
            tempfriends.replace(item.strip(word))
    return tempfriends



friends=["Rohan","harry","Sams","oppo",'pp']
'''
or we can take names manually by friends=[]

for i in range (5):
    name=input("Enter the name: ")
    friends.append(name)

print(friends)
'''
remove_word=input("Enter the word to remove")
removestrip(friends,remove_word)

print(removestrip(friends,remove_word))