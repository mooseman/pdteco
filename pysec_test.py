

#  pysec_test.py 
#  Try using the Pysec parser. 

import pysec 
from pysec import * 

sql_grammar = [] 

select_stmt = group("SELECT" & "*" & "from" & "mytable" & ";") 

sql_grammar.extend(select_stmt) 

#  Test the code 
print sql_grammar.parseString("SELECT * from mytable;")




