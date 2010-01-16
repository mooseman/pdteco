

#  filestuff.py 
#  Playing around with f.tell(), f.seek() and so on. 
#  With f.seek(x, n) - n=0 measures from the start of the file. 
#  n=1 measures from the current file position. n=2 measures from the 
#  end of the file. 

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

# Reset "stuff" to missing. 
stuff = ""

# Move the pointer to the start of the file. 
myfile.seek(0, 0) 

# Read a few bytes from the file into our string. 
stuff = myfile.read(10) 

# Print the data 
print stuff 

# Close the file 
myfile.close() 




