"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(minutes_cooked):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - minutes_cooked

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of layers in lasagna.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME' multiplied by
            number_of_layers.

    Function that takes the number_of_layers and returns the preparation time in minutes.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elasped time in minutes.

    :param number_of_layers: int - number of layers in lasagna.
    :param elapsed_bake_time: int - minutes in oven
    :return: int - sum of preparation_time and bake time

    Function that takes the number_of_layers and elapsed_bake_time and returns the total time             in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
