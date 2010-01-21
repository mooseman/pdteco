

#  tokenise.py  
#  Tokenise input data

class tok(object): 
   def __init__(self, data): 
      self.data, self.ptr = data, 0
      
   def _cur(self): 
      return self.data[self.ptr]
      
   def _get(self, x):
      self.ptr += x
      return self.data[self.ptr-x:self.ptr]
            
   def read(self): 
      #while self._cur() != "":
      while self._cur() != "*":
         i = self._get(1)
         if i == "$": 
            self.type = "foo" 
            print self.type      
            #self._get(1)                      
         else: 
            self.type = "bar" 
            print self.type          
          

# Test the code 
a = tok("abc$$def$$*") 
a.read() 
               
            



