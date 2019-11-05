import pytest
from exercise import EmployeeFactoryImpl, EmployeeRecord, InvalidEmployeeTypeError


def test_excercise_employee_factory_impl_check_comission_employee_created():
    comissioned_employee_record = EmployeeRecord("COMISSIONED")
    employee_factory = EmployeeFactoryImpl()
    comissioned_employee = employee_factory.make_employee(comissioned_employee_record)
    assert str(type(comissioned_employee)) == "<class 'exercise.ComissionedEmployee'>"


def test_excercise_employee_factory_impl_check_hourly_employee_created():
    hourly_employee_record = EmployeeRecord("HOURLY")
    employee_factory = EmployeeFactoryImpl()
    hourly_employee = employee_factory.make_employee(hourly_employee_record)
    assert str(type(hourly_employee)) == "<class 'exercise.HourlyEmployee'>"


def test_excercise_employee_factory_impl_check_salaried_employee_created():
    salaried_employee_record = EmployeeRecord("SALARIED")
    employee_factory = EmployeeFactoryImpl()
    salaried_employee = employee_factory.make_employee(salaried_employee_record)
    assert str(type(salaried_employee)) == "<class 'exercise.SalariedEmployee'>"


def test_excercise_employee_factory_impl_check_returned_exception():
    unknown_employee_record = EmployeeRecord("UNKNOWN")
    employee_factory = EmployeeFactoryImpl()
    with pytest.raises(InvalidEmployeeTypeError):
        employee_factory.make_employee(unknown_employee_record)
