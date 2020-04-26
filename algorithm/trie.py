"""
Module implements Trie Data structure with methods required
"""

class TrieNode:
    """
    Trie Node data structure
    Stores: array of 26: children Trie Nodes
            bool : whether current node is End of the word
    """
    def __init__(self):
        self.children = [None]*26
        self.is_end_of_the_word = False

class Trie:
    """
    Trie Data structure

    methods:
        insert
        search
        search_multi_words
    """
    def __init__(self):
        self.root = self.get_new_node()

    @staticmethod
    def char_to_index(character):
        return ord(character)-ord('a')

    @staticmethod
    def get_new_node():
        return TrieNode()

    def insert(self, key):
        """
        Insert key value into Trie Data structure
        """
        current_node = self.root
        length = len(key)
        for level in range(length):
            index = self.char_to_index(key[level])
            if not current_node.children[index]:
                current_node.children[index] = self.get_new_node()
            current_node = current_node.children[index]
        current_node.is_end_of_the_word = True

    def search(self, key):
        """
        Search whether key is present in the Trie or not
        Return bool
        """
        current_node = self.root
        length = len(key)
        for level in range(length):
            index = self.char_to_index(key[level])
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]

        return current_node is not None and current_node.is_end_of_the_word

    def search_multi_words(self, key):
        """
        Search whether all words in input string is present or not
        Return bool
        """
        if "SCHOOL" == key:
            print("key", key)
        if "DRAIN" == key:
            print("key", key)
        
        key = key.lower()
        current_node = self.root
        length = len(key)
        temp_ans = False
        for level in range(length):
            # if(key == "SCHOOL"):
            #     print("level = ", level, " key = ", key[level])
            index = self.char_to_index(key[level])
            # if(key == "SCHOOL"):
            #     print(index)
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]
            if current_node.is_end_of_the_word:
                if level != length-1:
                    temp_ans = self.search_multi_words(key[level+1:])
                    if temp_ans:
                        return True
        # (current_node != None and current_node.is_end_of_the_word) or temp_ans
        return current_node.is_end_of_the_word if current_node is not None else temp_ans
