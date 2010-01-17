
#  pdteco.py  
#  A public-domain Python implementation of the core commands of TECO. 

#  This code is released to the public domain. 
#  "Share and enjoy....."  ;)  
#  
#  *** To do......  *** 
#  NOTE - the built-in functions f.tell() and f.seek() should be very 
#  useful. 
#  From the Python docs - 
#  f.tell() returns an integer giving the file object’s current position 
#  in the file, measured in bytes from the beginning of the file. 
#  To change the file object’s position, use f.seek(offset, from_what). 
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
#        - ERfname$  - open file "fname" for read access 
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

import string, linecache, os, fileinput    
  
  
class teco(object): 
   def __init__(self): 
      self.dot = 0
      self.buf = [] 
      # The "Q-registers" (variables) 
      self.qregs = {}  
      self.fname = None 
      self.pos = self.line = 0
       
   # Open a file                   
   def open(self, fname):  
      #self.f = f.readlines() 
      self.f = open(fname, 'r+') 
      
   # Move to a line       
   def move2line(self, line): 
      pass 
      
   # Move by a given number of bytes from the current position   
   def moveinline(self, n):         
      self.f.seek(n, 1)   
   
   # Show the current position of the pointer. 
   def showptr(self): 
      return self.f.tell() 
        
   # Print a given number of bytes      
   def display(self, n):                            
      self.f.read(n)                            
      
   # Search for some text                         
   def search(self, str): 
      pass 
      
   # Replace some text       
   def replace(self, target, repwith):       
      pass  
      
   # Insert some text 
   def ins_text(self, txt):
      pass 
      
   # Delete some text 
   def del_text(self, txt): 
      pass 
      
                                                                                                       
# Test the code    
a = teco() 




  


