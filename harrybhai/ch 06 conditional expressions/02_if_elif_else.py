# if elif else ... , elif is just like else if , elif also must contain a valid checking 
# condition like if block , else block doesnt need any checking condition 
# also note one thing in the ladder , if , elif , else , only 1 block will be executed 
# either if or elif or other elif or else , not more than 1 block 
# to execute more than 1 block to execute , use multiple if  

age = int (input ("Enter theage : "))

if (age>=15):
    print ("Age is above 15")
    print ("You can access the game")
elif (age<0):
    print ("invalid age , negetive age entered ")
elif (age==0):
    print ("invalid age ,age =0 entered ")
else :
    print ("Age is bellow 15")
    print ("You can access the game")