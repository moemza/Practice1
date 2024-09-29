import unittest
from python_practice import *

class TestCase(unittest.TestCase):
    
    def test_filters(self):
        for number in filter_numbers(4,7):
            self.assertIsInstance(number, int, "Items in list must be integers")
        self.assertIsInstance(filter_numbers(9,0), list, "Expected a list")
        self.assertEqual(len(filter_numbers(9,7)), 8, "List is not expected length")
        self.assertEqual(filter_numbers(1, 5), [0,2,3,4,6,7,8,9], "Incorrect output")
        self.assertEqual(filter_numbers(0,4), [1,2,3,5,6,7,8,9], "Unexpected output")


    def test_stars(self):
        self.assertIsInstance(star_conversion("star", 4), str, "Expected a string")
        self.assertEqual(star_conversion("Coding is fun!", 4), "Cod*ng is fun!", "Unexpected output")
        self.assertEqual(star_conversion("I got this", 6), "I got*this", "Unexpected output")    


    def test_exponents(self):
        self.assertIsInstance(find_exponent(5, 125), int, "Expected an int")
        self.assertEqual(find_exponent(5,125), 3, "Unexpected output")
        self.assertEqual(find_exponent(7, 282475249), 10, "Unexpected output")
        self.assertEqual(find_exponent(6, 36), 2, "Unexpected output")


    def test_reverse(self):
        self.assertIsInstance(reverse_cases(["joef", "oijwer"]), list, "Expected a list")
        self.assertEqual(reverse_cases(['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']),
                         ['CAT', 'CATATATATCTSA', 'ABCDEFHIJKLMNOP', '521581932952421', '', 'FOO', 'UNIQUE'], 
                         "Unexpected output")
        self.assertEqual(reverse_cases(['Green', 'Red', 'Orange', 'Yellow', '', 'White']), 
                         ['gREEN', 'rED', 'oRANGE', 'yELLOW', '', 'wHITE'], "Unexpected output")
        self.assertEqual(reverse_cases(['Hello', '!@#', '!@#$', '123#@!']), ['hELLO', '#@!', '$#@!', '!@#321'], 
                         "Unexpected output")
        

    def test_month_days(self):
        self.assertIsInstance(month_days("January"), str,"Expected a string")
        self.assertEqual(month_days("mARch"), 31, "Unexpected output")
        self.assertEqual(month_days("feb"), 28, "Unexpected output")
        self.assertEqual(month_days("jun"), 30, "Unexpected output")


    def test_duplicates(self):
        self.assertIsInstance(remove_duplicates(["ji", "ki", "ji"]), list, "Expected a list")
        self.assertEqual(remove_duplicates([1, 3, 4, 10, 4, 1, 43]), [1, 3, 4, 10, 43], "Unexpected output")
        self.assertEqual(remove_duplicates([10, 11, 13, 23, 11, 25, 23, 76, 99]), [10, 11, 13, 23, 25, 76, 99], "Unexpected output")
        self.assertEqual(remove_duplicates(["python", "java", "C#", "java", "c++"]), ["python", "java", "C#", "c++"], "Unexpected output")


    def test_fibonacci(self):
        self.assertIsInstance(fibonacci(4), list, "Expected a list")
        self.assertEqual(len(fibonacci(6)), 6, "List is not expected length")
        self.assertEqual(fibonacci(1), [0], "Unexpected output")
        self.assertEqual(fibonacci(9), [0, 1, 1, 2, 3, 5, 8, 13, 21], "Unexpected output")


    def test_primes(self):
        self.assertIsInstance(prime_words("Come on"), str, "Expected a string")
        self.assertEqual(prime_words("The quick brown fox jumps over the lazy dog."), "The quick brown fox jumps the",
                         "Unexpected output")
        self.assertEqual(prime_words("Omicron Effect: Foreign Flights Won't Resume On Dec 15, Decision Later."),
                         "Omicron Effect: Foreign Flights Won't On Dec 15,", "Unexpected output")
        

    def test_decimals(self):
        self.assertIsInstance(shift_decimals(26732, 3), int, "Expected an integer")
        self.assertEqual(shift_decimals(12345, 1), 23451, "Unexpected output")
        self.assertEqual(shift_decimals(12345, 2), 34512, "Unexpected output")
        self.assertEqual(shift_decimals(12345, 5), 12345, "Unexpected output")
        self.assertEqual(shift_decimals(12345, 6), 54321, "Unexpected output")
