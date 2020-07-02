"""
Program: student.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: July 2020

Purpose: basic class for student information
"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not name_characters.issuperset(lname):
            raise ValueError
        if not name_characters.issuperset(fname):
            raise ValueError
        if not name_characters.issuperset(major):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f'{self.last_name}, {self.first_name} has major {self.major}' \
               f' with gpa: {str(self.gpa)}'
