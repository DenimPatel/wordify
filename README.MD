

# Wordify Phone Number
#### Wordify is a Python package to wordify Phone numbers.

Main 3 functionalities are:

- number_to_words()
    
      takes a string representing phone number and returns wordified string.


- words_to_numbers()
   
      takes wordified string and returns phone number.

- all_wordifications()
  
      takes a string representing phone number and returns a list of all wordified numbers.

## Test
```python
pytest
```

## Usage

```python
import Wordifier

wordifier = Wordifier()
wordifier.add_words_to_dictionary("data/google_10000_medium.txt")
number = "9878724665"
wordified_number = "9878SCHOOL"
response = wordifier.words_to_number(wordified_number) # returns phone number 
response = wordifier.number_to_words(number) # returns wordified number
response = wordifier.all_wordifications(number) # returns list of woridifed number
```
#### Output:
```python
Words to number: Query:  9878SCHOOL Response:  9878724665 

Number to words: Query:  9878724665 Response:  9878SCHOOL 

All wordification for Number:  9878724665
['98STRAIN65', '987TRAIN65', '9878SCHOOL'] 
```
## Assumptions:
- The number contains 9 to 12 digit
- The number can't have 0 and 1 digit except for the initial two positions
- Initial two numbers are not used for wordification
- Dictionary may contain duplicate words

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
