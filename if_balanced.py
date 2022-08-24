def if_balaned(word, dict_word):
    check = True
    length = len(word) - 1
    ind = 0

    while length > 1:
        if length + ind < len(word):
            for i in range(ind, length):
                dict_word[word[i]][ind] += 1
                ind += 1
        for key in dict_word.keys:
            if max(dict_word[key]) - min(dict_word[key]) <= 1:
                return
        length -= 1

    return word
