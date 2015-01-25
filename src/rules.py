import sys



def regurgitate(p, start = 1, end = None):
    end = len(p) if end is None else end
    return ''.join({ p[i] for i in range(start, end) })

def regurgitate_inv(p, start = 1, end = None):
    end = len(p) if end is None else end
    return ''.join({ p[i] for i in reversed(range(start, end)) })


def wrap_in_brackets(str):
    return 'OPENING_BRACE ' + str + 'CLOSING_BRACE'



### Productions



def p_compilation_unit(p):
    '''compilation_unit : extern_alias_directives_opt using_directives_opt namespace_member_decls_opt'''
    p[0] = regurgitate(p)


### 2.1
def p_namespace_name(p):
    '''namespace_name : namespace_or_type_name'''
    p[0] = p[1]

def p_type_name(p):
    '''type_name : namespace_or_type_name'''
    p[0] = p[1]

def p_namespace_or_type_name(p):
    '''namespace_or_type_name : IDENTIFIER type_arg_list_opt
    | namespace_or_type_name DOT IDENTIFIER type_arg_list_opt
    | qualified_alias_member'''

    p[0] = regurgitate(p)


### 2.2
def p_class_type(p):
    '''class_type : type_name
    | OBJECT
    | DYNAMIC
    | STRING'''

    p[0] = p[1]

def p_interface_type(p):
    '''interface_type : type_name'''
    p[0] = p[1]

### Temporary
def p_type_arg_list(p):
    '''type_arg_list : LT GT'''
    p[0] = p[1] + p[2]

def p_type_arg_list_opt(p):
    '''type_arg_list_opt : type_arg_list
    | empty'''

    p[0] = regurgitate(p)

### Other

def p_qualified_identifier(p):
    '''qualified_identifier : IDENTIFIER
                            | qualified_identifier DOT IDENTIFIER
    '''
    p[0] = p[1] if len(p) == 2 else p[1] + '.' + p[3]


def p_partial_opt(p):
    '''partial_opt : PARTIAL
    | empty'''

    p[0] = regurgitate(p)


### 2.6

def p_namespace_decl(p):
    '''namespace_decl : NAMESPACE qualified_identifier namespace_body semicolon_opt'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4] + '\n'


## namespace_body
def p_namespace_body(p):
    '''namespace_body : OPENING_BRACE extern_alias_directives_opt using_directives_opt namespace_member_decls_opt CLOSING_BRACE'''
    p[0] = '\n{\n' + regurgitate(p, 2, len(p) - 1) + '\n}'


## extern
def p_extern_alias_directive(p):
    '''extern_alias_directive : EXTERN ALIAS IDENTIFIER SEMICOLON'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ';'

def p_extern_alias_directives(p):
    '''extern_alias_directives : extern_alias_directive
                               | extern_alias_directives extern_alias_directive
    '''

    p[0] = regurgitate(p)

def p_extern_alias_directives_opt(p):
    '''extern_alias_directives_opt : extern_alias_directives
    | empty'''

    p[0] = '' if len(p) == 1 else regurgitate(p) + '\n'


## using
def p_using_namespace_directive(p):
    '''using_directive : USING qualified_identifier SEMICOLON'''

#    p[0] = 'using ' + regurgitate(p, 2)
    p[0] = 'using ' + p[2] + ';\n'

def p_using_alias_directive(p):
    '''using_directive : USING IDENTIFIER EQUALS namespace_or_type_name SEMICOLON'''

    p[0] = regurgitate(p)


def p_using_directives(p):
    '''using_directives : using_directive
                        | using_directives using_directive
    '''

    p[0] = regurgitate(p)

def p_using_directives_opt(p):
    '''using_directives_opt : using_directives
    | empty
    '''

    p[0] = '' if len(p) == 1 else regurgitate(p) + '\n'





## namespace_member
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


## type_decl
def p_type_decl(p):
    '''type_decl : class_decl
                  | struct_decl
                  | interface_decl
                  | enum_decl
                  | delegate_decl
    '''

    p[0] = p[1]

def p_qualified_alias_member(p):
    '''qualified_alias_member : IDENTIFIER COLON COLON IDENTIFIER type_arg_list_opt'''

    p[0] = regurgitate(p)
 


