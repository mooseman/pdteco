

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
        
    def _get_int_until(self, c):
       num = int(self._get(self.data.index(c, self.ptr)-self.ptr))
       self._get(1) # kill extra char
       return num
        
    def _get_str(self): 
       return self._get(self._get_int_until(":"))
       
    def _get_int(self): 
       return self._get_int_until("e")
       
    def decode(self):
       i = self._get(1)
       if i == "d":
          r = {}
          while self._cur() != "e":
             key = self._get_str()
             val = self.decode()
             r[key] = val
             self._get(1)
        elif i == "l":
             r = []
             while self._cur() != "e": 
                r.append(self.decode())
                self._get(1)
        elif i == "i": r = self._get_int()
        elif i.isdigit():
            self._get(-1) # reeeeewind
            r = self._get_str()
        return r


# Test the code 
a = parser() 



