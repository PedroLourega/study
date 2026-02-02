my_first_variable = 1 # my_first_variable bound to an integer object of value one.
my_first_variable = 2 # my_first_variable re-assigned to integer value 2.

print(type(my_first_variable))
print(my_first_variable)

my_first_variable = "Now, Im a string." # You may re-bind a name to a different object type and value.

print(type(my_first_variable))

my_first_variable = 'You can call me "str"'# Strings can be declared using single or double quote marks.

print(my_first_variable)

# CONSTANTS
"""
Constants are names meant to be assigned only once in a program. They should be defined at a module (file) level, and are typically visible to all functions and classes in the program. Using SCREAMING_SNAKE_CASE signals that the name should not be re-assigned, or its value mutated.
"""
