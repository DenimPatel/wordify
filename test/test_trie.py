"""
To test the Trie data structure and its methods
""" 
from algorithm.trie import TrieNode, Trie

class TestTrieNode:
    """
    Test functionalities of TrieNode
    """
    @staticmethod
    def test_trienode_basics():
        node = TrieNode()
        assert node.is_end_of_the_word is False
        assert None in node.children

class TestTrieDS:
    """
    Test functionalities of Trie data structure
    """
    @staticmethod
    def test_trie_char_to_index():
        """
        Test functionalities of Trie data structure
        """
        assert 0 == Trie._char_to_index('a')
        assert 3 == Trie._char_to_index('d')
        assert 25 == Trie._char_to_index('z')

    @staticmethod
    def test_trie_get_new_node():
        """
        Test functionalities of Trie data structure
        """
        node = Trie._get_new_node()
        assert node.is_end_of_the_word is False
        assert None in node.children

    @staticmethod
    def test_trie_insert1():
        """
        test insert conditions
        """
        trie_ds = Trie()
        insert_element = "a"
        trie_ds.insert(insert_element)
        assert trie_ds.root.children[Trie._char_to_index(insert_element)] is not None
    
    @staticmethod
    def test_trie_insert2():
        """
        test insert conditions
        """
        trie_ds = Trie()
        insert_element = "z"
        trie_ds.insert(insert_element)
        assert trie_ds.root.children[Trie._char_to_index(insert_element)] is not None
    
    @staticmethod
    def test_trie_search1():
        """
        test search conditions
        """
        trie_ds = Trie()
        insert_element = "z"
        trie_ds.insert(insert_element)
        assert trie_ds.search(insert_element) is True

    @staticmethod
    def test_trie_search2():
        """
        test search conditions
        """
        trie_ds = Trie()
        insert_element = "zazzfgdi"
        trie_ds.insert(insert_element)
        assert trie_ds.search(insert_element) is True

    @staticmethod
    def test_trie_search3():
        """
        test search conditions
        """
        trie_ds = Trie()
        assert trie_ds.search("random") is False

    @staticmethod
    def test_trie_search4():
        """
        test search conditions
        """
        trie_ds = Trie()
        assert trie_ds.search("jfdhjekjebt") is False
    
    @staticmethod
    def test_trie_searh_multiword1():
        """
        test search conditions for multiwords
        """
        trie_ds = Trie()
        insert_element1 = "a"
        insert_element2 = "z"
        trie_ds.insert(insert_element1)
        trie_ds.insert(insert_element2)
        assert trie_ds.search_multi_words(insert_element1 + insert_element2) is True

    @staticmethod
    def test_trie_searh_multiword2():
        """
        test search conditions for multiwords: what if string is empty
        """
        trie_ds = Trie()
        insert_element1 = "a"
        insert_element2 = ""
        trie_ds.insert(insert_element1)
        trie_ds.insert(insert_element2)
        assert trie_ds.search_multi_words(insert_element1 + insert_element2) is True

    @staticmethod
    def test_trie_searh_multiword3():
        """
        test search conditions for multiwords: what if string is empty
        """
        trie_ds = Trie()
        insert_element1 = ""
        insert_element2 = "z"
        trie_ds.insert(insert_element1)
        trie_ds.insert(insert_element2)
        assert trie_ds.search_multi_words(insert_element1 + insert_element2) is True

    @staticmethod
    def test_trie_searh_multiword4():
        """
        test search conditions for multiwords: general case
        """
        trie_ds = Trie()
        insert_element1 = "apple"
        insert_element2 = "zelle"
        trie_ds.insert(insert_element1)
        trie_ds.insert(insert_element2)
        assert trie_ds.search_multi_words(insert_element1 + insert_element2) is True

