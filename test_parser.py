

# test_parser.py
# Try a few things with creating tokens which know the 
# kind of token that should follow them. 

class token(object): 
   def __init__(self): 
      self.type = self.next = self.stmttype = None 
      self.attrdict = vars(self) 
   
   # Set an attribute    
   def set(self, attr, val): 
      if hasattr(self, attr):  
         setattr(self, attr, val) 
      else: 
         pass 
      
   # Get an attribute from a token. 
   def get(self, attr): 
      return getattr(self, attr)
         
   def display(self): 
      print self.attrdict 
      

# Test the code       
a = token() 
a.set('type', 'foo') 
a.set('next', 'bar') 
print a.get('next')
a.display() 




      
 

