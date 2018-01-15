import heapq
import random

heap = []
data = list(range(10000))
random.shuffle(data)

print(heapq.nlargest(10, data))
print(heapq.nsmallest(10, data))