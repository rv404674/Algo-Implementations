# NOTE: 1
# a heap is a complete BT i.e all nodes have two children.
# there can be two types of heap
# 1. max_heap = where A[parent(i)]>=A[i] i.e a parent node will always be greater than
# both its child node.
# 2. min_heap = where A[parent(i)] <= A[i]

# NOTE: 2
# for a node at index k
# wrt k starting from 0
# parent = (k-1)//2 , left_child = 2*k, right_child = 2*k+1

# NOTE: 3
# python3 heapq is min heap i.e smallest element at the top.
# for python3 heapq ""the smallest element has highest priority""
# Heaps are commonly used to implement priority queues. They’re the most popular concrete data structure for implementing the priority queue abstract data structure.
# pop and push from Heap is O(logn)
# heapify is O(n)
# Python heapq module includes heapify() for turning a iterable into a valid heap.

import heapq

a = [3, 5, 1, 2, 6, 8, 7]
heapq.heapify(a)

# NOTE: mn heap
# a heap doesnt need to be sorted to satisfy heap condition
print(a)
# [1, 2, 3, 5, 6, 8, 7]

heapq.heappop(a)
# 1

heapq.heappop(a)
# 2

heapq.heappush(a, 10)

a = { 'a':5, 'b':10, 'c':1}
pq = [(val,key) for key,val in a.items()]
# [('a', 5), ('b', 10), ('c', 1)]
heapq.heapify(pq)
heapq.heappop(pq)
# (1, 'c')

#NOTE: what if you want to find largest element first not smallest i.e you want to implement a mx heap
a = { 'a':5, 'b':10, 'c':1}
pq = [(-val,key) for key,val in a.items()]
heapq.heapify(pq)
# [(-5, 'a'), (-10, 'b'), (-1, 'c')]
heapq.heappop(pq)
# (-10, 'b')
 




