#Write a function to print the first and second best scores inside the array

def best_score(arr1):
    big1,big2 = arr1[0],arr1[1]
    for i in arr1:
        if i>big1:
            big2 = big1
            big1 = i
        elif i>big2 and i!=big1:
            big2 = i
    return big1,big2

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(best_score(myList))