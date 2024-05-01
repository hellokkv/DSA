#write a code such tht it should print the pair of sum of numbers which will be equal to the target element inside the array
#for ex [1,2,3,4,5,6]. Target = 5 -----> [2,3]   
#(sum of 2 + 3 =5)
def sum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print("Pairs of sum = ",i,j)
my_list = [1,8,2,4,5,2,4,3,3,7,7,8,9,5]
sum(my_list,15)
