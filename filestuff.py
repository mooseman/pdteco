

#  filestuff.py 
#  Playing around with f.tell(), f.seek() and so on. 
#  With f.seek(x, n) - n=0 measures from the start of the file. 
#  n=1 measures from the current file position. n=2 measures from the 
#  end of the file. 
#  Note - the linecache module allows random access to text files. This 
#  lets you jump forwards and backwards by line number. 
#  We can also use readlines(). This reads the whole file into a list 
#  of lines, making it very easy to move around the file by line. 

import linecache, os, fileinput  

# Open a file 
myfile = open("myfile.txt", 'r') 

# A string to store data in. 
stuff = ""

# Find the file descriptor
myfd = myfile.fileno()

# Print the current pointer position 
print "I am at ", myfile.tell() 

print "this is file ",  myfd 

# Use os.lseek() and see what it does. It actually moves the 
# "start of file" pointer by n bytes.  
# os.lseek(myfd, 2, 0)

#myfile.readline() 

# print "After lseek I am at ", myfile.tell() 

from itertools import islice

# A "line-seek" function. This is from the c.l.python mailing-list - 
def seek_to_line(f, n):
    for ignored_line in islice(f, n - 1):
        pass   # skip n-1 lines

# Try out the function 
f = open('fname')
seek_to_line(f, 10)    # seek to line 10

# print lines 10 and later
for line in f:
    print line 


# Read a few bytes from the file into our string. 
stuff = myfile.read(7) 

# Print the data 
print stuff 


myfile.readline() 

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




