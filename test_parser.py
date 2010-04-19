

# test_parser.py
# Try a few things with creating tokens which know the 
# kind of token that should follow them. 

import string, itertools   

class token(object): 
   def __init__(self): 
      self.type = self.next = self.stmttype = None 
      self.attrdict = vars(self) 
   
   # Set an attribute 
   # NOTE! This can als be used to store values to be passed 
   # to the next token.    
   def set(self, attr, val): 
      setattr(self, attr, val) 
            
   # Get an attribute from a token. 
   def get(self, attr): 
      return getattr(self, attr)
         
   def display(self): 
      print self.attrdict 
      

# Test the code       
a = token() 
a.set('type', 'foo') 
a.set('next', 'bar') 
a.set('moose', 'big') 
print a.get('next')
a.display() 


#  Create a parser with two modes - character and word. 
# Note - we could add a statement checker to this. It would look at the 
# stmttype of tokens to determine which kind of statement they belong in.
# When a statement is complete, it can flag that and act accordingly. 
# Also - attach actions to statements. 
class parser(object): 
   def __init__(self): 
      self.toklist = [] 
      self.mode = None 
      
   def setmode(self, mode): 
      self.mode = mode
      
   # Clear the token list    
   def clear(self):    
      self.toklist = [] 
            
   def parse(self, stuff, sep=" "): 
      if self.mode == 'char': 
         for ch in stuff: 
            self.toklist.append(ch)          
      elif self.mode == 'word': 
         for tok in stuff.split(sep): 
            self.toklist.append(tok) 
             
   def display(self): 
      print self.toklist 
      
      
# Test the code
a = parser() 
a.setmode('char') 
a.parse('The quick brown fox') 
a.display() 
a.setmode('word') 
a.clear()
a.parse('The quick brown fox') 
a.display() 

            




      
 

