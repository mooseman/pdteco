
#  pdteco.py  
#  A public-domain Python implementation of the core commands of TECO. 

#  This code is released to the public domain. 
#  "Share and enjoy....."  ;)  
#  
#  *** To do......  *** 
#  NOTE - the built-in functions f.tell() and f.seek() should be very 
#  useful. 
#  From the Python docs - 
#  f.tell() returns an integer giving the file objects current position 
#  in the file, measured in bytes from the beginning of the file. 
#  To change the file objects position, use f.seek(offset, from_what). 
#  The position is computed from adding offset to a reference point; 
#  the reference point is selected by the from_what argument. 
#  A from_what value of 0 measures from the beginning of the file, 
#  1 uses the current file position, and 2 uses the end of the file 
#  as the reference point. 
#  from_what can be omitted and defaults to 0, using the beginning of 
#  the file as the reference point.  

#  NOTE - Most TECO commands follow this general pattern -  
#  nX string ESC  

#  We need to implement the following types of commands - 
#  a) File commands - 
#        - ERfname$  - open file fname for read access 
#        - EBfname$  - open file for read/write with backup 
#        - EWfname$  - open file for writing.   
#        - EX$$ - close output file and exit.   

#  b) The eight basic Teco functions 
#        - DOT (current value of POINT)
#        - nC - Move POINT \T{n} characters forward. 
#        - nD - Delete \T{n} characters. 
#        - Istring\A{ESC} - Insert text. 
#        - nJ - Move POINT to absolute position \T{n} 
#        - m,nK - Kill a range of characters. 
#        - Sstring\A{ESC} - Search for a string. 
#        - Z - Current buffer size.  
#  c) Line-oriented commands - 
#        - nL - Move to beginning of $\T{n}^{th}$ line from \POINT{}. 
#        - nK - Kill from point  to beginning of $\T{n}^{th}$ following
#               line. 
#  d) Looping -  
#        - n< - Begin \T{n}-iteration loop. 
#        - >  - End loop. 
#        - n; - Exit loop if $\T{n} \geq 0$.  
#  e) Conditionals -  
#        - n"x - ( To be completed..... )      
#  f) "Q-registers", to store results. 
#  g) Conversion functions, from numbers to strings and vice versa.  
    
#  Helper functions 

#  Move n characters left or right from current position 
#  Use f.seek(n, 1) where 1 denotes "measure from current position" 

import string, linecache, os, fileinput    
from yeanpypa import *   
  
#  Teco commands. We put these in a grammar using yeanpypa. 
dbl_escape = Word( Literal('$') + Literal('$') )

escape = Literal('$') 

file = Literal('a') | Literal('b') | Literal('c') | Literal('d') \
       | Literal('e') | Literal('f') | Literal('g') | Literal('h') 
       
rank = Literal('1') | Literal('2') | Literal('3') | Literal('4') \
       | Literal('5') | Literal('6') | Literal('7') | Literal('8')         

square = Word( file + rank ) 


# dbl_escape = Word(escape + escape) 

#dbl_escape = Word( escape + escape )

#string = Literal('"') + alpha + Word(alpha | digit) + Literal('"') 

#operator =  Literal("=") | Literal("<") | Literal(">")  

stmt = escape | dbl_escape | file | rank | square 

# | string | operator 

grammar = stmt 


#  A function to parse input
def parseit(grammar, input):

    result = parse(grammar, input)

    if result.full(): 
       print "Success!" 
    else: 
       print "Fail"  


#  Parse a few moves
#parseit(grammar, "test")
#parseit(grammar, ">")
#parseit(grammar, "=")
parseit(grammar, "$") 
parseit(grammar, "$$")
parseit(grammar, "e4")



