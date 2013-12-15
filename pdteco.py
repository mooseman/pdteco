
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

import string, linecache, os, fileinput, curses
    
  
  
class editor(object): 
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
      
     
     
# Now the curses side of things. 
#  A class to handle keystrokes  
class keyhandler:
    def __init__(self, scr): 
       self.scr = scr                       
       # Dictionary to store our data in. This uses the line-number as 
       # the key, and the line text as the data.    
       self.data = {}      
       
       self.stuff = ""        
       
       # A variable to save the line-number of text. 
       self.win_y = self.win_x = 0  
       
       # The screen size (number of rows and columns). 
       (self.max_y, self.max_x) = self.scr.getmaxyx()
       # The top and bottom lines. These are defined because they help 
       # with page-up and page-down.  
       self.topline = 0
       self.bottomline = self.max_y - 1                            
       # Set page size (for page-up and page-down) 
       self.pagesize = self.max_y-1      
                                           
       curses.noecho() 
       self.scr.keypad(1)            
       self.scr.scrollok(1)
       self.scr.idlok(1)  
       self.scr.setscrreg(0, self.max_y-1)                                
       self.scr.refresh()	    
     
    def action(self):  
       while (1): 
          curses.echo()                 
          (y, x) = self.scr.getyx()   
          c=self.scr.getch()		# Get a keystroke    
                                                                                                
          if c in (curses.KEY_ENTER, 10):  
             #self.nextline()              
             pass 
          elif c==curses.KEY_BACKSPACE:  
             pass              
          elif c==curses.KEY_DC:  
             curses.noecho()                
             #self.removechar()                                               
             self.scr.refresh()                                         
          elif c==curses.KEY_UP:  
             curses.noecho()                
             self.scr.refresh()                                         
          # Ctrl-G quits the app                  
          elif c==curses.ascii.BEL: 
             break      
          elif 0<c<256:               
             c=chr(c)   
             if x < self.max_x-2:  
                self.stuff += c                           
             else:                 
                self.nextline()      
     
                                                                                                       
#  Main loop       
def main(stdscr):  
    a = keyhandler(stdscr)      
    a.action() 
                                   
#  Run the code from the command-line 
if __name__ == '__main__':  
  try: 
     stdscr = curses.initscr()   
     curses.noecho() ; curses.cbreak()
     stdscr.keypad(1)
     main(stdscr)      # Enter the main loop
     # Set everything back to normal
     stdscr.keypad(0)
     curses.echo() ; curses.nocbreak()
     curses.endwin()  # Terminate curses
  except:
     # In the event of an error, restore the terminal
     # to a sane state.
     stdscr.keypad(0)
     curses.echo() ; curses.nocbreak()
     curses.endwin()
     traceback.print_exc()  # Print the exception



