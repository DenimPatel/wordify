"""
Testing module for data loading functions
"""
import pytest
from utils.utils import read_string_to_number_mapping

class TestReadStringToNumber:
    """
    Test to check mapping from character to number
    """
    @staticmethod
    def test_read_string():
        """
        Test function to check character to number mapping
        """
        mapping = read_string_to_number_mapping()
        assert mapping["A"] == '2' and mapping["C"] == '2' and mapping["C"] == '2'
        assert mapping["D"] == '3' and mapping["E"] == '3' and mapping["F"] == '3'
        assert mapping["G"] == '4' and mapping["H"] == '4' and mapping["I"] == '4'
        assert mapping["J"] == '5' and mapping["K"] == '5' and mapping["L"] == '5'
        assert mapping["M"] == '6' and mapping["N"] == '6' and mapping["O"] == '6'
        assert mapping["P"] == '7' and mapping["Q"] == '7' and mapping["R"] == '7' \
            and mapping["S"] == '7'
        assert mapping["T"] == '8' and mapping["U"] == '8' and mapping["V"] == '8'
        assert mapping["W"] == '9' and mapping["X"] == '9' and mapping["Y"] == '9' \
            and mapping["Z"] == '9'

    @staticmethod
    def test_read_string_invalid():
        """
        Test: read string to number: invalid input: numeric
        """
        mapping = read_string_to_number_mapping()
        with pytest.raises(KeyError):
            assert mapping["3"]

    @staticmethod
    def test_read_string_invalid2():
        """
        Test: read string to number: invalid input: symbol
        """
        mapping = read_string_to_number_mapping()
        with pytest.raises(KeyError):
            assert mapping["-"]
