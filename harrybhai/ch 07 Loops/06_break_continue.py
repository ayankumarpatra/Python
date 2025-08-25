for i in range (20):
    print (i)
    if (i==10):
        break
# as soon as it get the break command , it will exit the loop immidietly , doesnt mater loop conditions 
for i in range (20): 
    
    if (i==10):
        continue
    print (i)
    
# continue will skip the current iteration from further being executed only ...
# note , if you given print i before the if , it will print 10 also , as you are printing first 
# then checking the condition
