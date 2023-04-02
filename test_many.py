from make_all import make_all
from if_balanced_intervals import if_balanced_interval
file_balanced_name="gene_balanced"
file_not_name="gene_not"
alphabet=["a","b"]
words_length=0
n_balanced=1

fn=open("nie_zbalansowane_choc_powinny","a")
fb=open("zbalansowane_choc_nie_powinny","a")

for i in range(4,19):
    words_length=i
    make_all(alphabet,words_length,n_balanced,file_balanced_name,file_not_name)

    file_balanced= open(file_balanced_name,"r+")
    file_not= open(file_not_name,"r+")

   
    for line in file_balanced.readlines():
        if(not if_balanced_interval(line.strip(),n_balanced)):
            fn.write(line.strip()+"\n")
    
    for line in file_not.readlines():
        if(if_balanced_interval(line.strip(),n_balanced)):
            fb.write(line.strip()+"\n")
    file_balanced.close()
    file_not.close()
fn.close()
fb.close()