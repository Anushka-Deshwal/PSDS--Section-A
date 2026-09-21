N, K = map(int, input().split())

arr = list(map(int, input().split()))

window_sum = sum(arr[:K])
max_sum = window_sum

for i in range(K, N):
    window_sum = window_sum + arr[i]
    window_sum = window_sum - arr[i - K]

    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)

s = input()

seen = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])

    max_length = max(max_length, right - left + 1)

print(max_length)