
"""
utility function to perform string manipulation/conversion/modification
"""
import re
import sys
sys.path.append("../")

def read_string_to_number_mapping():
    """
    return map which maps characters to numbers
    """
    mapping = {}
    with open("data/char_number_correspodence.txt") as file:
        for line in file:
            (key, val) = line.split()
            mapping[str(key)] = str(val)
    return mapping

def remove_non_alpha_numeric(input_string):
    """
    return string by removing non alpha numric characters from it
    """
    return re.sub(r'\W+', '', input_string)

def string_to_number(text):
    """
    return string by replacing characters with corresponding number
    """
    mapping = read_string_to_number_mapping()
    ans = ""
    for char in text:
        if char.isalpha():
            ans += mapping[char]
        else:
            ans += char
    return ans
