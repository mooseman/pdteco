
# custom_prompt.py
# Creates a custom Python prompt to run commands from

# This code is released to the public domain

# Some commands - 5r$$, 7l$$, 3u$$, 4d$$ 

import string, sys, os, cmd, fileinput 

class myShell(cmd.Cmd):
   prompt = 'teco>'
   intro = 'Welcome to teco'
   def do_exit(self, line):
      return True
   def do_quit(self, line):
      return True
      
   def open(self, fname): 
      myfile = file.open(fname, 'r+')     
      
   def move(self, line): 
      pass    
      
   def find(self, line): 
      pass       
      
   def insert(self, line): 
      pass    
      
   def delete(self, line): 
      pass    
      
   def save(self, line): 
      pass    
      
   
   
   
if __name__ == '__main__':
    a = myShell()
    a.cmdloop() 
    
    

