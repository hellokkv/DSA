#To remove duplicates from the list

def duplicates(list1):
    list1 = set(list1)
    list1 = list(list1)
    return(list1)
my_list = [1, 1, 2, 2, 3, 4, 5]
print(duplicates(my_list))