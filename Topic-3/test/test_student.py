"""
Program: test_student.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: July 2020

Purpose: demonstrate unit tests on a class
"""

import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Skyberg', 'Mike', 'Developer')

    def tearDown(self):
        del self.student

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Skyberg')
        self.assertEqual(self.student.first_name, 'Mike')
        self.assertEqual(self.student.major, 'Developer')

    def test_object_created_all_attributes(self):
        student = s.Student('Skyberg', 'Mike', 'Developer', 3.76)
        assert student.last_name == 'Skyberg'
        assert student.first_name == 'Mike'
        assert student.major == 'Developer'
        assert student.gpa == 3.76


if __name__ == '__main__':
    unittest.TestCase()
