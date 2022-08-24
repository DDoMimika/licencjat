def word_to_dit(word):
    dict_word = {}
    for letter in word:
        if letter not in dict_word:
            dict_word = []
    return dict_word
