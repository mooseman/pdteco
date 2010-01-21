

#  pdtokenise.py 
#  A public-domain Python tokenize function which can 
#  be used with programming languages other than Python. 
#  This tokenize is meant to be compatible with Python's 
#  tokenize. NOTE - we will include a user-specified token 
#  separator (with a default value for that). 

#  From the Python docs for tokenize - 
#  tokenize.tokenize(readline)
#  
#  "The generator produces 5-tuples with these members: 
#  the token type; the token string; a 2-tuple (srow, scol) of ints 
#  specifying the row and column where the token begins in the source; 
#  a 2-tuple (erow, ecol) of ints specifying the row and column where 
#  the token ends in the source; and the line on which the token was 
#  found. The line passed (the last tuple item) is the logical line; 
#  continuation lines are included. The 5 tuple is returned as a named 
#  tuple with the field names: type string start end line."  

#  "Type" here means the token type - number, string, punct, etc. 
#  The "token string" is the token itself. 

import cString, string, io, os, os.path, fileinput  

# Need to get - token type, token, startpos, endpos, line.
def tokenise(data, sep=" ")  
   tokenlist = [] 
   data, ptr = data, 0  
   tokentype = token = None 
   startpos = endpos = [0,0]
   line = 0 
   
   # See if data is from a file 
   if os.path.isfile(data): 
      myfile = open(data, 'r') 
      # Parse the data in the file 
   else: 
      # Parse the supplied data 
      for x in data: 
         pass 


 
