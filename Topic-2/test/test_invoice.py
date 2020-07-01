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


if __name__ == '__main__':
    unittest.TestCase()
