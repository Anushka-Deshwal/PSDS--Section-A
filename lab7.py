import heapq
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 15)
print("Min Heap:", heap)
print("Elements according to priority:")
while heap:
    print(heapq.heappop(heap), end=" ")
arr = [5, 2, 8, 1, 3]
heap = []
for x in arr:
    heapq.heappush(heap, x)
sorted_arr = []
while heap:
    sorted_arr.append(heapq.heappop(heap))
print("\nHeap Sort:", sorted_arr)