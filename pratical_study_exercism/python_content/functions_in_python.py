# FUNCTIONS
# The def keyword begins a function definition. Each function can have zero or more formal parameters in () parentheses, followed by a : colon. Statements for the body of the function begin on the line following def and must be indented in a block.




# The body of a function is indented by 2 spaces, & prints the sum of the numbers.

def add_two_numbers(number_one, number_two):
    total = number_one + number_two
    print(total)

print(add_two_numbers(3,4))

# Inconsistent identation in your code blocks weill raise an error


# Functions explicitly return a value or object via the return keyword:

# Function definition on first line, explicit return used on final line.

def add_others_numbers(number_one, number_two):
    return number_one + number_two

# Calling the function in the Python shell returns the sum of the numbers.

print(add_others_numbers(3,4))


# Assigning the function call to a variable and printing it 

# will also return the value.

sum_with_return = add_two_numbers(5, 6)
print(sum_with_return)


# Functions that do not have an explicit expression following a return will implicitly return the None object. The details of None will be covered in a later exercise. For the purposes of this exercise and explanation, None is a placeholder that represents nothing, or null:

# This function will return `None`
def square_a_number(number):
    square = number * number
    return # <-- note that this return is not followed by an expression


# Calling the function in the Python shell appears
 
# to not return anything at all

# Using print() with the function call shows that 

print(square_a_number(2))


# Functions that omit return will also implicitly return the None object. This means that if you do not use return in a function, Python will return the None object for you.

# This function omits a return keyword altogether

def add_two_numbers(number_one, number_two):
  result = number_one + number_two

print(add_two_numbers(5, 7))

# Assigning the function call to a variable and printing 

# the variable will also show None.

sum_without_return = add_two_numbers(5, 6)
print(sum_without_return)



# Calling Functions
# Functions are called or invoked using their name followed by (). Dot (.) notation is used for calling functions defined inside a class or module.

def raise_to_power(number, power):
        return number ** power

print(raise_to_power(3,3)) # Invoking the function with the arguments 3 and 3.

# Calling methods or functions in classes and modules.

start_text = "my silly sentence for examples."
str.upper(start_text)  # Calling the upper() method from the built-in str class on start_text.

# Importing the math module
import math
print(math.pow(2,4)) # Calling the pow() function from the math module