from collections import deque
import imp

dq=deque(maxlen=3)
print(dq)
dq.append(0)
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)
# dq.pop()
dq.popleft()
print(dq)


import queue as q
#or
# from multiprocessing import Queue

qu=q.Queue(maxsize=3)
print(qu.empty())
qu.put(0)
qu.put(1)
qu.put(2)
print(qu.full())
print(qu.get())
print(qu)