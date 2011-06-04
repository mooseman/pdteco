
#  pdteco.py  
#  A public-domain Python implementation of the core commands of TECO. 

#  This code is released to the public domain. 
#  "Share and enjoy....."  ;)  
#  
#  *** To do......  *** 
#  NOTE - the built-in functions f.tell() and f.seek() should be very 
#  useful. 
#  From the Python docs - 
#  f.tell() returns an integer giving the file objects current position 
#  in the file, measured in bytes from the beginning of the file. 
#  To change the file objects position, use f.seek(offset, from_what). 
#  The position is computed from adding offset to a reference point; 
#  the reference point is selected by the from_what argument. 
#  A from_what value of 0 measures from the beginning of the file, 
#  1 uses the current file position, and 2 uses the end of the file 
#  as the reference point. 
#  from_what can be omitted and defaults to 0, using the beginning of 
#  the file as the reference point.  

#  NOTE - Most TECO commands follow this general pattern -  
#  nX string ESC  

#  We need to implement the following types of commands - 
#  a) File commands - 
#        - ERfname$  - open file fname for read access 
#        - EBfname$  - open file for read/write with backup 
#        - EWfname$  - open file for writing.   
#        - EX$$ - close output file and exit.   

#  b) The eight basic Teco functions 
#        - DOT (current value of POINT)
#        - nC - Move POINT \T{n} characters forward. 
#        - nD - Delete \T{n} characters. 
#        - Istring\A{ESC} - Insert text. 
#        - nJ - Move POINT to absolute position \T{n} 
#        - m,nK - Kill a range of characters. 
#        - Sstring\A{ESC} - Search for a string. 
#        - Z - Current buffer size.  
#  c) Line-oriented commands - 
#        - nL - Move to beginning of $\T{n}^{th}$ line from \POINT{}. 
#        - nK - Kill from point  to beginning of $\T{n}^{th}$ following
#               line. 
#  d) Looping -  
#        - n< - Begin \T{n}-iteration loop. 
#        - >  - End loop. 
#        - n; - Exit loop if $\T{n} \geq 0$.  
#  e) Conditionals -  
#        - n"x - ( To be completed..... )      
#  f) "Q-registers", to store results. 
#  g) Conversion functions, from numbers to strings and vice versa.  
    
#  Helper functions 

#  Move n characters left or right from current position 
#  Use f.seek(n, 1) where 1 denotes "measure from current position" 

import string, linecache, fileinput  

 
class edit(object):
   def __init__(self):
      self.numlines = 0
      self.buf = ""
      # The position of the pointer is made up of the row, and the
      # position on the row.
      self.pos = [0, 0]
      self.linenum = self.pos[0]
      self.colnum = self.pos[1]
                       
   # Opon a file
   def open(self, fname):
      self.myfile = open(fname, 'r+').read().splitlines()
      #The number of lines in the file
      self.numlines = len(self.myfile) 
      
   # Close the file
   def close(self):
      self.outfile.close()
      
   # Save the file
   def save(self):
      self.outfile = open('outfile.txt', 'w') 
      self.outfile.writelines(self.myfile) 
      
   # Show the current position of the pointer.
   def tell(self):
      return self.pos
      
   # Move up or down by "x" lines
   def lmove(self, x):
      self.pos[0] += x
      self.linenum += x
      
   # Move within a line by "x" bytes.
   def move(self, x):
      if 0 <= (self.colnum + x) <= len(self.myfile[self.linenum]):
         self.pos[1] += x
         self.colnum += x
      else:
         pass
          
   # Get some data
   def get(self, num):
      self.buf = self.myfile[self.linenum][self.colnum: self.colnum + num]
      return self.buf
      
   # Delete "x" characters at the current position.
   # Because Python strings can't be changed, we create a new string
   # and make that the new version of the line.
   def delete(self, x):
      # This is the content of the part of the line BEFORE the pointer.
      starttext = self.myfile[self.linenum][0:self.colnum]
      endtext = self.myfile[self.linenum][self.colnum+x:len(self.myfile[self.linenum])]
      # Create the new version of the line, with the text inserted into it.
      self.myfile[self.linenum] = starttext + endtext
            
   # Write the string str. Because Python strings can't be changed, we
   # create a new string and make that the new version of the line.
   def insert(self, str):
      # This is the content of the part of the line BEFORE the pointer.
      starttext = self.myfile[self.linenum][0:self.colnum]
      endtext = self.myfile[self.linenum][self.colnum:len(self.myfile[self.linenum])]
      # Create the new version of the line, with the text inserted into it.
      self.myfile[self.linenum] = starttext + str + endtext
             
   # Search for come text
   # Limitation - this can't search for text which spans lines.
   def find(self, text):
      for line in self.myfile:
         if text in line:
            print "found"
            break
         else:
            print "not found"
            break
          
   # Repeat a command a given number of times. 
   def repeat(self, cmd, *args): 
      pass           
          
   def display(self):
      print self.myfile
          
          
# Test the code
a = edit()
a.open('test.txt')
print a.tell()
a.display()  
print a.get(4) 
a.move(7)    
print a.tell()             
a.find("second")             
a.insert("moose") 
a.move(5) 
a.delete(8)  
a.lmove(4) 
a.move(3)
a.insert("The quick brown fox")
print a.tell() 
a.save() 
a.display() 
a.close() 
 
