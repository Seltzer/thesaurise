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
    '''namespace_or_type_name : IDENTIFIER type_argument_list_opt
    | namespace_or_type_name DOT IDENTIFIER type_argument_list_opt
    | qualified_alias_member'''

    p[0] = regurgitate(p)


### 2.2
def p_type(p):
    '''type : value_type
    | reference_type
    | type_parameter'''

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

def p_reference_type(p):
    '''reference_type : class_type
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

def p_type_argument_list(p):
    '''type_argument_list : LT type_arguments GT'''

    p[0] = regurgitate(p)
    
def p_type_argument_list_opt(p):
    '''type_argument_list_opt : type_argument_list
    | empty'''

    p[0] = regurgitate(p)

def p_type_arguments(p):
    '''type_arguments : type_argument
    | type_arguments COMMA type_argument'''

    p[0] = regurgitate(p)

def p_type_argument(p):
    '''type_argument : type'''
    p[0] = p[1]
    
def p_type_parameter(p):
    '''type_parameter : IDENTIFIER'''
    p[0] = p[1]
    

### 2.3
def p_variable_ref(p):
    '''variable_reference : expression'''
    p[0] = p[1]


def p_expression(p):
    '''expression : empty'''
    p[0] = regurgitate(p)

### Other



def p_partial_opt(p):
    '''partial_opt : PARTIAL
    | empty'''

    p[0] = regurgitate(p)



### 2.4 Expressions
def p_argument_list(p):
    '''argument_list : argument
    | argument_list COMMA argument'''

    p[0] = regurgitate(p)

def p_argument(p):
    '''argument : argument_name_opt argument_value'''

    p[0] = regurgitate(p)


def p_argument_name(p):
    '''argument_name : IDENTIFIER COLON'''
    p[0] = p[1] + ': '

def p_argument_name_opt(p):
    '''argument_name_opt : argument_name
    | empty'''

    p[0] = regurgitate(p)

def p_argument_value(p):
    '''argument_value : expression
    | REF variable_reference
    | OUT variable_reference'''

    p[0] = regurgitate(p)

# def p_primary_expression(p):
#     '''primary_expression : primary_no_array_creation_expression
#     | array_creation_expression'''

#     p[0] = regurgitate(p)


# def p_primary_no_array_creation_expression(p):
#     '''primary_no_array_creation_expression : literal


def p_simple_name(p):
    '''simple_name : IDENTIFIER type_argument_list'''

    p[0] = regurgitate(p)

def p_parenthesized_expr(p):
    '''parenthesized_expression : OPENING_PARENTHESIS expression CLOSING_PARENTHESIS'''
    p[0] = regurgitate(p)

#def p_member_access
    
def p_predefined_type(p):
    '''predefined_type : BOOL
    | BYTE
    | CHAR
    | DECIMAL
    | DOUBLE
    | FLOAT
    | INT
    | LONG
    | OBJECT
    | SBYTE
    | SHORT
    | STRING
    | UINT
    | ULONG
    | USHORT'''

    p[0] = p[1]

# def p_invocation_expression(p):
#     '''invocation_expression : primary_expression OPENING_PARENTHESIS argument_list_opt CLOSING_PARENTHESIS'''

#     p[0] = regurgitate(p)

# def p_element_access(p):
#     '''element_access : primary_no_array_creation_expression OPENING_BRACKET argument_list CLOSING_BRACKET'''

#     p[0] = regurgitate(p)



def p_this_access(p):
    '''this_access : THIS'''
    p[0] = p[1]


# def p_base_access(p):
#     '''base_access : BASE DOT IDENTIFIER
#     | BASE OPENING_BRACKET argument_list CLOSING_BRACKET'''
#     p[0] = regurgitate(p)


#def p_opst_increment_expression(p):
    








### 2.6
def p_compilation_unit(p):
    '''compilation_unit : extern_alias_directives_opt using_directives_opt namespace_member_declarations_opt'''
    p[0] = regurgitate(p)

