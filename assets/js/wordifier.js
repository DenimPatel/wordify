/**
 * Wordifier, ported from algorithm/wordifier.py, algorithm/dictionary.py and utils/utils.py.
 */
const NUMBER_TO_CHARACTERS = {
  '2': ['A', 'B', 'C'],
  '3': ['D', 'E', 'F'],
  '4': ['G', 'H', 'I'],
  '5': ['J', 'K', 'L'],
  '6': ['M', 'N', 'O'],
  '7': ['P', 'Q', 'R', 'S'],
  '8': ['T', 'U', 'V'],
  '9': ['W', 'X', 'Y', 'Z'],
};

const CHARACTER_TO_NUMBER = {};
for (const [digit, chars] of Object.entries(NUMBER_TO_CHARACTERS)) {
  chars.forEach((char) => { CHARACTER_TO_NUMBER[char] = digit; });
}

function findNumberToCharacterMapping(digit) {
  return NUMBER_TO_CHARACTERS[digit] || null;
}

function removeNonAlphaNumeric(input) {
  // mirrors Python's re.sub(r'\W+', '', input) — \w is [A-Za-z0-9_]
  return input.replace(/[^a-zA-Z0-9_]+/g, '');
}

function stringToNumber(text) {
  let ans = '';
  for (const char of text) {
    if (/[a-zA-Z]/.test(char)) {
      ans += CHARACTER_TO_NUMBER[char.toUpperCase()];
    } else {
      ans += char;
    }
  }
  return ans;
}

function findAllCombinations(queryNumber) {
  const allCombinations = [];
  let ans = findNumberToCharacterMapping(queryNumber[0]);
  let currAns = [];
  for (let iterator = 1; iterator < queryNumber.length; iterator++) {
    const chars = findNumberToCharacterMapping(queryNumber[iterator]);
    for (const eachAns of ans) {
      for (const char of chars) {
        currAns.push(eachAns + char);
        allCombinations.push(eachAns + char);
      }
    }
    ans = currAns;
    currAns = [];
  }
  return allCombinations;
}

class WordifierError extends Error {}

class Wordifier {
  constructor(trie) {
    this.trie = trie;
  }

  _isValidQuery(numberQuery) {
    const rest = numberQuery.slice(2);
    if (rest.includes('0') || rest.includes('1')) {
      throw new WordifierError('Digits after the first two cannot contain 0 or 1.');
    }
    return true;
  }

  checkWordsAgainstDictionary(allCombinations) {
    const foundWords = [];
    for (const combination of allCombinations) {
      if (this.trie.searchMultiWords(combination.toLowerCase())) {
        foundWords.push(combination);
      }
    }
    return foundWords;
  }

  allWordifications(number) {
    const query = removeNonAlphaNumeric(number);
    this._isValidQuery(query);
    const result = [];
    for (let i = 2; i < query.length; i++) {
      const queryToCombinations = query.slice(i);
      const allCombinations = findAllCombinations(queryToCombinations);
      const words = this.checkWordsAgainstDictionary(allCombinations);
      for (const word of words) {
        result.push(query.slice(0, i) + word + query.slice(i + word.length));
      }
    }
    return result;
  }

  numberToWords(number) {
    const query = removeNonAlphaNumeric(number);
    this._isValidQuery(query);
    let result = '';
    let lastWord = '';
    for (let i = 2; i < query.length; i++) {
      const queryToCombinations = query.slice(i);
      const allCombinations = findAllCombinations(queryToCombinations);
      const words = this.checkWordsAgainstDictionary(allCombinations);
      for (const word of words) {
        const ans = query.slice(0, i) + word + query.slice(i + word.length);
        if (word.length >= lastWord.length) {
          result = ans;
          lastWord = word;
        }
      }
    }
    return result;
  }

  static wordsToNumber(queryString) {
    return stringToNumber(queryString);
  }
}
