# To check if 1 list if permutations of the other one. for ex: keep-peek, bad-dab,
#the letters are same but the order of the letters are different
#HINT: use sort functions


def permutations(arr1,arr2):
    arr1,arr2 = list(arr1),list(arr2)
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    elif len(arr1) != len(arr2):
        return False
    else:
        return False
hello = [1,2,3]
hello2 = [3,1,1]
print(permutations(hello,hello2))
