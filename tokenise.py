

#  tokenise.py  
#  Tokenise input data

class tok(object): 
   def __init__(self): 
      self.toklist = [] 
      self.ptr = 0 
      
   def read(self, data): 
      for x in data: 
         self.ptr += 1
         if x == "$": 
            self.type = "foo" 
         else: 
            self.type = "bar" 
         print self.type          
               

# Test the code 
a = tok() 
a.read("abc$$defgh$") 

               
            



