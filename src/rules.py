import sys



def regurgitate(p):
    return ''.join({ p[i] for i in range(1, len(p)) })


### Productions

def p_everything(p):
    '''everything : namespace_decl
    '''
    p[0] = p[1]


def p_qualified_identifier(p):
    '''qualified_identifier : IDENTIFIER
                            | qualified_identifier DOT IDENTIFIER
    '''
    p[0] = regurgitate(p)


def p_namespace_decl(p):
    '''namespace_decl : NAMESPACE qualified_identifier namespace_body'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_namespace_body(p):
    '''namespace_body : OPEN_BRACKET CLOSE_BRACKET'''
    p[0] = p[1] + ' ' + p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
