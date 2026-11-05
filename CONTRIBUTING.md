# Contributing to Wordify

Wordify is a small Python package — plus a static demo site — that turns phone
numbers into words and back. Give it `9878724665` and it can offer you
`9878SCHOOL`; give it `9878SCHOOL` and it gives you the number back.

- **Live demo:** <https://denimpatel.github.io/wordify/>
- **Readme:** [README.MD](README.MD)

This guide walks through how the repo is laid out, how to run it, and where new
code should go. It assumes you have never seen the project before.

## Project layout

```text
wordify/
├── index.html                        # Static demo page (hero, demo, how-it-works); GitHub Pages serves this
├── assets/
│   ├── css/
│   │   └── style.css                 # Styles for the demo page
│   └── js/
│       ├── app.js                    # Demo behaviour: mobile menu, scroll reveal, tabs, wiring forms to the wordifier
│       ├── trie.js                   # Browser-side port of algorithm/trie.py (TrieNode and Trie)
│       └── wordifier.js              # Browser-side Wordifier plus the keypad/string helpers from utils/utils.py
├── algorithm/
│   ├── wordifier.py                  # Wordifier: number_to_words(), all_wordifications(), words_to_number(),
│   │                                 #   add_words_to_dictionary(), add_single_word_to_dictionary(), and the
│   │                                 #   private helpers _is_valid_query(), check_words_against_dictionary(),
│   │                                 #   find_all_combinations()
│   ├── dictionary.py                 # Dictionary: wraps a Trie, counts words, loads a word list or one word,
│   │                                 #   exposes search() and search_multi_words()
│   └── trie.py                       # TrieNode and Trie: insert(), search(), search_multi_words(); 26 children
│                                     #   (a-z) per node plus an end-of-word flag
├── utils/
│   └── utils.py                      # String helpers: read_string_to_number_mapping() (reads
│                                     #   data/char_number_correspodence.txt), remove_non_alpha_numeric(),
│                                     #   string_to_number(), find_number_to_character_mapping() (2-9 keypad map)
├── data/
│   ├── char_number_correspodence.txt # Letter-to-digit keypad mapping, one "LETTER DIGIT" pair per line
│   ├── google_10000_medium.txt       # Word list used by run_code.py and the Python tests, one word per line
│   └── words.json                    # The demo's word list as a JSON array; app.js fetches it in the browser
├── test/                             # pytest suite (see "Tests" below)
│   ├── test_wordifier.py
│   ├── test_dictionary.py
│   ├── test_trie.py
│   ├── test_utility.py
│   └── test_read_files.py
├── run_code.py                       # Loads the dictionary and prints three example outputs
├── requirement.txt                   # pytest is the only package to install (`re` ships with Python)
├── .github/
│   └── workflows/
│       └── pages.yml                 # Deploys the repo root to GitHub Pages on every push to master
└── LICENSE                           # MIT
```

The file name `char_number_correspodence.txt` is spelled that way in the repo,
so keep using that spelling when you refer to it.

A couple of things worth knowing:

- `index.html` loads `trie.js`, `wordifier.js` and then `app.js` in that order.
  It has a number-to-words panel and a words-to-number panel, and the dictionary
  is fetched from `data/words.json`.
- `data/google_10000_medium.txt` and `data/words.json` hold the same 5,459
  words in two formats: a plain text file for Python, and a JSON array the
  browser can fetch.

## How the pieces fit together

- `Wordifier` owns a `Dictionary`, and `Dictionary` owns a `Trie`.
- `utils/utils.py` supplies the keypad mapping and the string helpers that
  `Wordifier` and `Dictionary` use.
- The JavaScript files in `assets/js/` mirror the same pieces for the browser:
  `trie.js` ports `Trie`, and `wordifier.js` ports `Wordifier` together with the
  keypad/string helpers from `utils.py`.
- `index.html` and everything under `assets/` are the only things GitHub Pages
  serves. The Python package never runs on the site — the demo is entirely
  client-side.

## Running it locally

Run every command from the repo root. The Python code and tests open files under
`data/` with paths relative to the repo root, so running from somewhere else
will fail to find them.

```bash
pip install -r requirement.txt   # install pytest
python run_code.py               # print the three example outputs
pytest                           # run the test suite
```

## Adding a feature

- **Algorithm changes** go in `algorithm/`, with a matching test in `test/`.
- **New string helpers** go in `utils/utils.py`.
- **Demo-page changes** go in `index.html` and `assets/` (`style.css` for looks,
  `app.js` for behaviour).
- If you change the Python algorithm, mirror the change in `assets/js/` so the
  browser demo stays in sync with the package.

## Tests

The suite uses [pytest](https://pytest.org/). Tests live in `test/`, roughly one
file per module:

| File | Covers |
| --- | --- |
| `test_wordifier.py` | `algorithm/wordifier.py` |
| `test_dictionary.py` | `algorithm/dictionary.py` |
| `test_trie.py` | `algorithm/trie.py` |
| `test_utility.py` | helpers in `utils/utils.py` |
| `test_read_files.py` | reading the keypad mapping from `data/` |

Run `pytest` from the repo root. New behaviour needs a test — please add one
with your change rather than only testing by hand.

## Pull requests

Pull requests are welcome. For major changes, please open an issue first to
discuss what you would like to change, and make sure the tests are updated as
appropriate. Note that a push to `master` redeploys the live demo, so anything
merged there goes public at <https://denimpatel.github.io/wordify/>.

## License

Wordify is released under the MIT license. See [LICENSE](LICENSE).
