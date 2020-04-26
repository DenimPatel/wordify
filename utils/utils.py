
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
            ans += mapping[char.upper()]
        else:
            ans += char
    return ans

def find_number_to_character_mapping(number):
    """
    Return correspondence from number to characters
    ex: "4" -> ["G", "H", "I"]
    Input should be valid query i.e. input can't be 0 or 1
    """
    # number = 
    # if not number.isdigit():
    #     return ""

    mapping = {}
    mapping["2"] = ["A", "B", "C"]
    mapping["3"] = ["D", "E", "F"]
    mapping["4"] = ["G", "H", "I"]
    mapping["5"] = ["J", "K", "L"]
    mapping["6"] = ["M", "N", "O"]
    mapping["7"] = ["P", "Q", "R", "S"]
    mapping["8"] = ["T", "U", "V"]
    mapping["9"] = ["W", "X", "Y", "Z"]
    return mapping[number]
