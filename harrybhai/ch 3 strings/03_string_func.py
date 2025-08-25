str ="hello world"

#1 len
print ("Length of the string is : ",len(str))

#2 startswith and endswith , it will return boolean either true or false 
# syntax stringname.endsorstartswith("words")

print(str.endswith("rld"))

print (str.startswith("ello"))

# 3. string.count("c") – counts the total number of occurrences of any character. 
str1 = "harry" 
count = str1.count("r") 
# print(count)  # Output: 2
 
# 4. the first character of a given string. 
# str1 = "harry" 
capitalized_string = str1.capitalize() 
print(capitalized_string)  # Output: "Harry" 

# 5. string.find(word) – This function friends a word and returns the index of first 
# occurrence of that word in the string. 
# str1 = "harry" 
index = str.find("rr") 
print(index)  # Output: 2 

# 6. string.replace (old word, new word ) – This function replace the old word with 
# new word in the entire string, but will replace each and every element in the entire string . 
# str = "harry" 
replaced_string = str.replace("r", "l") 
print(replaced_string)  # Output: "hally"  