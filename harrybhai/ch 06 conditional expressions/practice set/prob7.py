'''
Write a program to find out whether a given post is talking about “Harry” or not. 
'''

post=input ("Enter your post here : ")

temppost=post.lower()
if ("harry" in temppost):
    print("POst contains harry")
else :
    print("POst does not contains harry")