def p_struct_decl(p):
    '''struct_decl : STRUCT IDENTIFIER OPENING_BRACE CLOSING_BRACE'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]
    
def p_interface_decl(p):
    '''interface_decl : INTERFACE IDENTIFIER OPENING_BRACE CLOSING_BRACE'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

    
def p_enum_decl(p):
    '''enum_decl : ENUM IDENTIFIER OPENING_BRACE CLOSING_BRACE '''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

    
def p_delegate_decl(p):
    '''delegate_decl : DELEGATE IDENTIFIER OPENING_BRACE CLOSING_BRACE'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]



### 2.7 Classes
def p_class_decl(p):
    '''class_decl : class_modifiers_opt partial_opt CLASS IDENTIFIER class_base_opt type_param_constraints_clauses_opt class_body semicolon_opt'''

    p[0] = regurgitate(p)

def p_class_modifiers_opt(p):
    '''class_modifiers_opt : class_modifiers
    | empty
    '''

    p[0] = regurgitate(p)

def p_class_modifiers(p):
    '''class_modifiers : class_modifier
    | class_modifiers class_modifier'''

    p[0] = p[1] if len(p) == 2 else p[1] + ' ' + p[2]


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

def p_type_param_list(p):
    '''type_param_list : LT type_params GT'''

    p[0] = '<' + p[2] + '>'

def p_type_params(p):
    '''type_params : attributes_opt type_param
    | type_params COMMA attributes_opt type_param'''

    p[0] = regurgitate(p)

def p_type_param(p):
    '''type_param : IDENTIFIER'''

def p_class_base_opt(p):
    '''class_base_opt : COLON class_type
    | COLON interface_type_list
    | COLON class_type COMMA interface_type_list
    | empty'''

    p[0] = regurgitate(p)

    
def p_interface_type_list(p):
    '''interface_type_list : interface_type
    | interface_type_list COMMA interface_type'''
    p[0] = regurgitate(p)

def p_type_parameter_constraints_clause(p):
    '''type_param_constraints_clause : WHERE type_param COLON type_param_constraints'''

    p[0] = regurgitate(p)

def p_type_param_constraints_clauses(p):
    '''type_param_constraints_clauses : type_param_constraints_clause
    | type_param_constraints_clauses type_param_constraints_clause'''

    p[0] = regurgitate(p)

def p_type_param_constraints_clauses_opt(p):
    '''type_param_constraints_clauses_opt : type_param_constraints_clauses
    | empty'''

    p[0] = regurgitate(p)

def p_type_param_constraints(p):
    '''type_param_constraints : primary_constraint
    | secondary_constraints
    | ctor_constraint
    | primary_constraint COMMA secondary_constraints
    | primary_constraint COMMA ctor_constraint
    | secondary_constraints COMMA ctor_constraint
    | primary_constraint COMMA secondary_constraints COMMA ctor_constraint'''

    p[0] = regurgitate(p)

def p_primary_constraint(p):
    '''primary_constraint : class_type
    | CLASS
    | STRUCT'''

    p[0] = p[1]

def p_secondary_constraints(p):
    '''secondary_constraints : interface_type
    | type_param
    | secondary_constraints COMMA interface_type
    | secondary_constraints COMMA type_param'''

    p[0] = regurgitate(p)

def p_ctor_constraint(p):
    '''ctor_constraint : NEW OPENING_PARENTHESIS CLOSING_PARENTHESIS'''

    p[0] = regurgitate(p)
    
def p_class_body(p):
    '''class_body : OPENING_BRACE class_member_decls_opt CLOSING_BRACE'''

    p[0] = regurgitate(p)

def p_class_member_decl(p):
    '''class_member_decl : CONST'''

    p[0] = p[1]

def p_class_member_decls(p):
    '''class_member_decls : class_member_decl
    | class_member_decls class_member_decl'''

    p[0] = regurgitate(p)

def p_class_member_decls_opt(p):
    '''class_member_decls_opt : class_member_decls
    | empty'''

    p[0] = regurgitate(p)


### Other
def p_attributes_opt(p):
    '''attributes_opt : empty'''

    p[0] = ''

## semicolon_opt
def p_semicolon_opt(p):
    '''semicolon_opt : SEMICOLON
    | empty'''

    p[0] = regurgitate(p)


## empty
def p_empty(p):
    'empty :'

    p[0] = ''
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
