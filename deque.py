# queue using list and collections.deque

from collections import deque

que = deque([1,2,3])

que.append(4)
que.append(5)

print que

que.popleft() # FIFO

print que