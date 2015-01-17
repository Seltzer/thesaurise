import sys, os

from subprocess import Popen, PIPE
from lib.ply import yacc,lex
from src.tokens import *
from src.rules import *


def parse(filename):
    logger = yacc.NullLogger()
    
    yacc.yacc(debug=logger, errorlog=logger)

    filename = "tests/test.cs"
    f = open(filename, "r")
    data = f.read();
    f.close();
    
    return yacc.parse(data, lexer=lex.lex(nowarn=1))