def p_namespace_declaration(p):
    '''namespace_declaration : NAMESPACE qualified_identifier namespace_body semicolon_opt'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4] + '\n'

def p_qualified_identifier(p):
    '''qualified_identifier : IDENTIFIER
                            | qualified_identifier DOT IDENTIFIER
    '''
    p[0] = p[1] if len(p) == 2 else p[1] + '.' + p[3]

def p_namespace_body(p):
    '''namespace_body : OPENING_BRACE extern_alias_directives_opt using_directives_opt namespace_member_declarations_opt CLOSING_BRACE'''
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

def p_namespace_member_declaration(p):
    '''namespace_member_declaration : namespace_declaration
    | type_declaration'''

    p[0] = p[1]

def p_namespace_member_declarations(p):
    '''namespace_member_declarations : namespace_member_declaration
    | namespace_member_declarations namespace_member_declaration'''

    p[0] = regurgitate(p)

def p_namespace_member_declarations_opt(p):
    '''namespace_member_declarations_opt : namespace_member_declarations
    | empty'''

    p[0] = regurgitate(p)

def p_type_declaration(p):
    '''type_declaration : class_declaration
    | struct_declaration
    | interface_declaration
    | enum_declaration
    | delegate_declaration
    '''

    p[0] = p[1]

def p_qualified_alias_member(p):
    '''qualified_alias_member : IDENTIFIER COLON COLON IDENTIFIER type_argument_list_opt'''

    p[0] = regurgitate(p)
    
def p_interface_declaration(p):
    '''interface_declaration : INTERFACE IDENTIFIER OPENING_BRACE CLOSING_BRACE'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]


### 2.7 Classes
def p_class_declaration(p):
    '''class_declaration : class_modifiers_opt partial_opt CLASS IDENTIFIER type_parameter_list_opt class_base_opt type_parameter_constraints_clauses_opt class_body semicolon_opt'''

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

def p_type_parameter_list_opt(p):
    '''type_parameter_list_opt : type_parameter_list
    | empty'''

    p[0] = regurgitate(p)

def p_type_parameter_list(p):
    '''type_parameter_list : LT type_parameters GT'''

    p[0] = '<' + p[2] + '>'

def p_type_parameters(p):
    '''type_parameters : attributes_opt type_parameter
    | type_parameters COMMA attributes_opt type_parameter'''

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
    '''type_parameter_constraints_clause : WHERE type_parameter COLON type_parameter_constraints'''

    p[0] = regurgitate(p)

def p_type_parameter_constraints_clauses(p):
    '''type_parameter_constraints_clauses : type_parameter_constraints_clause
    | type_parameter_constraints_clauses type_parameter_constraints_clause'''

    p[0] = regurgitate(p)

def p_type_parameter_constraints_clauses_opt(p):
    '''type_parameter_constraints_clauses_opt : type_parameter_constraints_clauses
    | empty'''

    p[0] = regurgitate(p)

def p_type_parameter_constraints(p):
    '''type_parameter_constraints : primary_constraint
    | secondary_constraints
    | constructor_constraint
    | primary_constraint COMMA secondary_constraints
    | primary_constraint COMMA constructor_constraint
    | secondary_constraints COMMA constructor_constraint
    | primary_constraint COMMA secondary_constraints COMMA constructor_constraint'''

    p[0] = regurgitate(p)

def p_primary_constraint(p):
    '''primary_constraint : class_type
    | CLASS
    | STRUCT'''

    p[0] = p[1]

def p_secondary_constraints(p):
    '''secondary_constraints : interface_type
    | type_parameter
    | secondary_constraints COMMA interface_type
    | secondary_constraints COMMA type_parameter'''

    p[0] = regurgitate(p)

def p_constructor_constraint(p):
    '''constructor_constraint : NEW OPENING_PARENTHESIS CLOSING_PARENTHESIS'''

    p[0] = regurgitate(p)
    
def p_class_body(p):
    '''class_body : OPENING_BRACE class_member_declarations_opt CLOSING_BRACE'''

    p[0] = regurgitate(p)

def p_class_member_declaration(p):
    '''class_member_declaration : CONST'''

    p[0] = p[1]

def p_class_member_declarations(p):
    '''class_member_declarations : class_member_declaration
    | class_member_declarations class_member_declaration'''

    p[0] = regurgitate(p)

def p_class_member_declarations_opt(p):
    '''class_member_declarations_opt : class_member_declarations
    | empty'''

    p[0] = regurgitate(p)


# def p_constant_modifiers(p):
#     '''constant_modifiers : constant_modifier
#     | constant_modifiers constant_modifier'''
#     p[0] = regurgitate(p)

# def p_constant_modifier(p):
#     '''constant_modifier : NEW
#     | PUBLIC
#     | PROTECTED
#     | INTERNAL
#     | PRIVATE'''
#     p[0] = p[1]

# def p_constant_declarators(p):
#     '''constant_declarators : constant_declarator
#     | constant_declarators constant_declarator'''
#     p[0] = regurgitate(p)
    
# def p_constant_declarator(p):
#     '''constant_declarator : IDENTIFIER EQUALS constant_expression'''

