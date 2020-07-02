"""
Program: test_invoice.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: test the invoice class
"""

import unittest
from class_definitions import invoice as inv


class MyTestCase(unittest.TestCase):
    def test_invoice_constructor(self):
        item_dict = {'iPad': 799.99}
        expected = f'Invoice#: 99\n' \
                   f'Mike Skyberg, Customer#: 1234\n' \
                   f'123 Heathrow Drive, Ames, Iowa\n' \
                   f'515-515-5551\n' \
                   f'{item_dict}'
        invoice = inv.Invoice(inv_id=99,
                              c_id=1234,
                              lname='Skyberg',
                              fname='Mike',
                              phone='515-515-5551',
                              addr='123 Heathrow Drive, Ames, Iowa',
                              items={'iPad': 799.99})
        self.assertEqual(str(invoice), expected)

    def test_invoice_creation_no_items(self):
        expected = f'Invoice#: 201\n' \
                   f'Tax.....$0.00\n' \
                   f'Total.....$0.00'
        invoice = inv.Invoice(inv_id=201,
                              c_id=1234,
                              lname='Skyberg',
                              fname='Mike',
                              phone='515-515-5551',
                              addr='123 Heathrow Drive, Ames, Iowa')
        self.assertEqual(invoice.create_invoice(), expected)

    def test_invoice_creation(self):
        items_dict = {'iPad': 799.99, 'Surface': 999.99}
        expected = f'Invoice#: 42\n' \
                   f'iPad.....$799.99\n' \
                   f'Surface.....$999.99\n' \
                   f'Tax.....$108.00\n' \
                   f'Total.....$1907.98'
        invoice = inv.Invoice(inv_id=42,
                              c_id=1234,
                              lname='Skyberg',
                              fname='Mike',
                              phone='515-515-5551',
                              addr='123 Heathrow Drive, Ames, Iowa',
                              items=items_dict)
        self.assertEqual(invoice.create_invoice(), expected)


if __name__ == '__main__':
    unittest.TestCase()
