
## Acknowledgements

 - [WiktionaryParser](https://github.com/suyashb95/WiktionaryParser)
 


## Features

- **Fetch Word Data from Wiktionary**: Utilizes the WiktionaryParser to fetch detailed information about a given word from Wiktionary.
- **Etymology Extraction**: Extracts and provides the etymology of the word.
- **Definitions Extraction**: Retrieves definitions in human-readable format
- **Declension Detection**: Identifies and returns the declension of the word if mentioned in the definitions

## Example Usage

```py
from word import Word

# Create a Word object
word = Word('example_word')

# Access etymology
print(word.etymology)

# Access definitions
print(word.definitions)

# Access declension
print(word.get_declension())

# Access IPA pronunciation
print(word.ipa)
```

