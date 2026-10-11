N = int(input("Size of array: "))
nums = list(map(int, input("Enter array elements: ").split()))
count = 0
for i in range(N):
    sum1 = sum(map(int, str(nums[i])))
    print(nums[i], "-> Digit Sum =", sum1)
for i in range(N):
    for j in range(i + 1, N):
        sum1 = sum(map(int, str(nums[i])))
        sum2 = sum(map(int, str(nums[j])))
        if sum1 == sum2:
            count += 1
print("Number of pairs:", count)