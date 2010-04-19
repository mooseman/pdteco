

#  storecmds.py 
#  Store the requested commands and arguments 
#  until given the go-ahead to run them. 

#  The TECO commands we want are - 
#  Files - Read, write, save, close. 
#  Lines - Move between lines, within lines. Go to a line. 
#  Move "x" lines up or down. Move "x" bytes back or forward. 
#  Editing - Insert, delete, type. 
#  Looping - repeat a command "x" times. 
#  Variables - define and use. 
#  Macros - define and run. 


argstack = cmdstack = []
cmddict = {} 

# A stack for arguments. 
def argstack(args): 
  for arg in args:
     argstack.push(arg)
    
# A stack for commands.     
def cmdstack(cmd): 
  cmdstack.push(cmd)  

# A dict to map TECO command abbreviations to their Python equivalents.
def fillcmddict(): 
    cmddict.update({"T": "print", 
                    "D": "del" , 
                    "L": "move",    
                    "I": "insert" , 
                    "S": "search" }) 
                    
# Print the command dict 

fillcmddict() 

for x in cmddict.items(): 
   print x 
   
                        
    


