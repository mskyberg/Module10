"""
Program: test_employee.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: test the employee class
"""

import datetime
import unittest
from class_definitions import employee as e


class MyTestCase(unittest.TestCase):
    def test_salaried_employee_creation(self):
        expected = f'Mike Skyberg\n123 Heathrow Drive\nAmes, Iowa\n' \
                   f'Salaried employee: $10,000/year\nStart date: 1-14-2013'
        start_date = datetime.datetime(2013, 1, 14)
        s_employee = e.Employee(lname='Skyberg',
                                fname='Mike',
                                address='123 Heathrow Drive Ames, Iowa',
                                phone='515-515-5551',
                                salaried=True,
                                s_date=start_date,
                                salary=10000)
        self.assertEqual(s_employee.display(), expected)

    def test_hourly_employee_creation(self):
        expected = f'Mike Skyberg\n123 Heathrow Drive\nAmes, Iowa\n' \
                   f'Hourly employee: $9/hour\nStart date: 1-14-2013'
        start_date = datetime.datetime(2013, 1, 14)
        s_employee = e.Employee(lname='Skyberg',
                                fname='Mike',
                                address='123 Heathrow Drive Ames, Iowa',
                                phone='515-515-5551',
                                salaried=False,
                                s_date=start_date,
                                salary=9)
        self.assertEqual(s_employee.display(), expected)


if __name__ == '__main__':
    unittest.TestCase()
