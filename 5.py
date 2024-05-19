def funcTest5 (lst):
    tempdict = {}
    outputdict = {}
    for i in range(len(lst)):
        if len(lst[i].split()) in tempdict:
            tempdict[len(lst[i].split())] = tempdict[len(lst[i].split())] + 1
        else:
            tempdict[len(lst[i].split())] = 1
    tempdict = dict(sorted(tempdict.items()))
    for i in tempdict:
        if i % 10 == 1 and i != 11:
            outputdict[str(i) + " слово"] = str((tempdict[i]/len(lst)) * 100) + "%"
        elif i % 10 in (2, 3, 4) and not(i in (12, 13, 14)) :
            outputdict[str(i) + " слова"] = str((tempdict[i]/len(lst)) * 100) + "%"
        else:
            outputdict[str(i) + " слов"] = str((tempdict[i]/len(lst)) * 100) + "%"
    return outputdict



search_queries = ["watch new movies", 
                  "coffee near me", 
                  "how to find the determinant", 
                  "python", 
                  "data science jobs in UK", 
                  "courses for data science", 
                  "taxi", 
                  "google", 
                  "yandex", 
                  "bing", 
                  "foreign exchange rates USD/BYN", 
                  "Netflix movies watch online free"
                  ]

print(funcTest5(search_queries))


