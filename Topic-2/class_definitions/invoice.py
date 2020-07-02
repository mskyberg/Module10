"""
Program: invoice.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: July 2020

Purpose:
"""


class Invoice(object):
    def __init__(self, inv_id, c_id, addr, lname, fname, phone, items=dict()):
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

    def add_item(self, item):
        """
        add item to the total items dictionary
        
        :param item: the item key, value to add to items dictionary
        """
        self.items_with_price.update(item)

    def create_invoice(self):
        """
        Prints each item with price then a total with tax calculated
        """
        sales_tax = 0.06
        item_sum = 0
        inv = f'Invoice#: {self.invoice_id}\n'
        for key, value in self.items_with_price.items():
            item_sum += value
            inv += f'{key}.....${value:.2f}\n'

        tax = item_sum * sales_tax
        inv += f'Tax.....${tax:.2f}\n'
        inv += f'Total.....${tax + item_sum:.2f}'
        # print(inv)
        # returning for unit testing purposes
        return inv

    def display(self):
        """
        display the invoice object information

        :returns: no return
        """
        print(f'{self.first_name} {self.last_name}, Customer#: '
              f'{self.customer_id}\n{self.address}\n{self.phone_number}\n'
              f'{self.create_invoice()}')

    def __str__(self):
        return f'Invoice#: {self.invoice_id}\n{self.first_name} ' \
               f'{self.last_name}, Customer#: {self.customer_id}\n' \
               f'{self.address}\n{self.phone_number}\n{self.items_with_price}'

    def __repr__(self):
        return f'invoice_id = {self.invoice_id}\n' \
               f'customer_id = {self.customer_id}\n' \
               f'last_name = {self.last_name}\n' \
               f'first_name = {self.first_name}\n' \
               f'phone_number = {self.phone_number}\n' \
               f'address = {self.address}\n' \
               f'items_with_price = {self.items_with_price}\n'


if __name__ == '__main__':
    # Driver code
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
    invoice.display()
