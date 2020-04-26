"""
Test the wordifier methods
"""
import pytest
from algorithm.wordifier import Wordifier

@pytest.fixture
def ready_wordifier():
    """
    Return wordifier intance
    """
    wordifier = Wordifier()
    wordifier.add_words_to_dictionary("data/google_10000_medium.txt")
    return wordifier

class TestWordifier:
    """
    Test wordifier methods
    """
    @staticmethod
    def test_wordifier_words_to_numbers(ready_wordifier):
        """
        Test method: words to numbers
        """
        assert ready_wordifier.words_to_number("HELLO") == "43556"
        assert ready_wordifier.words_to_number("hello") == "43556"
        assert ready_wordifier.words_to_number("painterhothot") == "7246837468468"
        assert ready_wordifier.words_to_number("18-SUPPORT") == "18-7877678"

    @staticmethod
    def test_wordifier_words_to_numbers_2(ready_wordifier):
        """
        Test method: words to numbers with numerals and special characters
        """
        assert ready_wordifier.words_to_number("803-308-hello") == "803-308-43556"
        assert ready_wordifier.words_to_number("803-308-HELLO") == "803-308-43556"

    @staticmethod
    def test_wordifier_all_wordification1(ready_wordifier):
        """
        Test method: check atleast one response is there for known wodified query
        """
        query = ready_wordifier.words_to_number("18SOFTWARE")
        response = ready_wordifier.all_wordifications(query)
        assert len(response) >= 1

    @staticmethod
    def test_wordifier_all_wordification2(ready_wordifier):
        """
        Test method: all wordification see known answer is present
        """
        query = ready_wordifier.words_to_number("38SOFTWARE")
        response = ready_wordifier.all_wordifications(query)
        assert len(response) >= 1
        assert "38SOFTWARE" in response

    @staticmethod
    def test_wordifier_all_wordification3(ready_wordifier):
        """
        Test method: all wordification see known answer is present
        """
        query = ready_wordifier.words_to_number("99-PRODUCTS")
        response = ready_wordifier.all_wordifications(query)
        assert len(response) >= 1
        assert "99PRODUCTS" in response

    @staticmethod
    def test_wordifier_all_wordification3a(ready_wordifier):
        """
        Test method: all wordification see known answer is present
        """
        query = ready_wordifier.words_to_number("983SCHOOL9")
        response = ready_wordifier.all_wordifications(query)
        assert len(response) >= 1
        assert "983SCHOOL9" in response
    
    @staticmethod
    def test_wordifier_all_wordification4(ready_wordifier):
        """
        Test method: all wordification see all answer has correct phone number
        """
        query = ready_wordifier.words_to_number("18PAINTSAINT")
        response = ready_wordifier.all_wordifications(query)
        assert len(response) >= 1
        for each in response:
            assert ready_wordifier.words_to_number(each) == query
