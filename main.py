from latindict.word import Word


def main():
    word = Word('vivere')
    print(f"Word: {word.word}")
    print(word.data)
    print(f"Declension: {word.declension}")
    print(f"Etymology: {word.etymology}")
    print("Definitions:")
    for i, definition in enumerate(word.get_definitions(), 1):
        print(f"\t{i}. {definition}")
    # print(f"IPA: {word.ipa}")


if __name__ == '__main__':
    main()
