arr = [2, 1, 5, 2, 3, 2]
target = 7
left = 0
total = 0
minimum = float('inf')
start = 0
end = 0
for right in range(len(arr)):
    total += arr[right]
    while total > target:
        if right - left + 1 < minimum:
            minimum = right - left + 1
            start = left
            end = right
        total -= arr[left]
        left += 1
if minimum == float('inf'):
    print("No subarray found")
else:
    print("Subarray:", arr[start:end + 1])
    print("Length:", minimum)
    print("Sum:", sum(arr[start:end + 1]))