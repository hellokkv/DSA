#To print the pairs of sum of number which will be equal to the target element

def pairs(arr1,target):
    new_list = []
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):

            if arr1[i] + arr1[j] == target:
                p = f'{arr1[i]}+{arr1[j]}'
                new_list.append(p)
    return new_list
mylist = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
print(pairs(mylist,7))

