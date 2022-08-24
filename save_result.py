from paths import FILE_RESULT


def save_result(word):
    f = open(FILE_RESULT, "a")
    f.write(word)
    f.close
