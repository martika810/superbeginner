import unittest
import inspect
from palindrome import Palindrome

class PalindromeTestClass(unittest.TestCase):
    def test_sentence_that_is_palindrom(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        palindrome = Palindrome('Nurses Run')
        self.assertTrue(palindrome.is_palindrome())

    def test_sentence_that_is_not_palindrome(self):
        print("\nRunning Test Method : " + inspect.stack()[0][3])
        palindrome = Palindrome('How are you')
        self.assertFalse(palindrome.is_palindrome())