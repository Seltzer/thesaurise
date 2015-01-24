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
def p_namespace_body(p):
    '''namespace_body : OPEN_BRACKET extern_alias_directives_opt using_directives_opt namespace_member_decls_opt CLOSE_BRACKET'''
    p[0] = regurgitate(p)


## extern
def p_extern_alias_directive(p):
    '''extern_alias_directive : EXTERN ALIAS IDENTIFIER'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_extern_alias_directives(p):
    '''extern_alias_directives : extern_alias_directive
                               | extern_alias_directives extern_alias_directive
    '''

    p[0] = regurgitate(p)

def p_extern_alias_directives_opt(p):
    '''extern_alias_directives_opt : extern_alias_directives
    | empty'''

    p[0] = regurgitate(p)

## using
def p_using_directive(p):
    '''using_directive : USING'''

    p[0] = p[1]

def p_using_directives(p):
    '''using_directives : using_directive
                        | using_directives using_directive
    '''

    p[0] = regurgitate(p)

def p_using_directives_opt(p):
    '''using_directives_opt : using_directives
    | empty
    '''

    p[0] = regurgitate(p)

# namespace_member
def p_namespace_member_decl(p):
    '''namespace_member_decl : namespace_decl
                             | type_decl
    '''

    p[0] = p[1]

def p_namespace_member_decls(p):
    '''namespace_member_decls : namespace_member_decl
                              | namespace_member_decls namespace_member_decl
    '''

    p[0] = regurgitate(p)


def p_namespace_member_decls_opt(p):
    '''namespace_member_decls_opt : namespace_member_decls
    | empty'''

    p[0] = regurgitate(p)


# type_decl
def p_type_decl(p):
    '''type_decl : class_decl
                  | struct_decl
                  | interface_decl
                  | enum_decl
                  | delegate_decl
    '''

    p[0] = p[1]
    
def p_class_decl(p):
    '''class_decl : class_modifiers_opt CLASS IDENTIFIER OPEN_BRACKET CLOSE_BRACKET'''

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


# Class modifiers
def p_class_modifiers_opt(p):
    '''class_modifiers_opt : class_modifiers
    | empty
    '''

    p[0] = regurgitate(p)

def p_class_modifiers(p):
    '''class_modifiers : class_modifier
    | class_modifiers class_modifier'''

    p[0] = regurgitate(p)


def p_class_modifier(p):
    '''class_modifier : PUBLIC
    | PROTECTED
    | PRIVATE
    | INTERNAL
    | SEALED
    | ABSTRACT
    | STATIC
    | NEW
    '''

    p[0] = p[1]


def p_empty(p):
    'empty :'

    p[0] = ''
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
