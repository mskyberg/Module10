"""
Program: employee.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: Demonstrate the use of encapsulation by creating an employee class
"""

import datetime


class Employee(object):
    """ Employee Class """
    def __init__(self, lname, fname, address, phone, salaried,
                 s_date, salary):
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
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = phone
        self.salaried = salaried
        self.start_date = s_date
        self.salary = salary

    def display(self):
        """
        Description: display the employee information

        :returns: string of employee information
        """
        # cleanup address
        address_list = self.address.split(', ')
        street = f'{address_list[0]}'
        city_state = f'{address_list[1]}, {address_list[2]}'

        # determine earnings statement
        earnings_string = ''
        if self.salaried:
            earnings_string = f'Salaried employee: ${self.salary:,}/year'
        else:
            earnings_string = f'Hourly employee: ${self.salary:,}/hour'

        # format start date
        s_date = self.start_date.strftime('%m-%d-%Y').lstrip("0").\
            replace(" 0", " ")

        # return final string
        return f'{self.first_name} {self.last_name}\n{street}\n{city_state}' \
               f'\n{earnings_string}\nStart date: {s_date}'

    def __str__(self):
        pass

    def __repr__(self):
        pass


if __name__ == '__main__':
    pass
