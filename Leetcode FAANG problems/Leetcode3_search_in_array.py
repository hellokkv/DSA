#Finding a number in an array using linear search method
def linear_search(arr1,target):
    for i in range(len(arr1)):
        if arr1[i] == target:
            print("index position= ",i)
            return f"Found at position= {i+1}"

    return "Not found"
my_array = [12,34,1,2,356,678,34,56]
print(linear_search(my_array, 35))