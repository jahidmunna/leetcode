import heapq

nums = [3, 9, 4, 1, 5, 9, 2, 0, 5, 3, 5]
print("Actual Numbers: ", nums)
K = 5 # Top lowest K elements of the list
max_heap = []
for num in nums:
    length = len(max_heap)
    if length < K:
        heapq.heappush(max_heap, -num)
    else:
        if -max_heap[0]>num:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)

max_heap = [-num for num in max_heap]
max_heap = sorted(max_heap)
print(f"Smallest {K}th elements are: {max_heap}")

K = 5 # Top largest K elements of the list
min_heap = []
for num in nums:
    length = len(min_heap)
    if length < K:
        heapq.heappush(min_heap, num)
    else:
        if min_heap[0]<num:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

min_heap = sorted(min_heap, reverse=True)
print(f"Largest {K}th elements are: {min_heap}")
