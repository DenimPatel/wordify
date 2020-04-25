"""
test module for basic utility functions
"""
from utils.utils import remove_non_alpha_numeric, string_to_number
 
 
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
       return_val = string_to_number("CDZZ")
       assert return_val == "2399"
 
   @staticmethod
   def test_string_to_number_2():
       """
       test case:
       """
       return_val = string_to_number("AAZZ")
       assert return_val == "2299"
 
   @staticmethod
   def test_string_to_number_3():
       """
       test case:
       """
       return_val = string_to_number("ZZAA")
       assert return_val == "9922"
 
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
       return_val = string_to_number("WXYZ")
       assert return_val == "9999"
 
