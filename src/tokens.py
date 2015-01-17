import lib.ply.lex as lex
from pprint import pprint

tokens = (
    'MAGIC_NUMBER',
    'DOT',
    'NAMESPACE',
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'IDENTIFIER',
    )


t_MAGIC_NUMBER = r'42'
t_DOT = r'\.'
t_OPEN_BRACKET = r'{'
t_CLOSE_BRACKET = r'}'


def t_NAMESPACE(t):
    r'namespace'

    return t


# Quite restrictive
def t_IDENTIFIER(t):
    r'[A-Za-z]+'

    return t
    
    

# # A regular expression rule with some action code
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
