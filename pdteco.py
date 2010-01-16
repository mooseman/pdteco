
#  pdteco.py  
#  A public-domain Python implementation of the core commands of TECO. 

#  This code is released to the public domain. 
#  "Share and enjoy....."  ;)  

#  Acknowledgement - Very many thanks to the developers of the 
#  public-domain "eel" implementation of TECO, available here - 
#  http://www.ibiblio.org/pub/academic/computer-science/history/pdp-11/teco/eel/
#  This Python implementation would have been much more difficult if that 
#  version had not been available. 


#  *** To do......  *** 
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
      self.fname = None 
      self.pos = self.line = 0
      
   def command(self, cmd):  
      self.cmd = cmd 
      # Handle the supplied command. 
                                    
   def ins(self, ch)   
      pass 



  


