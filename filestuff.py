

#  filestuff.py 
#  Playing around with f.tell(), f.seek() and so on. 

# Open a file 
myfile = open("myfile.txt", 'r') 

# A string to store data in. 
stuff = ""

# Print the current pointer position 
print myfile.tell() 

# Advance the pointer 3 bytes from the start of the file. 
myfile.seek(3, 0) 

# Print the current pointer position 
print myfile.tell() 

# Read a few bytes from the file into our string. 
stuff = myfile.read(7) 

# Print the data 
print stuff 

# Close the file 
myfile.close() 











