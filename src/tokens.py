import lib.ply.lex as lex
from pprint import pprint

tokens = [
    'IDENTIFIER',

    # Symbols
    'CLOSING_BRACE',
    'CLOSING_BRACKET',
    'CLOSING_PARENTHESIS',
    'COLON',
    'COMMA',
    'DOT',
    'EQUALS',
    'GT',
    'LT',
    'OPENING_BRACE',
    'OPENING_BRACKET',
    'OPENING_PARENTHESIS',
    'QUESTION_MARK',
    'SEMICOLON',    
    ]



t_CLOSING_BRACE = r'}'
t_CLOSING_BRACKET = r'\]'
t_CLOSING_PARENTHESIS = r'\)'
t_COLON = r':'
t_COMMA = r','
t_DOT = r'\.'
t_EQUALS = r'='
t_GT = r'>'
t_LT = r'<'
t_OPENING_BRACE = r'{'
t_OPENING_BRACKET = r'\['
t_OPENING_PARENTHESIS = r'\('
t_QUESTION_MARK = r'\?'
t_SEMICOLON = r';'


reserved_words = {
    'abstract' : 'ABSTRACT',
    'alias' : 'ALIAS',
    'as' : 'AS',
    'base' : 'BOOL',
    'break' : 'BREAK',
    'byte' : 'BYTE',
    'case' : 'CASE',
    'catch' : 'CATCH',
    'char' : 'CHAR',
    'checked' : 'CHECKED',
    'class' : 'CLASS',
    'const' : 'CONST',
    'continue' : 'CONTINUE',
    'decimal' : 'DECIMAL',
    'default' : 'DEFAULT',
    'delegate' : 'DELEGATE',
    'do' : 'DO',
    'double' : 'DOUBLE',
    'dynamic' : 'DYNAMIC',
    'else' : 'ELSE',
    'enum' : 'ENUM',
    'event' : 'EVENT',
    'explicit' : 'EXPLICIT',
    'extern' : 'EXTERN',
    'false' : 'FALSE',
    'finally' : 'FINALLY',
    'fixed' : 'FIXED',
    'float' : 'FLOAT',
    'for' : 'FOR',
    'foreach' : 'FOREACH',
    'goto' : 'GOTO',
    'if' : 'IF',
    'implicit' : 'IMPLICIT',
    'in' : 'IN',
    'int' : 'INT',
    'interface' : 'INTERFACE',
    'internal' : 'INTERNAL',
    'is' : 'IS',
    'lock' : 'LOCK',
    'long' : 'LONG',
    'namespace' : 'NAMESPACE',
    'new' : 'NEW',
    'null' : 'NULL',
    'object' : 'OBJECT',
    'operator' : 'OPERATOR',
    'out' : 'OUT',
    'override' : 'OVERRIDE',
    'params' : 'PARAMS',
    'partial' : 'PARTIAL',
    'private' : 'PRIVATE',
    'protected' : 'PROTECTED',
    'public' : 'PUBLIC',
    'readonly' : 'READONLY',
    'ref' : 'REF',
    'return' : 'RETURN',
    'sbyte' : 'SBYTE',
    'sealed' : 'SEALED',
    'short' : 'SHORT',
    'sizeof' : 'SIZEOF',
    'stackalloc' : 'STACKALLOC',
    'static' : 'STATIC',
    'string' : 'STRING',
    'struct' : 'STRUCT',
    'switch' : 'SWITCH',
    'this' : 'THIS',
    'throw' : 'THROW',
    'true' : 'TRUE',
    'try' : 'TRY',
    'typeof' : 'TYPEOF',
    'uint' : 'UINT',
    'ulong' : 'ULONG',
    'unchecked' : 'UNCHECKED',
    'unsafe' : 'UNSAFE',
    'ushort' : 'USHORT',
    'using' : 'USING',
    'virtual' : 'VIRTUAL',
    'void' : 'VOID',
    'volatile' : 'VOLATILE',
    'where' : 'WHERE',
    'while' : 'WHILE',
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
