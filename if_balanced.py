def if_balaned(word, dict_word):
    check = True
    letter_max_min={}
    for letter in word:
        if not letter in letter_max_min:
            letter_max_min[letter]=[0,0]

    for len in dict_word:
        print(f"\n {len}")
        for case in dict_word[len]:
            print(case)
            for letter in letter_max_min:
                if not letter in dict_word[len][case]:
                    letter_max_min[letter][0]=0
                else:
                    if case==0:
                        letter_max_min[letter]=[dict_word[len][case][letter],dict_word[len][case][letter]]
                    if dict_word[len][case][letter]<letter_max_min[letter][0]:
                        letter_max_min[letter][0]=dict_word[len][case][letter]
                    elif dict_word[len][case][letter]>letter_max_min[letter][1]:
                        letter_max_min[letter][1]=dict_word[len][case][letter]
        for letter in letter_max_min.keys():
            if letter_max_min[letter][1]-letter_max_min[letter][0]>1:
                check=False
    return check


    #FIXME
