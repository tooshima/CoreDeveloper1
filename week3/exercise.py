#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----

# Test code is in test_excersise.py. If you want to test this class,
# please use the following command.
# python -m pytest

from abc import ABCMeta, abstractmethod

COMISSIONED = "COMISSIONED"
HOURLY = "HOURLY"
SALARIED = "SALARIED"


class InvalidEmployeeTypeError(Exception):
    def __init__(self, msg: str, original_exception: str = None):
        if original_exception is not None:
            super(InvalidEmployeeTypeError, self).__init__(
                msg + (": %s" % original_exception)
            )
        else:
            super(InvalidEmployeeTypeError, self).__init__(msg)
        self.original_exception = original_exception


class Employee(metaclass=ABCMeta):
    @abstractmethod
    def is_payday(self):
        pass

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def deliver_pay(self, money):
        pass


class EmployeeRecord:
    def __init__(self, type: str):
        self.type = type


class ComissionedEmployee(Employee):
    def is_payday(self):
        pass

    def calculate_pay(self):
        pass

    def deliver_pay(self, money):
        pass


class HourlyEmployee(Employee):
    def is_payday(self):
        pass

    def calculate_pay(self):
        pass

    def deliver_pay(self, money):
        pass


class SalariedEmployee(Employee):
    def is_payday(self):
        pass

    def calculate_pay(self):
        pass

    def deliver_pay(self, money):
        pass


class EmployeeFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_employee(self, record: EmployeeRecord) -> Employee:
        pass


class EmployeeFactoryImpl(EmployeeFactory):
    def make_employee(self, record: EmployeeRecord) -> Employee:
        if record.type == COMISSIONED:
            return ComissionedEmployee()
        elif record.type == HOURLY:
            return HourlyEmployee()
        elif record.type == SALARIED:
            return SalariedEmployee()
        else:
            raise InvalidEmployeeTypeError(str(record.type))


# -----END PAYROLL CODE-----