#     p[0] = regurgitate(p)

# def p_field_declaration(p):
#     '''field_declaration : attributes_opt field_modifiers_opt type variable_declarators SEMICOLON'''
#     p[0] = regurgitate(p)

# def p_field_modifiers(p):
#     '''field_modifiers : field_modifier
#     | field_modifiers field_modifier'''
#     p[0] = regurgitate(p)


# def p_field_modifier(p):
#     '''field_modifier : NEW
#     | PUBLIC
#     | PROTECTED
#     | INTERNAL
#     | PRIVATE
#     | STATIC
#     | READONLY
#     | VOLATILE'''

#     p[0] = p[1]

# def p_variable_declarators(p):
#     '''variable_declarator : variable_declarator
#     | variable_declarators variable_declarator'''
#     p[0] = regurgitate(p)

# def p_variable_declarator(p):
#     '''variable_declarator : IDENTIFIER
#     | IDENTIFIER EQUALS variable_initialiser'''
#     p[0] = regurgitate(p)

# def p_variable_initialiser(p):
#     '''variable_initialiser : expression
#     | array_initialiser'''
#     p[0] = p[1]

# def p_method_declaration(p):
#     '''method_declaration : method_header method_body'''
#     p[0] = regurgitate(p)


# # TODO: This definitely ain't gonna work!!!
# def p_method_header(p):
#     '''method_header : attributes_opt method_modifiers_opt
#     PARTIAL_OPT return_type member_name type_parameter_list_opt
#     OPENING_PARENTHESIS formal_parameter_list_opt CLOSING_PARENTHESIS
#     type_parameter_constraints_clauses_opt'''
#     p[0] = regurgitate(p)

# def p_method_modifiers(p):
#     '''method_modifiers : method_modifier
#     | method_modifiers method_modifier'''
#     p[0] = regurgitate(p)

# def p_method_modifier(p):
#     '''method_modifier : NEW
#     | PUBLIC
#     | PROTECTED
#     | INTERNAL
#     | PRIVATE
#     | STATIC
#     | VIRTUAL
#     | SEALED
#     | OVERRIDE
#     | ABSTRACT
#     | EXTERN'''
#     p[0] = p[1]

# def p_return_type(p):
#     '''return_type : type
#     | VOID'''
#     p[0] = p[1]

# def p_member_name(p):
#     '''member_name : IDENTIFIER
#     | interface_type DOT IDENTIFIER'''
#     p[0] = regurgitate(p)

# def p_method_body(p):
#     '''method_body : block
#     | SEMICOLON'''
#     p[0] = p[1]

# def p_formal_parameter_list(p):
#     '''formal_parameter_list : fixed_parameters
#     | fixed_parameters COMMA parameter_array
#     | parameter_array'''
#     p[0] = regurgitate(p)

# def p_fixed_parameters(p):
#     '''fixed_parameters : fixed_param
#     | fixed_parameters fixed_parameter'''
#     p[0] = regurgitate(p)

# def p_fixed_param(p):
#     '''fixed_parameter : attributes_opt parameter_modifier_opt type IDENTIFIER default_argument_opt'''
#     p[0] = regurgitate(p)

# def p_default_argument(p):
#     '''default_argument : EQUALS expression'''
#     p[0] = regurgitate(p)

# def p_parameter_modifier(p):
#     '''parameter_modifier : REF
#     | OUT
#     | THIS'''
#     p[0] = p[1]

# def p_parameter_array(p):
#     '''parameter_array : attributes_opt PARAMETERS array_type IDENTIFIER'''
#     p[0] = regurgitate(p)

# def p_property_declaration(p):
#     '''property_declaration : attributes_opt property_modifiers_opt type member_name OPENING_PARENTHESIS accessor-declarations CLOSING_PARENTHESIS'''

#     p[0] = regurgitate(p)

# def p_property_modifiers(p):
#     '''property_modifiers : property_modifier
#     | property_modifiers property_modifier'''
#     p[0] = regurgitate(p)

# def p_property_modifier(p):
#     '''property_modifier : NEW
#     | PUBLIC
#     | PROTECTED
#     | INTERNAL
#     | PRIVATE
#     | STATIC
#     | VIRTUAL
#     | SEALED
#     | OVERRIDE
#     | ABSTRACT
#     | EXTERN'''
#     p[0] = p[1]


### 2.8 Structs
def p_struct_declaration(p):
    '''struct_declaration : attributes_opt struct_modifiers_opt partial_opt STRUCT IDENTIFIER type_parameter_list_opt struct_interfaces_opt type_parameter_constraints_clauses_opt struct_body semicolon_opt'''
    p[0] = regurgitate(p)

