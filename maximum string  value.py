test_list = ['gfg', 'is', 'best', 'for', 'geeks']
max_len = -1
for ele in test_list:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele
print("Maximum length string is : " + res)


     