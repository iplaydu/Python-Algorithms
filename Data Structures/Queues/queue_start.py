# try out the Python queue functions
from collections import deque

# TODO: create a new empty deque object that will function as a queue

q = deque()

# TODO: add some items to the queue

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)


# TODO: print the queue contents

print(q)

# TODO: pop an item off the front of the queue

q.popleft()
print(q)