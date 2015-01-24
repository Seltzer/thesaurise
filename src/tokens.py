import lib.ply.lex as lex
from pprint import pprint

tokens = [
    'IDENTIFIER',

    # Symbols
    'OPEN_BRACKET',
    'CLOSE_BRACKET',
    'SEMICOLON',
    'DOT',
    'EQUALS',
    'GT',
    'LT',
    'COLON'
    ]


t_DOT = r'\.'
t_OPEN_BRACKET = r'{'
t_CLOSE_BRACKET = r'}'
t_SEMICOLON = r';'
t_EQUALS = r'='
t_GT = r'>'
t_LT = r'<'
t_COLON = r':'

reserved_words = {
    'abstract' : 'ABSTRACT',
    'alias' : 'ALIAS',
    'class' : 'CLASS',
    'delegate' : 'DELEGATE',
    'enum' : 'ENUM',
    'extern' : 'EXTERN',
    'interface' : 'INTERFACE',
    'internal' : 'INTERNAL',
    'namespace' : 'NAMESPACE',
    'new' : 'NEW',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'public' : 'PUBLIC',
    'sealed' : 'SEALED',
    'static' : 'STATIC',
    'struct' : 'STRUCT',
    'using' : 'USING',
    }

tokens += list(reserved_words.values())


# Quite restrictive at this stage
def t_IDENTIFIER(t):
    r'[A-Za-z]+'

    t.type = reserved_words.get(t.value,'IDENTIFIER')

    return t


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
