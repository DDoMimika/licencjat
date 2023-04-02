# from make_balanced import make_balanced
# from make_not_balanced import make_not_balanced
from if_balanced_intervals import if_balanced_interval

# from math import ceil
file_balanced= open("balanced_test_gene","r+")
file_not= open("not_test_gene","r+")

# tabalphabet=["a","b","c","d"]
# alphabet=["a"]
# tabrange=[20,15,12]
# for i in range(1,4):
#     alphabet.append(tabalphabet[i])
#     for n in range(4,ceil(tabrange[i-1]/2)):
#         make_not_balanced(alphabet,i,1,file_not)
#         file_not.write("\n")
#     for b in range(4,tabrange[i-1]):
#         make_balanced(alphabet,i,1,file_balanced)
#         file_balanced.write("\n")


fn=open("nie_zbalansowane_choc_powinny","w")

for line in file_balanced.readlines():
    if(not if_balanced_interval(line.strip(),9)):
        fn.write(line.strip()+"\n")
fn.close()


fb=open("zbalansowane_choc_nie_powinny","w")

for line in file_not.readlines():
    if(if_balanced_interval(line.strip(),9)):
        fb.write(line.strip()+"\n")
fb.close()