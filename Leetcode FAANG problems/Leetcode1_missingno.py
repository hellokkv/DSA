#Find the missing number in the array of consecutive number
def missing(arr,n):
    total=n*(n+1)/2
    sum_arr=sum(arr)
    missing= total-sum_arr
    return int(missing)
print(missing([1,2,3,4,6],6))