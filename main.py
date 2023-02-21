from if_bilanced import if_bilanced
from load_dict import load_file
from save_result import save_result
from dict import word_to_dit

N = 1
data = load_file()
for word in data:
    word = word.strip()
    # dict_word = word_to_dit(word)
    if if_bilanced(word, N):
        save_result(word)
