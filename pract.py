dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge(d1,d2):
    
    for i in d1 and d2:
        count=0
        if d1[i] == d2[i]:
            count+=i
        d1.update(d2)
            
    return d1
print(merge(dict1,dict2))