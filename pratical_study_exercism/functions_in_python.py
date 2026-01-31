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

print(add_others_numbers(3,4))


# Assigning the function call to a variable and printing it 

# will also return the value.

sum_with_return = add_two_numbers(5, 6)
print(sum_with_return)