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
# it will read the 0th line (indexing starts with 0 )
line3 =f.readline()
# actually f.readline is a pointer that points towards the last open location , but note , if you get all 
# data by .readlines , it will move the pointer to end 
# now it the next line

# but if you do like out of bound access eg 3 line , give 4 time readline , it will give a empty string 
print(line1)
print(line3)

f.close()