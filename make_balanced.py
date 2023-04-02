# tworzenie słów zbilanoswanych
from if_balanced import if_balanced

def make_first_words(alphabet,word,n,tab):
    for letter in alphabet:
        word2=word+letter
        if(if_balanced(word2,n)==False):
            continue
        if len(word2)==n:
            tab.append(word2)
        else:
            make_first_words(alphabet,word2,n,tab)
    return tab

def add_letters(alphabet,tab,n):
    temp_tab=[]
    for word in tab:
        for letter in alphabet:
            if(if_balanced(word+letter,n)):
                temp_tab.append(word+letter)
    return temp_tab

def make_balanced(alphabet,length,n,file):
    tab=[]
    i=[0 for j in range(n+1)]
    tab=make_first_words(alphabet,"",n+2,tab)
    while(len(tab[0])!=length):
        tab=add_letters(alphabet,tab,n)
    file.write("\n".join(tab))

# with open("baza_zbalansowane","w") as file:
#     for i in range(4,21):
#         make_balanced(["a","b","c","d"],i,1)
#         file.write("\n")