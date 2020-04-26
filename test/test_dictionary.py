"""
Test Dictionary DS
"""
import sys
sys.path.append("../")

from algorithm.dictionary import Dictionary

class TestDictionary:
    """
    Test Dictionary DS implementation
    """
    @staticmethod
    def test_dictionary_constuction():
        """
        Test whether dictionary construction works properly
        """
        dictionary_obj = Dictionary()
        assert dictionary_obj is not None
        assert len(dictionary_obj) == 0

    @staticmethod
    def test_dictionary_after_one_addition():
        """
        Test dictionary status after adding one word
        """
        dictionary_obj = Dictionary()
        add_word = "az"
        dictionary_obj.add_single_word(add_word)
        assert dictionary_obj.search(add_word) is True
        assert len(dictionary_obj) == 1
        assert dictionary_obj.search_multi_words(add_word * 3) is True

    @staticmethod
    def test_dictionary_after_multi_addition():
        """
        Test dictionary status after adding one word
        """
        dictionary_obj = Dictionary()
        add_word1 = "az"
        add_word2 = "by"
        add_word3 = "cx"
        dictionary_obj.add_single_word(add_word1)
        dictionary_obj.add_single_word(add_word2)
        dictionary_obj.add_single_word(add_word3)
        assert dictionary_obj.search(add_word1) is True
        assert dictionary_obj.search(add_word2) is True
        assert dictionary_obj.search(add_word3) is True
        assert dictionary_obj.search("random") is False
        assert len(dictionary_obj) == 3
        assert dictionary_obj.search_multi_words(add_word1 + add_word3) is True

    @staticmethod
    def test_dictionary_text_read():
        """
        Test dictionary adds words from text file properly
        """
        dictionary_obj = Dictionary()
        dictionary_obj.add_to_dictionary_from_txt("data/google_10000_medium.txt")
        assert len(dictionary_obj) != 0
# TO DO: Add more test cases
 