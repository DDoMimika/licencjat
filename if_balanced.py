# to prawie jest wektorami Parikha

def if_balanced(word, n):
    letter_amount = {}
    
    for letter in word:
        letter_amount[letter] = 0

    for len_factor in range(n+1, len(word)):
        letter_max_min = {x: {"max":0,"min":len(word)}for x in letter_amount}
        for factor_nr in range(0, len(word) - len_factor + 1):
            letter_amount = {x: 0 for x in letter_amount}
            for letter in word[factor_nr : len_factor + factor_nr]:
                letter_amount[letter] += 1
            for letter in letter_amount:
                if letter_amount[letter] > letter_max_min[letter]["max"]:
                    letter_max_min[letter]["max"] = letter_amount[letter]
                if letter_amount[letter] < letter_max_min[letter]["min"]:
                    letter_max_min[letter]["min"] = letter_amount[letter]
        for letter in letter_max_min.keys():
            if letter_max_min[letter]["max"] - letter_max_min[letter]["min"] > n:
                return False
    return True