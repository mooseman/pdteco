
#  pdteco.py  
#  A public-domain Python implementation of the core commands of TECO. 

#  This code is released to the public domain. 
#  "Share and enjoy....."  ;)  
#  
    
#  Helper functions 

#  Move n characters left or right from current position 
#  Use f.seek(n, 1) where 1 denotes "measure from current position" 

import string, linecache, os, fileinput, curses, curses.ascii, traceback
    
  
       
# Now the curses side of things. 
#  A class to handle keystrokes  
class keyhandler:
    def __init__(self, scr): 
       self.scr = scr                              
       
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
             if y > 0:                                   
                self.scr.move(y-1, x)                    
                self.set_y(-1)                   
             elif y == 0 and self.win_y > 0:   
                self.scr.scroll(-1)   
                self.scr.move(y, x)  
                self.set_y(-1)                 
             else: 
                pass                                                                                     
             self.scr.refresh()
          elif c==curses.KEY_DOWN:
             curses.noecho()              
             if y < self.max_y-1:                 
                self.scr.move(y+1, x)   
                self.set_y(1)                                                               
             else:                                          
                self.scr.scroll(1)                 
                self.scr.move(y, x)  
                self.set_y(1)                 
             self.scr.refresh()   
          elif c==curses.KEY_LEFT: 
             curses.noecho()  
             if x > 0: 
                self.scr.move(y, x-1) 
             else: 
                pass 
             self.scr.refresh()
          elif c==curses.KEY_RIGHT: 
             curses.noecho() 
             if x < self.max_x-1:
                self.scr.move(y, x+1) 
             else: 
                pass                 
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
     #traceback.print_exc()  # Print the exception



