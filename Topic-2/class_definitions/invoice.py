"""
Program: invoice.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: July 2020

Purpose:
"""


class Invoice(object):
    def __init__(self, inv_id, c_id, lname, fname, phone, addr, items={}):
        """
        Invoice Class Constructor

        :param inv_id: invoice Id
        :param c_id: customer Id
        :param lname: customer last name
        :param fname: customer first name
        :param phone: customer phone number
        :param addr: customer address
        :param items: dictionary of items on the order with price
        """
        self.invoice_id = inv_id
        self.customer_id = c_id
        self.last_name = lname
        self.first_name = fname
        self.phone_number = phone
        self.address = addr
        self.items_with_price = items

    def add_item(self):
        """
        add item to the total items dictionary
        
        :param item: the item key, value to add to items dictionary
        """
        pass

    def create_invoice(self):
        """
        Prints each item with price then a total with tax calculated
        """
        pass

    def __str__(self):
        return f'Invoice#: {self.invoice_id}\n{self.first_name} ' \
               f'{self.last_name}, Customer#: {self.customer_id}\n' \
               f'{self.address}\n{self.phone_number}\n{self.items_with_price}'

    def __repr__(self):
        pass


if __name__ == '__main__':
    # Driver code
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
