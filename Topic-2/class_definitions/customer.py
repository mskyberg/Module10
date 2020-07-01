"""
Program: customer.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: July 2020

Purpose: Demonstrate the use of encapsulation by creating an customer class
"""


class Customer(object):
    """ Customer Class """
    def __init__(self):
        """
        Constructor for Customer class

        :param c_id:
        :param lname:
        :param fname:
        :param phone:
        :param addr:
        """
        # customer_id - required: number
        # last_name - required: string
        # first_name - required: string
        # phone_number - required: string
        # address - required: string
        pass

    def display(self):
        """
        Description: display the customer information

        :returns: string of customer information
        """
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


if __name__ == '__main__':
    pass
