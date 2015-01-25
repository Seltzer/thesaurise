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


def p_start(p):
    '''start : compilation_unit'''
    p[0] = p[1]


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
def p_type(p):
    '''type : value_type
    | ref_type
    | type_param'''

    p[0] = p[1]

def p_value_type(p):
    '''value_type : struct_type
    | enum_type'''

    p[0] = p[1]

def p_struct_type(p):
    '''struct_type : type_name
    | simple_type
    | nullable_type'''

    p[0] = p[1]

def p_simple_type(p):
    '''simple_type : numeric_type
    | floating_point_type
    | DECIMAL'''

    p[0] = p[1]

def p_numeric_type(p):
    '''numeric_type : integral_type
    | floating_point_type
    | DECIMAL'''

    p[0] = p[1]
    
def p_integral_type(p):
    '''integral_type : SBYTE
    | BYTE
    | SHORT
    | USHORT
    | INT
    | UINT
    | LONG
    | CHAR'''

    p[0] = p[1]


def p_floating_point_type(p):
    '''floating_point_type : FLOAT
    | DOUBLE'''

    p[0] = p[1]

def p_nullable_type(p):
    '''nullable_type : non_nullable_value_type QUESTION_MARK'''

    p[0] = regurgitate(p)

def p_non_nullable_value_type(p):
    '''non_nullable_value_type : type'''

    p[0] = p[1]

def p_enum_type(p):
    '''enum_type : type_name'''

def p_ref_type(p):
    '''ref_type : class_type
    | interface_type
    | array_type
    | delegate_type'''

    p[0] = p[1]
    
def p_class_type(p):
    '''class_type : type_name
    | OBJECT
    | DYNAMIC
    | STRING'''

    p[0] = p[1]

def p_interface_type(p):
    '''interface_type : type_name'''
    p[0] = p[1]

def p_rank_specifiers(p):
    '''rank_specifiers : rank_specifier
    | rank_specifiers rank_specifier'''

    p[0] = regurgitate(p)

def p_rank_specifier(p):
    '''rank_specifier : OPENING_BRACKET dim_separators_opt CLOSING_BRACKET'''

    p[0] = regurgitate(p)

def p_dim_separators(p):
    '''dim_separators : COMMA
    | dim_separators COMMA'''

    p[0] = regurgitate(p)

def p_dim_separators_opt(p):
    '''dim_separators_opt : dim_separators
    | empty'''

    p[0] = regurgitate(p)

def p_delegate_type(p):
    '''delegate_type : type_name'''

    p[0] = p[1]

def p_type_arg_list(p):
    '''type_arg_list : LT type_args GT'''

    p[0] = regurgitate(p)
    
def p_type_arg_list_opt(p):
    '''type_arg_list_opt : type_arg_list
    | empty'''

    p[0] = regurgitate(p)

def p_type_args(p):
    '''type_args : type_arg
    | type_args COMMA type_arg'''

    p[0] = regurgitate(p)

def p_type_arg(p):
    '''type_arg : type'''
    p[0] = p[1]
    
def p_type_param(p):
    '''type_param : IDENTIFIER'''
    p[0] = p[1]
    

### 2.3
def p_var_ref(p):
    '''var_ref : expression'''
    p[0] = p[1]


def p_expression(p):
    '''expression : empty'''
    p[0] = regurgitate(p)

### Other



def p_partial_opt(p):
    '''partial_opt : PARTIAL
    | empty'''

    p[0] = regurgitate(p)


### 2.6
def p_compilation_unit(p):
    '''compilation_unit : extern_alias_directives_opt using_directives_opt namespace_member_decls_opt'''
    p[0] = regurgitate(p)

def p_namespace_decl(p):
    '''namespace_decl : NAMESPACE qualified_identifier namespace_body semicolon_opt'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4] + '\n'

def p_qualified_identifier(p):
    '''qualified_identifier : IDENTIFIER
                            | qualified_identifier DOT IDENTIFIER
    '''
    p[0] = p[1] if len(p) == 2 else p[1] + '.' + p[3]

def p_namespace_body(p):
    '''namespace_body : OPENING_BRACE extern_alias_directives_opt using_directives_opt namespace_member_decls_opt CLOSING_BRACE'''
    p[0] = '\n{\n' + regurgitate(p, 2, len(p) - 1) + '\n}'

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


def p_using_namespace_directive(p):
    '''using_directive : USING namespace_name SEMICOLON'''

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

def p_namespace_member_decl(p):
    '''namespace_member_decl : namespace_decl
    | type_decl'''

    p[0] = p[1]

def p_namespace_member_decls(p):
    '''namespace_member_decls : namespace_member_decl
    | namespace_member_decls namespace_member_decl'''

    p[0] = regurgitate(p)

def p_namespace_member_decls_opt(p):
    '''namespace_member_decls_opt : namespace_member_decls
    | empty'''

    p[0] = regurgitate(p)

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
    '''class_decl : class_modifiers_opt partial_opt CLASS IDENTIFIER type_param_list_opt class_base_opt type_param_constraints_clauses_opt class_body semicolon_opt'''

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

def p_type_param_list_opt(p):
    '''type_param_list_opt : type_param_list
    | empty'''

    p[0] = regurgitate(p)

def p_type_param_list(p):
    '''type_param_list : LT type_params GT'''

    p[0] = '<' + p[2] + '>'

def p_type_params(p):
    '''type_params : attributes_opt type_param
    | type_params COMMA attributes_opt type_param'''

    p[0] = regurgitate(p)

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


### 2.9 (Arrays)
def p_array_type(p):
    '''array_type : non_array_type rank_specifiers'''
    p[0] = regurgitate(p)

def p_non_array_type(p):
    '''non_array_type : type'''

def p_array_initialiser(p):
    '''array_initialiser : OPENING_BRACE var_initialiser_list_opt CLOSING_BRACE
    | OPENING_BRACE var_initialiser_list COMMA CLOSING_BRACE'''

    p[0] = regurgitate(p)

def p_var_initialiser(p):
    '''var_initialiser : expression
    | array_initialiser'''

    p[0] = p[1]

def p_var_initialiser_list(p):
    '''var_initialiser_list : var_initialiser
    | var_initialiser_list COMMA var_initialiser'''

    p[0] = regurgitate(p)

def p_var_initialiser_list_opt(p):
    '''var_initialiser_list_opt : var_initialiser_list
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
