

# iterator_parser.py 

# Acknowledgement - Very many thanks to Fredrik Lundh for doing the 
# code below! 

# Note - this code is from the follwing site - 
# http://effbot.org/zone/simple-iterator-parser.htm 
# The copyright for this site says that "examples, test scripts and 
# other short code fragments can be considered as being in the public 
# domain." 
# This bit of code is mentioned to be an example, so I will accordingly 
# treat it as being in the public domain. Thanks again, Fredrik! 

import cStringIO, tokenize

def atom(next, token):
    if token[1] == "(":
        out = []
        token = next()
        while token[1] != ")":
            out.append(atom(next, token))
            token = next()
            if token[1] == ",":
                token = next()
        return tuple(out)
    elif token[0] is tokenize.STRING:
        return token[1][1:-1].decode("string-escape")
    elif token[0] is tokenize.NUMBER:
        try:
            return int(token[1], 0)
        except ValueError:
            return float(token[1])
    raise SyntaxError("malformed expression (%s)" % token[1])

def simple_eval(source):
    src = cStringIO.StringIO(source).readline
    src = tokenize.generate_tokens(src)
    src = (token for token in src if token[0] is not tokenize.NL)
    res = atom(src.next, src.next())
    if src.next()[0] is not tokenize.ENDMARKER:
        raise SyntaxError("bogus data after expression")
    return res

    
# Test the code 
print simple_eval("(1, 2, 3, \n4711.0)")


    
    
    