def p_struct_modifiers(p):
    '''struct_modifiers : struct_modifier
    | struct_modifiers struct_modifier'''
    p[0] = regurgitate(p)

def p_struct_modifiers_opt(p):
    '''struct_modifiers_opt : struct_modifiers
    | empty'''
    p[0] = regurgitate(p)

def p_struct_modifier(p):
    '''struct_modifier : NEW
    | PUBLIC
    | PROTECTED
    | INTERNAL
    | PRIVATE'''
    p[0] = p[1]

def p_struct_interfaces(p):
    '''struct_interfaces : COLON interface_type_list'''
    p[0] = regurgitate(p)

def p_struct_interfaces_opt(p):
    '''struct_interfaces_opt : struct_interfaces
    | empty'''
    p[0] = regurgitate(p)

def p_struct_body(p):
    '''struct_body : OPENING_PARENTHESIS struct_member_declarations_opt CLOSING_PARENTHESIS'''
    p[0] = regurgitate(p)

def p_struct_member_declarations(p):
    '''struct_member_declarations : struct_member_declaration
    | struct_member_declarations struct_member_declaration'''
    p[0] = regurgitate(p)

def p_struct_member_declarations_opt(p):
    '''struct_member_declarations_opt : struct_member_declarations
    | empty'''
    p[0] = regurgitate(p)


def p_struct_member_declaration(p):
    '''struct_member_declaration : empty'''
    p[0] = regurgitate(p)

# def p_struct_member_declaration(p):
#     '''struct_member_declaration : constant_declaration
#     | field_declaration
#     | method_declaration
#     | property_declaration
#     | event_declaration
#     | indexer_declaration
#     | operator_declaration
#     | constructor_declaration
#     | static_constructor_declaration
#     | type_declaration'''
#     p[0] = p[1]
    


### 2.9 Arrays
def p_array_type(p):
    '''array_type : non_array_type rank_specifiers'''
    p[0] = regurgitate(p)

def p_non_array_type(p):
    '''non_array_type : type'''

def p_array_initialiser(p):
    '''array_initialiser : OPENING_BRACE variable_initialiser_list_opt CLOSING_BRACE
    | OPENING_BRACE variable_initialiser_list COMMA CLOSING_BRACE'''

    p[0] = regurgitate(p)

def p_variable_initialiser(p):
    '''variable_initialiser : expression
    | array_initialiser'''

    p[0] = p[1]

def p_variable_initialiser_list(p):
    '''variable_initialiser_list : variable_initialiser
    | variable_initialiser_list COMMA variable_initialiser'''

    p[0] = regurgitate(p)

def p_variable_initialiser_list_opt(p):
    '''variable_initialiser_list_opt : variable_initialiser_list
    | empty'''

    p[0] = regurgitate(p)





### 2.11 Enums
def p_enum_declaration(p):
    '''enum_declaration : attributes_opt ENUM IDENTIFIER enum_base_opt enum_body semicolon_opt'''
    p[0] = regurgitate(p)

def p_enum_base(p):
    '''enum_base : COLON integral_type'''
    p[0] = regurgitate(p)

def p_enum_base_opt(p):
    '''enum_base_opt : enum_base
    | empty'''
    p[0] = regurgitate(p)

def p_enum_body(p):
    '''enum_body : OPENING_PARENTHESIS enum_member_declarations_opt CLOSING_PARENTHESIS
    | OPENING_PARENTHESIS enum_member_declarations COMMA CLOSING_PARENTHESIS'''
    p[0] = regurgitate(p)

def p_enum_modifiers(p):
    '''enum_modifiers : enum_modifier
    | enum_modifiers enum_modifier'''
    p[0] = regurgitate(p)

def p_enum_modifier(p):
    '''enum_modifier : NEW
    | PUBLIC
    | PROTECTED
    | INTERNAL
    | PRIVATE'''
    p[0] = p[1]

def p_enum_member_declarations(p):
    '''enum_member_declarations : enum_member_declaration
    | enum_member_declarations enum_member_declaration'''
    p[0] = regurgitate(p)

def p_enum_member_declarations_opt(p):
    '''enum_member_declarations_opt : enum_member_declarations
    | empty'''
    p[0] = regurgitate(p)

def p_enum_member_declaration(p):
    '''enum_member_declaration : attributes_opt IDENTIFIER
    | attributes_opt IDENTIFIER EQUALS constant_expression'''
    p[0] = regurgitate(p)

