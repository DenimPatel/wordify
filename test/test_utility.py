"""
test module for basic utility functions
"""
from utils.utils import remove_non_alpha_numeric, \
    string_to_number, \
    find_number_to_character_mapping
 
 
class TestRemoveNonAlphaNumeric:
   """
       test for fucntion remove_non_alpha_numeric
   """
 
   @staticmethod
   def test_function1():
       """
       test function: basic
       """
       test_string = "aihadjfn-kjadfj-jafkj-"
       assert remove_non_alpha_numeric(test_string) == "aihadjfnkjadfjjafkj"
 
   @staticmethod
   def test_function2():
       """
       test function: adverse
       """
       test_string = "--@&*$&@*)-aih[[[[[ad.......jf====^&(*)=n-kja------dfj-jafkj-------"
       assert remove_non_alpha_numeric(test_string) == "aihadjfnkjadfjjafkj"
 
   @staticmethod
   def test_function3():
       """
       test fuction: corner case
       """
       test_string = "--803(345)1645"
       assert remove_non_alpha_numeric(test_string) == "8033451645"
 
class TestStringToNumber:
   """
   test function string_to_number
   """
   @staticmethod
   def test_string_to_number_1():
       """
       test case:
       """
       return_val = string_to_number("CDzZ")
       assert return_val == "2399"
 
   @staticmethod
   def test_string_to_number_2():
       """
       test case:
       """
       return_val = string_to_number("AAazZZ")
       assert return_val == "222999"
 
   @staticmethod
   def test_string_to_number_3():
       """
       test case:
       """
       return_val = string_to_number("ZZ5AA")
       assert return_val == "99522"
 
   @staticmethod
   def test_string_to_number_4():
       """
       test case:
       """
       return_val = string_to_number("PQRS")
       assert return_val == "7777"
 
   @staticmethod
   def test_string_to_number_5():
       """
       test case:
       """
       return_val = string_to_number("9XYZ")
       assert return_val == "9999"
 
class TestNumberToCharacterMapping:
    """
    Test correspondence from number to characters
    """
    @staticmethod
    def test_num_to_chars_mapping():
        assert find_number_to_character_mapping("2") == ["A", "B", "C"]
        assert find_number_to_character_mapping("3") == ["D", "E", "F"]
        assert find_number_to_character_mapping("4") == ["G", "H", "I"]
        assert find_number_to_character_mapping("5") == ["J", "K", "L"]
        assert find_number_to_character_mapping("6") == ["M", "N", "O"]
        assert find_number_to_character_mapping("7") == ["P", "Q", "R", "S"]
        assert find_number_to_character_mapping("8") == ["T", "U", "V"]
        assert find_number_to_character_mapping("9") == ["W", "X", "Y", "Z"]