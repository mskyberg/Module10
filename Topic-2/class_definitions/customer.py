"""
Program: customer.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: July 2020

Purpose: Demonstrate the use of encapsulation by creating an customer class
"""


class Customer(object):
    """ Customer Class """
    def __init__(self, c_id, lname, fname, phone, addr):
        """
        Constructor for Customer class

        :param c_id: Customer id
        :param lname: Customer Last Name
        :param fname: Customer First Name
        :param phone: Customer Phone Number
        :param addr: Customer address
        """
        self.customer_id = c_id
        self.last_name = lname
        self.first_name = fname
        self.phone_number = phone
        self.address = addr
        pass

    def display(self):
        """
        Description: display the customer information

        :returns: string of customer information
        """
        # cleanup address
        address_list = self.address.split(', ')
        street = f'{address_list[0]}'
        city_state = f'{address_list[1]}, {address_list[2]}'

        # return final string
        return f'{self.first_name} {self.last_name}, Customer#: ' \
               f'{self.customer_id}\n{street}\n{city_state}\n' \
               f'{self.phone_number}'

    def __str__(self):
        pass

    def __repr__(self):
        pass


if __name__ == '__main__':
    pass
