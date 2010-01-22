

#  tokenise.py  
#  Tokenise input data

class tok(object): 
   def __init__(self): 
      self.numlines = 0 
      self.buf = ""    
      # The position of the pointer is made up of the row, and the 
      # position on the row.     
      self.pos = [0, 0] 
      self.linenum = self.pos[0] 
      self.colnum = self.pos[1] 
                       
   # Opon a file              
   def open(self, fname): 
      self.myfile = open(fname, 'r+').read().splitlines() 
      #The number of lines in the file 
      self.numlines = len(self.myfile)  
   
   # Show the current position of the pointer.                 
   def tell(self): 
      return self.pos   
      
   # Move up or down by "x" lines    
   def lmove(self, x): 
      self.pos[0] += x 
      
   # Move within a line by "x" bytes.  
   def move(self, x):  
      if 0 <= (self.colnum + x) <= len(self.myfile[self.linenum]): 
         self.pos[1] += x 
      else: 
         pass    
          
   # Get some data             
   def get(self, num): 
      self.buf = self.myfile[self.linenum][self.colnum: self.colnum + num] 
      return self.buf 
      
   # Delete "x" characters at the current position.   
   def delete(self, x):    
      pass 
      
   # Write the string str    
   def put(self, str):    
      pass       
       
   # Search for come text  
   # Limitation - this can't search for text which spans lines. 
   def find(self, text): 
      for line in self.myfile: 
         if text in line: 
            print "found" 
            break 
         else: 
            print "not found"                
            break 
          
   def display(self): 
      print self.myfile        
          
          
# Test the code 
a = tok() 
a.open('myfile.txt') 
print a.tell() 
print a.get(10) 
a.move(7)    
print a.tell()             
a.find("lamb")             
a.display() 
