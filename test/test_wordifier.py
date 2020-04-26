"""
Test the wordifier methods
"""
import pytest
from algorithm.wordifier import Wordifier

@pytest.fixture
def ready_wordifier():
    '''Returns a Wallet instance with a zero balance'''
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

    @staticmethod
    def test_wordifier_words_to_numbers_2(ready_wordifier):
        """
        Test method: words to numbers with numerals and special characters
        """
        assert ready_wordifier.words_to_number("803-308-hello") == "803-308-43556"
        assert ready_wordifier.words_to_number("803-308-HELLO") == "803-308-43556"

    @staticmethod
    def test_wordifier_all_wordification3(ready_wordifier):
        """
        Test method: check atleast one response is there for known wodified query
        """
        query = ready_wordifier.words_to_number("18SOFTWARE")
        response = ready_wordifier.all_wordifications(query)
        assert len(response) >= 1

    @staticmethod
    def test_wordifier_all_wordification(ready_wordifier):
        """
        Test method: all wordification see known answer is present
        """
        ready_wordifier.add_words_to_dictionary("data/google_10000_medium.txt")
        query = ready_wordifier.words_to_number("18PAINTPAINT")
        response = ready_wordifier.all_wordifications(query)
        assert len(response) >= 1
        assert "18PAINTPAINT" in response

    @staticmethod
    def test_wordifier_all_wordification2(ready_wordifier):
        """
        Test method: all wordification see all answer has correct phone number
        """
        ready_wordifier.add_words_to_dictionary("data/google_10000_medium.txt")
        query = ready_wordifier.words_to_number("18PAINTSAINT")
        response = ready_wordifier.all_wordifications(query)
        assert len(response) >= 1
        for each in response:
            assert ready_wordifier.words_to_number(each) == query
