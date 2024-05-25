from src.word import Word


def main():
    word = Word('vir')
    print(f"Word: {word.word}")
    print(f"Declension: {word.get_declension()}")
    print(f"Etymology: {word.etymology}")
    print("Definitions:")
    for i, definition in enumerate(word.get_definitions(), 1):
        print(f"\t{i}. {definition}")
    print(f"IPA: {word.ipa}")


if __name__ == '__main__':
    main()
