T = int(input("Number of Test: "))
for i in range(T):
    s=input("Enter the String: ")
    freq = [0] * 26 
    for ch in s:
      freq[ord(ch) - ord('a')]+=1
      ans=0
      for x in freq:
          ans += x//2
    print(ans)