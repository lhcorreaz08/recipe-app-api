""" Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add(self):
        self.assertEqual(calc.add(3, 8), 11)


    def test_subs(self):
        self.assertEqual(calc.substract(5, 11), -6)
        