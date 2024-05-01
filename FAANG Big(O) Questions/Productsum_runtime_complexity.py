def psum(arr1):
    sum=0
    product=1
    for i in arr1:
        sum+=i

    for i in arr1:
        product*=i
    print(f"Sum = {sum} and Product = {product}")

list1 = [2,3,4,5,6]
print(psum(list1))