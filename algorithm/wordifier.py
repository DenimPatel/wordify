"""
Module implements methods such as:
    wordify number
    all possible wordification
    convert wordified number
"""
from algorithm.dictionary import Dictionary
from utils.utils import find_number_to_character_mapping, string_to_number

class Wordifier:
    """
    Main methods includes:
        - number_to_words
        - all_wordifications
        - words_to_number
    """
    def __init__(self):
        self.dictionary = Dictionary()

    def all_wordifications(self, number):
        """
        Returns All wordification
        """
        result = []
        for i in range(2, len(number)):
            query_to_combinations = number[i:]
            all_combinations = self.find_all_combinations(query_to_combinations)
            words = self.check_words_against_dictionary(all_combinations)
            for word in words:
                ans = number[:i] + word + number[i+len(word):]
                result.append(ans)
            return result

    @staticmethod
    def words_to_number(query_string):
        """
        converts wordified phone number into numeric phone number
        """
        return string_to_number(query_string)

    def add_words_to_dictionary(self, filename):
        """
        Add words from file in the dictionary
        """
        self.dictionary.add_to_dictionary_from_txt(filename)

    def add_single_word_to_directory(self, word):
        """
        Add single word in the dictionary
        """
        self.dictionary.add_single_word(word)

    def check_words_against_dictionary(self, all_combinations):
        """
        Return all the combinations which are present in a Number
        """
        found_words = []
        for combination in all_combinations:
            query = combination.lower()
            is_present = self.dictionary.search_multi_words(query)
            if is_present:
                found_words.append(combination)
        return found_words

    @staticmethod
    def find_all_combinations(query_number):
        """
        From the query number, find all the combinations of words possible
        """
        all_combinations = []
        ans = find_number_to_character_mapping(int(query_number[0]))
        curr_ans = []
        for iterator in range(1, len(query_number)):
            num = query_number[iterator]
            chars = find_number_to_character_mapping(num)
            for each_ans in ans:
                for char in chars:
                    curr_ans.append(each_ans + str(char))
                    all_combinations.append(each_ans + str(char))
            ans = curr_ans
            curr_ans = []
        return all_combinations
