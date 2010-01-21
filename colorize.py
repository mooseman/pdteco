
# Note - this code is from here - 
# http://gnosis.cx/TPiP/244.code 

# It is from David Mertz' book "Text Processing in Python". 
# David has very generously put the code in that book in the 
# public domain. Many thanks for that, David! 

# colorize.py 

import keyword, token, tokenize, sys
from cStringIO import StringIO

PLAIN = '%s'
BOLD  = '<b>%s</b>'
CBOLD = '<font color="%s"><b>%s</b></font>'
_KEYWORD = token.NT_OFFSET+1
_TEXT    = token.NT_OFFSET+2
COLORS   = { token.NUMBER:     'black',
             token.OP:         'darkblue',
             token.STRING:     'green',
             tokenize.COMMENT: 'darkred',
             token.NAME:       None,
             token.ERRORTOKEN: 'red',
             _KEYWORD:         'blue',
             _TEXT:            'black'  }

class ParsePython:
    "Colorize python source"
    def __init__(self, raw):
        self.inp  = StringIO(raw.expandtabs(4).strip())
    def toHTML(self):
        "Parse and send the colored source"
        raw = self.inp.getvalue()
        self.out = StringIO()
        self.lines = [0,0]      # store line offsets in self.lines
        self.lines += [i+1 for i in range(len(raw)) if raw[i]=='\n']
        self.lines += [len(raw)]
        self.pos = 0
        try:
            tokenize.tokenize(self.inp.readline, self)
            return self.out.getvalue()
        except tokenize.TokenError, ex:
            msg,ln = ex[0],ex[1][0]
            sys.stderr.write("ERROR: %s %s\n" %
                             (msg, raw[self.lines[ln]:]))
            return raw
    def __call__(self,toktype,toktext,(srow,scol),(erow,ecol),line):
        "Token handler"
        # calculate new positions
        oldpos = self.pos
        newpos = self.lines[srow] + scol
        self.pos = newpos + len(toktext)
        if toktype in [token.NEWLINE, tokenize.NL]:  # handle newlns
            self.out.write('\n')
            return
        if newpos > oldpos:     # send the orig whitspce, if needed
            self.out.write(self.inp.getvalue()[oldpos:newpos])
        if toktype in [token.INDENT, token.DEDENT]:
            self.pos = newpos   # skip indenting tokens
            return
        if token.LPAR <= toktype and toktype <= token.OP:
            toktype = token.OP  # map token type to a color group
        elif toktype == token.NAME and keyword.iskeyword(toktext):
            toktype = _KEYWORD
        color = COLORS.get(toktype, COLORS[_TEXT])
        if toktext:             # send text
            txt = Detag(toktext)
            if color is None:    txt = PLAIN % txt
            elif color=='black': txt = BOLD % txt
            else:                txt = CBOLD % (color,txt)
            self.out.write(txt)

Detag = lambda s: \
    s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

if __name__=='__main__':
    parsed = ParsePython(sys.stdin.read())
    print '<pre>'
    print parsed.toHTML()
    print '</pre>'



