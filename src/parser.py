import sys, os

from subprocess import Popen, PIPE
from lib.ply import yacc,lex
from src.tokens import *
from src.rules import *

def generateParser():
    print('Generating parser')

    #logger = yacc.NullLogger()
    logger = yacc.PlyLogger(sys.stderr)
    
    yacc.yacc(debug=logger, errorlog=logger)


def parse(filename):
    print('About to parse ' + filename)
    
    f = open(filename, "r")
    data = f.read();
    f.close();
    
    return yacc.parse(data, lexer=lex.lex(nowarn=1))



