def filter_long_words(*args, **kwargs):
    min_length = kwargs.pop('min_length', 0)

    words = []
    for word in args:
        if len(word) > min_length:
            words.append(word)
    print(words)
    return words


filter_long_words('hello', 'hello', 'my', 'old', 'friend', min_length=5)
filter_long_words('hello', 'hello', 'my', 'old', 'friend', max_len=100)

