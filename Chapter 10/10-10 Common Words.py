def word_count(filename, word):
    """Count how many times a word repeats in the file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        pass
    else:
        wordcount = contents.lower().count(word)

        print(f"\nThe word '{word}' appears approximately {wordcount} times in {filename}")

filename = 'self-help.txt'

word_count(filename, 'the')

