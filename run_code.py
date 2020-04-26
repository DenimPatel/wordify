"""
To try custom queries
"""
from  algorithm.wordifier import Wordifier

def run_functionalities():
    """
    Uses Wordifier and perfroms 3 functionality
    1. Words to number
    2. Number to words
    3. All wordification
    """
    wordifier = Wordifier()
    wordifier.add_words_to_dictionary("data/google_10000_medium.txt")

    # Functionality 1: Words to Number
    query_srting = "9878SCHOOL"
    number = wordifier.words_to_number(query_srting)
    print("\nWords to number: ", "Query: ", query_srting, "Response: ", number, "\n")

    #Functionaliry 3: Number to Words
    response = wordifier.number_to_words(number)
    print("Number to words: ", number, "Query: ", number, "Response: ", response, "\n")

    # Functionality 2: All wordification
    response = wordifier.all_wordifications(number)
    print("All wodification for Number: ", number)
    print(response, "\n")

if __name__ == "__main__":
    run_functionalities()
