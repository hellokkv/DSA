#To return true if the given set of list contains any duplicates and false if its distinct

def duplicates(arr1):
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[i] == arr1[j]:
                return True
        else:
            return False
my_list = [1,2,3,5]
print(duplicates(my_list))