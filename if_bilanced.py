# to prawie jest wektorami Parikha

def if_bilanced(word, n):
    letter_max_min = {}
    letter_amount = {}
    
    for letter in word:
        if not letter in letter_amount:
            letter_amount[letter] = 0

    for i in range(n+1, len(word)):
        letter_max_min = {x: [len(word), 0] for x in letter_amount}
        for case in range(0, len(word) - i + 1):
            letter_amount = {x: 0 for x in letter_amount}
            for letter in word[case : i + case]:
                letter_amount[letter] += 1
            for letter in letter_amount:
                if letter_amount[letter] > letter_max_min[letter][1]:
                    letter_max_min[letter][1] = letter_amount[letter]
                elif letter_amount[letter] < letter_max_min[letter][0]:
                    letter_max_min[letter][0] = letter_amount[letter]
        for letter in letter_max_min.keys():
            if letter_max_min[letter][1] - letter_max_min[letter][0] > n:
                return False
    return True
