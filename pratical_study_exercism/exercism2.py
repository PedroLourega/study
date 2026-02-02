# Instructions
# You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook.

# You have five tasks, all related to cooking your recipe.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 60

def bake_time_remaining(x):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    
    return EXPECTED_BAKE_TIME - x

print(bake_time_remaining(20))
    

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - preparation time in minutes.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calclate the elapsed cooking time.

    :param num_of_layers:int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the time already spend baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return (number_of_layers * 2) + elapsed_bake_time


