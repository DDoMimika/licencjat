# sprwadznie przerw

def if_balanced_interval(word, n):
    dict_intervals = {}
    max_sum = 0
    min_sum = len(word)
    max_tab=[]
    for i in range(len(word)):
        if word[i] not in dict_intervals:
            dict_intervals[word[i]] = {"intervals": [i], "last": i}
        else:
            dict_intervals[word[i]]["intervals"].append(
                i - dict_intervals[word[i]]["last"] - 1
            )
            dict_intervals[word[i]]["last"] = i
    for key in dict_intervals:
        dict_intervals[key]["intervals"].append(i - dict_intervals[key]["last"])
        if(len(dict_intervals[key]["intervals"])>n+1):
            max_tab=[]
            for j in range(1,len(dict_intervals[key]["intervals"])-1):
                max_sum = 0
                min_sum = len(word)
                for k in range(0, len(dict_intervals[key]["intervals"]) - j + 1):
                    sum_intervals = sum(dict_intervals[key]["intervals"][k : k + j])
                    if sum_intervals > max_sum:
                        max_sum = sum_intervals
                    if sum_intervals < min_sum and k !=0 and k+j!=len(dict_intervals[key]["intervals"]):
                        min_sum = sum_intervals
                max_tab.append(max_sum)
                if (j>=n and max_tab[j-n]-min_sum > n):
                    return False
    return True

