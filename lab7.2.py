arr = [4, 2, 7, 1]
arr.sort()
result = []
left = 0
right = len(arr) - 1
while left <= right:
    result.append(arr[left])
    left += 1
    if left <= right:
        result.append(arr[right])
        right -= 1
total = 0
for i in range(1, len(result)):
    total += abs(result[i] - result[i - 1])
print("Rearranged array:", result)
print("Total sum:", total)