num=int(input("Enter total number of linrs "))
if(num%2==0):
    print_limit=int(num/2)-1
else:
    print_limit=int(num/2)

for i in range (1,print_limit+1):
    spaces=print_limit-i+1
    while(spaces>0):
        print(" ",end="")
        spaces-=1
    for j in range (1,i+1):
        print(j,end=" ")
    print("")

for k in range (1,print_limit+2):
    print(k,end=" ")

print("")

for l in range (print_limit,0,-1):
    rev_spaces=print_limit-l+1
    while(rev_spaces>0):
        print(" ",end="")
        rev_spaces-=1
    for m in range (1,l+1):
        print(m,end=" ")
    print("")

