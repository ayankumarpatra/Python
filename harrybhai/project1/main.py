'''
stone paper scissor 

'''

import random

yourchoice=int(input("1.for stone \n2.for paper \n3.for scissor \nEnter the choice : "))

computerchoice=random.choice([1,2,3])

dictopt={1:"stone",2:"paper",3:"scissor"}

if yourchoice==computerchoice:
    print("Its a tie \nBoth choose ",end="")
    print(dictopt.get(computerchoice))
elif((yourchoice==1 and computerchoice==3)or(yourchoice==2 and computerchoice==1) or (yourchoice==3 and computerchoice==2)):
    print("Great , you won \nComputer choose ",end="")
    print(dictopt.get(computerchoice))
    print("You choose: ",end="")
    print(dictopt.get(yourchoice))
elif((yourchoice==3 and computerchoice==1)or(yourchoice==1 and computerchoice==2) or (yourchoice==2 and computerchoice==3)):
    print("Soory , you loose \nComputer choose ",end="")
    print(dictopt.get(computerchoice))
    print("You choose: ",end="")
    print(dictopt.get(yourchoice))
