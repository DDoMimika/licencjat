from if_balanced import if_balanced
def add_letters(word,alphabet):
    tab=[]
    n=len(set(word))
    for i in range(min(n+1,len(alphabet))):
        tab.append(word+alphabet[i])
    return tab

def generate_words(tab,alphabet,length):
    if(len(tab[0])==length):
        return tab
    else:
        ntab=[]
        for word in tab:
            ntab+=add_letters(word,alphabet)
        return generate_words(ntab,alphabet,length)


def make_all(alphabet,length,n,fileb,filen):
    bfile=open(fileb,"w")
    nfile=open(filen,"w")
    tab=generate_words([""],alphabet,length)
    for word in tab:
        if(if_balanced(word,n)):
            bfile.write(word+"\n")
        else:
            nfile.write(word+"\n")
    bfile.close()
    nfile.close()

# make_all(["a","b"],15,9,"gene_balanced","gene_not")
