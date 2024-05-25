import json
import re

from wiktionaryparser import WiktionaryParser


class Word:
    def __init__(self, word):
        self.parser = WiktionaryParser()
        self.parser.set_default_language('latin')
        self.word = word
        self.data = json.loads(json.dumps(self.parser.fetch(word)))
        self.declension = self.get_declension()
        self.etymology = self.get_etymology()
        self.definitions = self.get_definitions()
        self.ipa = self.get_ipa()

    def get_etymology(self):
        etymology = ''
        if self.data:
            etymology = self.data[0]['etymology']
        return etymology

    def get_definitions(self):
        definitions = []
        if self.data:
            for part_of_speech in self.data[0]['definitions']:
                definitions.extend(part_of_speech['text'])
                definitions = [definition for definition in definitions if not re.search(r'\(.+?\)', definition)]

        return definitions

    def get_declension(self):
        declension = 0
        if self.data:
            for part_of_speech in self.data[0]['definitions']:
                for text in part_of_speech['text']:
                    match = re.search(r'(first|second|third|fourth|fifth)', text)
                    if match:
                        declension = match.group(1)
                        declension = {
                            'first': 1,
                            'second': 2,
                            'third': 3,
                            'fourth': 4,
                            'fifth': 5
                        }[declension]
                        break
        return declension

    def get_ipa(self):
        ipa = ''
        if self.data and self.data[0]['pronunciations']['text']:
            ipa_text = self.data[0]['pronunciations']['text'][0]
            match = re.search(r'IPA:\s*(/\S+/)', ipa_text)
            if match:
                ipa = match.group(1)
        else:
            ipa = "Not set"
        return ipa
