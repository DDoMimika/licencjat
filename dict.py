def word_to_dit(word):
    dict_word = {}
    for i in range(len(word)-1,1,-1):
        dict_word[i]={}
        for j in range(0,len(word)+1-i):
            dict_word[i][j]={}
            for letter in word[j:j+i]:
                if letter not in dict_word[i][j]:
                    dict_word[i][j][letter]=1
                else:
                    dict_word[i][j][letter]+=1
    return dict_word
