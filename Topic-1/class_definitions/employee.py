"""
Program: employee.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrate the use of encapsulation by creating an employee class
"""


class Employee(object):
    """ Employee Class """
    def __init__(self):
        """
        Constructor for Employee class

        :param lname: employee last name
        :param fname: employee first name
        :param address: employee address
        :param phone: employee phone number
        :param salaried: employee salaried check (true if salaried)
        :param s_date: employee start date
        :param salary: employee earnings
        """

    def display(self):
        """
        Description: display the employee information

        :returns: string of employee information
        """
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


if __name__ == '__main__':
    pass
