import lib.ply.lex as lex
from pprint import pprint

tokens = (
    'IDENTIFIER',
    'MAGIC_NUMBER',
#    'NOTHING',

    # Keywords
    'NAMESPACE',
    'USING',
    'EXTERN',
    'ALIAS',
    'CLASS',
    'STRUCT',
    'INTERFACE',
    'ENUM',
    'DELEGATE',

    # Symbols
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'DOT',    
    )


t_MAGIC_NUMBER = r'42'
t_DOT = r'\.'
t_OPEN_BRACKET = r'{'
t_CLOSE_BRACKET = r'}'


def t_NAMESPACE(t):
    r'namespace'

    return t


def t_USING(t):
    r'using'

    return t;

def t_EXTERN(t):
    r'extern'

    return t;

def t_ALIAS(t):
    r'alias'

    return t;

def t_CLASS(t):
    r'class'

    return t;

def t_STRUCT(t):
    r'struct'

    return t;

def t_INTERFACE(t):
    r'interface'

    return t;

def t_ENUM(t):
    r'enum'

    return t;

def t_DELEGATE(t):
    r'delegate'

    return t;


# Quite restrictive
def t_IDENTIFIER(t):
    r'[A-Za-z]+'

    return t
    
# def t_NOTHING(t):
#     r''

#     return t

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
