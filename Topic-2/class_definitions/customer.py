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
        if isinstance(c_id, int):
            self.customer_id = c_id
        else:
            raise AttributeError(f'Invalid Customer ID: {c_id}')
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
        return f'{self.customer_id}{self.first_name} {self.last_name}\n' \
               f'{self.address}\n{self.phone_number}'

    def __repr__(self):
        return f'customer_id = {self.customer_id}\n' \
               f'last_name = {self.last_name}\n' \
               f'first_name = {self.first_name}\n' \
               f'address = {self.address}\n' \
               f'phone_number = {self.phone_number}\n'


if __name__ == '__main__':
    customer1 = Customer(586, 'Bravo', 'Johnny', '867-5309',
                         '134 NoWhere Ave, Ames, Iowa')
    print(customer1.display())

    try:
        customer2 = Customer('test_string_id', 'name1', 'name2', 'addr1', 'phone1')
        # i dont really understand how you expect to print this if customer2 is undefined
        print(customer2.display())
    except AttributeError as err:
        print(err)

    # I handled the attribute error in the constructor of the customer class.
