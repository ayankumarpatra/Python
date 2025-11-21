# print all element in a list use list and index as parameters 

def Print_Elements(mainlist,No_Of_Elements):
    # for i in range (No_Of_Elements):
    #     print(f"{mainlist[i]} ,",end=" ")
    # or a simpler approach
    if(len(mainlist==0 ) or No_Of_Elements==0):
        print("No elements are there in the list, please retry\n")
        return
    for element in mainlist:
        print(element ,end=" ," )


No_Of_Elements=int(input("Enter no of elements in the list : "))

mainlist=[]

for i in range (No_Of_Elements):
    n=(input(f"Enter element{i+1} "))
    mainlist.append(n)

Print_Elements(mainlist,No_Of_Elements)
