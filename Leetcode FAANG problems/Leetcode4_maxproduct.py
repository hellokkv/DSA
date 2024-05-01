#print the maximum product possible within the given array of numbers
#Solve again with another logic

def max_product(arr):
    arr.sort(reverse = True)
    a=arr[0]*arr[1]
    return f"{a} ({arr[0]}*{arr[1]})"
my_list = [1,2,9,3,7,5,6]
print(max_product(my_list))