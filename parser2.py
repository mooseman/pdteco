

# parser.py
# Acknowledgement - this code is based on the public domain code from here - 
# http://buffis.com/2007/07/28/bittorrent-bencode-decoder-in-python-
# using-30-lines-of-code/


class parser(object):
    def __init__(self, data): 
       self.data, self.ptr = data, 0
    
    # Return the data at the pointer    
    def _cur(self): 
       return self.data[self.ptr]
       
    # Get x bytes from the pointer to x    
    def _get(self, x):
       self.ptr += x
       return self.data[self.ptr-x:self.ptr]
    
    # Do stuff.                
    def decode(self):
       i = self._get(1)
       # Might make this a "while true" 
       while self._cur() != "*":
          print "foo"       
          self._get(1)
        
       
# Test the code 
a = parser() 



