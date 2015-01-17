import sys



def regurgitate(p):
    return ''.join({ p[i] for i in range(1, len(p)) })

def wrap_in_brackets(str):
    return 'OPEN_BRACKET ' + str + 'CLOSE_BRACKET'



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

## namespace_body
def p_namespace_body_empty(p):
    '''namespace_body : OPEN_BRACKET CLOSE_BRACKET'''
    p[0] = p[1] + ' ' + p[2]

def p_namespace_body_just_externs(p):
    '''namespace_body : OPEN_BRACKET extern_alias_directives CLOSE_BRACKET'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_namespace_body_just_usings(p):
    '''namespace_body : OPEN_BRACKET using_directives CLOSE_BRACKET'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_namespace_body_just_ns_members(p):
    '''namespace_body : OPEN_BRACKET namespace_member_decls CLOSE_BRACKET'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]


## extern
def p_extern_alias_directives(p):
    '''extern_alias_directives : extern_alias_directive
                               | extern_alias_directives extern_alias_directive
    '''

    p[0] = regurgitate(p)
        
def p_extern_alias_directive(p):
    '''extern_alias_directive : EXTERN ALIAS IDENTIFIER'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]



## using
def p_using_directives(p):
    '''using_directives : using_directive
                        | using_directives using_directive
    '''

    p[0] = regurgitate(p)

def p_using_directive(p):
    '''using_directive : USING'''

    p[0] = p[1]



def p_namespace_member_decls(p):
    '''namespace_member_decls : namespace_member_decl
                              | namespace_member_decls namespace_member_decl
    '''

    p[0] = regurgitate(p)


def p_namespace_member_decl(p):
    '''namespace_member_decl : namespace_decl
                             | type_decl
    '''

    p[0] = p[1]


def p_type_decl(p):
    '''type_decl : class_decl
                  | struct_decl
                  | interface_decl
                  | enum_decl
                  | delegate_decl
    '''

    p[0] = p[1]
    
def p_class_decl(p):
    '''class_decl : CLASS IDENTIFIER OPEN_BRACKET CLOSE_BRACKET'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

def p_struct_decl(p):
    '''struct_decl : STRUCT IDENTIFIER OPEN_BRACKET CLOSE_BRACKET'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]
    
def p_interface_decl(p):
    '''interface_decl : INTERFACE IDENTIFIER OPEN_BRACKET CLOSE_BRACKET'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

    
def p_enum_decl(p):
    '''enum_decl : ENUM IDENTIFIER OPEN_BRACKET CLOSE_BRACKET '''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

    
def p_delegate_decl(p):
    '''delegate_decl : DELEGATE IDENTIFIER OPEN_BRACKET CLOSE_BRACKET'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

    


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
