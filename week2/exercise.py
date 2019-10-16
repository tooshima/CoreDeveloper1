#!/usr/bin/env python

# Week 2 Exercises: Naming

# Rewrite the two functions below.

# In your commit message, explain what was wrong and how you fixed it.

# FUNCTION 1: Check for a specific value in a list


def find_specific_value_in_list(find_value, input_list):
    if find_value in input_list:
        print("There is a 1")
        return
    else:
        for item in input_list:
            print(item)
        return

# FUNCTION 2: Pick out even numbers


def pick_out_even_numbers(input_list):
    even_number_list = []

    for number in input_list:
        if (number % 2) == 0:
            even_number_list.append(number)

    print(even_number_list)
    return even_number_list


if __name__ == "__main__":
    # FUNCTION 1 test
    target_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    find_value = 1
    find_specific_value_in_list(find_value, target_list)

    find_value = 100
    find_specific_value_in_list(find_value, target_list)

    # FUNCTION2 test
    pick_out_even_numbers(target_list)
