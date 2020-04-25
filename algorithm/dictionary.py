"""
Module implements Dictionary data structure to store Englist words
Methods:
    Add words from txt
    add single word
    search word in dictionary
    search string consist of multiply words
"""
from algorithm.trie import Trie

class Dictionary:
    """
    Dictionary DS
    Mehods:
        len(object)
        add_single_word
        add_to_dictionary_from_txt
        search
        search_multi_words
    """
    def __init__(self):
        self.data = Trie()
        self.total_count = 0

    def __len__(self):
        """
        Return the length of Dictionary
        """
        return self.total_count

    def add_to_dictionary_from_txt(self, dict_name):
        """
        Import information from txt file
        which contains words in each line
        """
        with open(dict_name) as file:
            for line in file:
                if len(line) > 1:
                    self.data.insert(line.split()[0])
                    self.total_count = self.total_count + 1

    def add_single_word(self, word_to_add):
        """
        Insert one word into dictionary
        """
        self.data.insert(word_to_add)
        self.total_count = self.total_count + 1

    def search(self, word_to_search):
        """
        Search a word in dictionary
        """
        return self.data.search(word_to_search)

    def search_multi_words(self, multi_words):
        """
        Search whether all words containing in string is present
        """
        return self.data.search_multi_words(multi_words)
