def if_balaned(word):
    letter_max_min={}
    letter_list={}
    for letter in word:
        if not letter in letter_list:
            letter_list[letter]=0
    for i in range(2,len(word)):
        letter_max_min={x: [len(word),0] for x in letter_list}
        for case in range(0,len(word)-i+1):
            letter_list={x: 0 for x in letter_list}
            for letter in word[case:i+case]:
                letter_list[letter]+=1
            for letter in letter_list:
                if letter_list[letter]>letter_max_min[letter][1]:
                    letter_max_min[letter][1]=letter_list[letter]
                elif  letter_list[letter]<letter_max_min[letter][0]:
                    letter_max_min[letter][0]=letter_list[letter]
        for letter in letter_max_min.keys():
            if letter_max_min[letter][1]-letter_max_min[letter][0]>1:
                return False
    return True


    #FIXME
