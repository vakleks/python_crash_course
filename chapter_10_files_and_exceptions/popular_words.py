def count_popular_word(filename, word):
    """How many such words in the text."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        count_word = contents.lower().count(word)

        msg = f"The '{word}' appears in the {filename} about {count_word} times."
        print(msg)

filename = 'alice.txt'
count_popular_word(filename, 'the')