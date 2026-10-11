
def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            sum1 = sum(int(digit) for digit in str(abs(nums[i])))
            sum2 = sum(int(digit) for digit in str(abs(nums[j])))
            if sum1 == sum2:
                count += 1
    print(count)
solve()
