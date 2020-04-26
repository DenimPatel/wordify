"""
Test the wordifier methods 
"""
from algorithm.wordifier import Wordifier

class TestWordifier:
    """
    Test wordifier methods
    """
    @staticmethod
    def test_wordifier_words_to_numbers():
        """
        Test method: words to numbers
        """
        wordifier = Wordifier()
        assert wordifier.words_to_number("HELLO") == "43556"
        assert wordifier.words_to_number("hello") == "43556"
        assert wordifier.words_to_number("painterhothot") == "7246837468468"
        

    @staticmethod
    def test_wordifier_words_to_numbers_2():
        """
        Test method: words to numbers with numerals and special characters
        """
        wordifier = Wordifier()
        assert wordifier.words_to_number("803-308-hello") == "803-308-43556"
        assert wordifier.words_to_number("803-308-HELLO") == "803-308-43556"

    @staticmethod
    def test_wordifier_all_wordification3():
        """
        Test method: check atleast one response is there for known wodified query
        """
        wordifier = Wordifier()
        wordifier.add_words_to_dictionary("data/google_10000_medium.txt")
        query = wordifier.words_to_number("18SOFTWARE")
        response = wordifier.all_wordifications(query)
        assert len(response) >= 1

    @staticmethod
    def test_wordifier_all_wordification():
        """
        Test method: all wordification see known answer is present
        """
        wordifier = Wordifier()
        wordifier.add_words_to_dictionary("data/google_10000_medium.txt")
        query = wordifier.words_to_number("18PAINTPAINT")
        response = wordifier.all_wordifications(query)
        assert len(response) >= 1
        assert "18PAINTPAINT" in response
    
    @staticmethod
    def test_wordifier_all_wordification2():
        """
        Test method: all wordification see all answer has correct phone number
        """
        wordifier = Wordifier()
        wordifier.add_words_to_dictionary("data/google_10000_medium.txt")
        query = wordifier.words_to_number("18PAINTSAINT")
        response = wordifier.all_wordifications(query)
        assert len(response) >= 1
        for each in response:
            assert wordifier.words_to_number(each) == query
