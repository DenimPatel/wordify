import sys
sys.path.append("../")

import numpy
from  algorithm.wordifier import Wordifier
from utils import *
if __name__ == "__main__":
    wordifier = Wordifier()
    wordifier.add_words_to_dictionary("data/google_10000_medium.txt")
    query_srting = "983SCHOOL9"
    print("query_srting = ", query_srting)
    query = wordifier.words_to_number(query_srting)
    response = wordifier.all_wordifications(query)
    print("query_srting is present in all wodificaton = ", query_srting in response)
