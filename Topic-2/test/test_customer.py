"""
Program: test_customer.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: test the customer class
"""

import unittest
from class_definitions import customer as c


class MyTestCase(unittest.TestCase):
    def test_customer_creation(self):
        expected = f'Mike Skyberg, Customer#: 1234\n123 Heathrow Drive\n' \
                   f'Ames, Iowa\n515-515-5551'
        s_customer = c.Customer(c_id=1234,
                                lname='Skyberg',
                                fname='Mike',
                                phone='515-515-5551',
                                addr='123 Heathrow Drive, Ames, Iowa')
        self.assertEqual(s_customer.display(), expected)


if __name__ == '__main__':
    unittest.TestCase()
