#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----


class FizzBuzz:
    def __init__(self):
        self._check_number = 0
        self._output_string = ''

    def set_number(self, check_number):
        self._set_check_number(check_number)
        self._check_fizz_buzz_conditions()

    def get_result(self):
        return self._output_string

    def _set_check_number(self, check_number):
        self._check_number = check_number
        self._output_string = check_number

    def _check_fizz_buzz_conditions(self):
        self._check_fizz()
        self._check_buzz()
        self._check_fizz_buzz()

    def _check_fizz(self):
        if self._check_number % 3 == 0:
            self._output_string = "Fizz"

    def _check_buzz(self):
        if self._check_number % 5 == 0:
            self._output_string = "Buzz"

    def _check_fizz_buzz(self):
        if self._check_number % 15 == 0:
            self._output_string = "Fizz Buzz"


MAX_NUMBER = 101

if __name__ == "__main__":
    fizz_buzz = FizzBuzz()

    for check_number in range(MAX_NUMBER):
        fizz_buzz.set_number(check_number)
        print(fizz_buzz.get_result())

# -----END FIZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----


# -----END PAYROLL CODE-----
