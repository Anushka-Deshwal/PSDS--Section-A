#3sum problem
nums = [5, 6, -3, 8, 1, 9, 2]
nums.sort()
for i in range(len(nums) - 2):
    left = i + 1
    right = len(nums) - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == 0:
            print(nums[i], nums[left], nums[right])
            left += 1
            right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1

#fabonacci series 
n = int(input("Enter number : "))
a = 1
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c  
    
print("\n") 

#tower of hanoi
def tower_of_hanoi(n, source, helper, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, helper)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, helper, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, "A", "B", "C")