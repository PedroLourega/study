# Docstrings are read by automated documentation tools and are returned by calling the special attribute .__doc__ on the function, method, or class name. Docstring conventions are laid out in PEP257.

# Docstrings can also function as lightweight unit tests, which will be covered in a later exercise.

# An example on a user-defined function.

def raise_to_power(number, power):
        """Raise a number to an arbitrary power.

        :param number: int the base number.
        :param power: int the power to raise the base number to.
        :return: int - number raised to the specified power.

        Takes a number and raises it to the specified power, returning the result.
        """

        return number ** power

# Calling the .__doc__ attribute of the function and printing the result.
print(raise_to_power.__doc__)