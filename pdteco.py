
#  pdteco.py  
#  A public-domain Python implementation of the core commands of TECO. 

#  This code is released to the public domain. 
#  "Share and enjoy....."  ;)  

#  Acknowledgement - Very many thanks to the developers of the 
#  public-domain implementation of TECO which runs under "eel".  
#  That version of TECO is available here - 
#  http://www.ibiblio.org/pub/academic/computer-science/history/pdp-11/teco/eel/
#  This Python implementation would have been much more difficult if that 
#  version had not been available. 


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
#  a) The eight basic Teco functions 
#        - DOT (current value of POINT)
#        - nC - Move POINT \T{n} characters forward. 
#        - nD - Delete \T{n} characters. 
#        - Istring\A{ESC} - Insert text. 
#        - nJ - Move POINT to absolute position \T{n} 
#        - m,nK - Kill a range of characters. 
#        - Sstring\A{ESC} - Search for a string. 
#        - Z - Current buffer size.  
#  b) Line-oriented commands - 
#        - nL - Move to beginning of $\T{n}^{th}$ line from \POINT{}. 
#        - nK - Kill from point  to beginning of $\T{n}^{th}$ following
#               line. 
#  c) Looping -  
#        - n< - Begin \T{n}-iteration loop. 
#        - >  - End loop. 
#        - n; - Exit loop if $\T{n} \geq 0$.  
#  d) Conditionals -  
#        - n"x - ( To be completed..... )      
#  e) "Q-registers", to store results. 
#  f) Conversion functions, from numbers to strings and vice versa.  
    

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
      
                                                             
# Test the code    
a = teco() 




  


