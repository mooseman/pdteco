

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
      
   def open(self, fname): 
      self.myfile = open(fname, 'r+').readlines()  
      #The number of lines in the file 
      self.numlines = len(self.myfile)   
      
      
   # Now - THIS part of the code is concerned with TECO. 
   # We have opened a file. Now, we can do various operations on it.          
   def read(self): 
      for x in self.data:      
         i = self._get(1)
         if i == "$": 
            self.type = "foo" 
            print self.type                  
         else: 
            self.type = "bar" 
            print self.type          
          

# Test the code 
a = tok("abc$$def$$") 
a.read() 
               
            



