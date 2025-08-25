'''
3. A spam comment is defined as a text containing following keywords: 
“Make a lot of money"
"buy now" "subscribe this" "click this"
 Write a program 
to detect these spams.
'''

filter_1="Make a lot of money"
filter_2="buy now"
filter_3="subscribe this"
filter_4="click this"

comment=input ("Enter your comment here : ")

if (filter_1 in comment or filter_2 in comment or filter_3 in comment or filter_4 in comment ):
        flag = 1
        print ("Spam Detected")
else :
        flag = 0
        print ("Not Spam")
# i added the flag by myself , if we have to delete the comment etc later or anything we have to do 
'''
one more thing we can do here , it cant detect Buy noe or bUy now etc as the texts are case sensitive , 
so we can do like
comment=input ("Enter your comment here : ")
tempcomment =comment.lower()
print (tempcomment)

now we can do further actions on tempcomment , as  user sometimes may want to keep the main comment as it is , so 
if flag =0 then will print the main comment else discard 

or also we can do like 

filters = ["make a lot of money", "buy now", "subscribe this", "click this"]

for word in filters:
    if word in tempcomment:
        flag = 1
        break
else:
    flag = 0

'''
