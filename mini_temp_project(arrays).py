days_no = int(input("How many days Temperature?"))
list1 = []
sum=0
count = 0
for i in range(days_no):
    temp = float(input(f"Enter {i+1}'s high temp: "))
    list1.append(temp)
    sum+=temp
    avg = sum/days_no
for i in (list1):
    if i > avg:
        count+=1
print("Avg = ",round(avg,2))
print(f"{count} day(s) above average")

    