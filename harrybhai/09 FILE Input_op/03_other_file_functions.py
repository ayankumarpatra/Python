f=open("updatedfile.txt")

lines=f.readlines()

print(lines)

print(type(lines))
# it will read and return all the lines as a list of strings 

# to get a specific line , we will just give the line number after that eg 
# to get line 3 , do like line3=f.readline() // not readlines , done print 
f.seek(0)    

# have to set the file pointer to the first position , else it will return a empty string 
line1 =f.readline()
line3 =f.readline()
print(line1)
print(line3)

f.close()