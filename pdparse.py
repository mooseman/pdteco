

#  pdparse.py  
#  See if it is possible to condense some of the Yeanpypa code 
#  down to a very simple parsing framework.  
#  This code is released to the public domain. 


class rule(object): 
   
   def match(inputreader): 
      pass 
      
   def __add__(self, second_rule):   
      return AndRule(self, second_rule)
      
   def __or__(self, second_rule):
      return OrRule(self, second_rule) 
      
      
         












