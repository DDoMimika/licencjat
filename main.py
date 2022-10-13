
from if_balanced import if_balaned
from load_dict import load_file
from save_result import save_result
from dict import word_to_dit

data = load_file()
for word in data:
    word = word.strip()
    dict_word = word_to_dit(word)
    if if_balaned(word, dict_word):
        save_result(word)