def p_constant_expression(p):
    '''constant_expression : expression'''
    p[0] = p[1]


### 2.12 Delegates
def p_delegate_declaration(p):
    '''delegate_declaration : DELEGATE IDENTIFIER OPENING_BRACE CLOSING_BRACE'''

    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + ' ' + p[4]

def p_delegate_modifiers(p):
    '''delegate_modifiers : delegate_modifier
    | delegate_modifiers delegate_modifier'''

    p[0] = regurgitate(p)

def p_delegate_modifier(p):
    '''delegate_modifier : NEW
    | PUBLIC
    | PROTECTED
    | INTERNAL
    | PRIVATE'''


### 2.13 Attributes
# def p_global_attributes(p):
#     '''global_attributes : global_attribute_sections'''
#     p[0] = p[1]

# def p_global_attribute_sections(p):
#     '''global_attribute_sections : global_attribute_section
#     | global_attribute_sections global_attribute_section'''
#     p[0] = regurgitate(p)

# # TODO: comma_opt?
# def p_global_attribute_section(p):
#     '''global_attribute_section : OPENING_BRACKET global_attribute_target_specifier attribute_list CLOSING_BRACKET
#     | OPENING_BRACKET global_attribute_target_specifier attribute_list COMMA CLOSING_BRACKET'''
#     p[0] = regurgitate(p)


# def p_global_attribute_target_specifier(p):
#     '''global_attribute_target_specifier : global_attribute_target COLON'''
#     p[0] = regurgitate(p)

# def p_global_attribute_target(p):
#     '''global_attribute_target : ASSEMBLY
#     | MODULE'''

#     p[0] = p[1]

# def p_attributes(p):
#     '''attributes : attribute_sections'''
#     p[0] = regurgitate(p)

# def p_attribute_sections(p):
#     '''attribute_sections : attribute_section
#     | attribute_sections attribute_section'''
#     p[0] = regurgitate(p)

# def p_attribute_section(p):
#     '''attribute_section : OPENING_BRACKET attribute_target_specifier_opt attribute_list CLOSING_BRACKET
#     |  OPENING_BRACKET attribute_target_specifier_opt attribute_list COMMA CLOSING_BRACKET'''

#     p[0] = regurgitate(p)

# def p_attribute_target_specifier(p):
#     '''attribute_target_specifier : attribute_target COLON'''
#     p[0] = regurgitate(p)

# def p_attribute_target_specifier_opt(p):
#     '''attribute_target_specifier_opt : attribute_target_specifier
#     | empty'''
#     p[0] = regurgitate(p)

# def p_attribute_target(p):
#     '''attribute_target : FIELD
#     | EVENT
#     | METHOD
#     | PARAM
#     | PROPERTY
#     | RETURN
#     | TYPE'''
#     p[0] = p[1]

# def p_attribute_list(p):
#     '''attribute_list : attribute
#     | attribute_list COMMA attribute'''
#     p[0] = regurgitate(p)

# def p_attribute(p):
#     '''attribute : attribute_name attribute_args_opt'''
#     p[0] = regurgitate(p)

# def p_attribute_name(p):
#     '''attribute_name : type_name'''
#     p[0] = p[1]

# def p_attribute_arguments(p):
#     '''attribute_arguments : OPENING_PARENTHESIS positional_argument_list_opt CLOSING_PARENTHESIS
#     | OPENING_PARENTHESIS positional_argument_list COMMA named_argument_list CLOSING_PARENTHESIS
#     | OPENING_PARENTHESIS named_argument_list CLOSING_PARENTHESIS'''
#     p[0] = regurgitate(p)


# def p_attribute_args_opt(p):
#     '''attribute_args_opt : attribute_args
#     | empty'''
#     p[0] = regurgitate(p)

# def p_positional_argument_list(p):
#     '''positional_argument_list : positional_arg
#     | positional_argument_list COMMA positional_argument'''
#     p[0] = regurgitate(p)

# def p_positional_argument(p):
#     '''positional_argument : argument_name_opt attribute_argument_expression'''
#     p[0] = regurgitate(p)

# def p_named_argument_list(p):
#     '''named_argument_list : named_arg
#     | named_argument_list COMMA named_argument'''
#     p[0] = regurgitate(p)

# def p_named_argument(p):
#     '''named_argument : IDENTIFIER EQUALS attribute_argument_expression'''
#     p[0] = regurgitate(p)

# def p_attribute_argument_expression(p):
#     '''attribute_argument_expression : expression'''
#     p[0] = regurgitate(p)
    
    
    





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
