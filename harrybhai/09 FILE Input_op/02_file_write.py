st="Thank you for the journey , will give a better comeback"

f=open("updatedfile.txt","w") # w for write , if you dont give anything , by default it will open in read mode
# here if you give a name that doesnt exist in the pwd , it will create a file of that name , eg if we give
# abc.txt,"w"  it will create a file named abc.txt
f.write(st)
f.close()

f1=open("file.txt")
data=f1.read()
print(data)
f1.close()