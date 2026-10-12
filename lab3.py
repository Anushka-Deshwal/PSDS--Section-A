#stack removing elements one by one
'''import numpy as np
arr = np.array([1,2,3,4,6])
print("Before popped")
while arr.size>0 :
    print("after popped")
    arr = np.delete(arr,-1)
    print(arr)'''

#nqueue and dqueue
import numpy as np
queue = np.array([10,20,30])
print("Original queue",queue)
#enqueue
queue = np.append(queue,40)
print("After enqueue",queue)
#Dequeue
dequeued_item  =  queue[0]
print("Dequeue_item",dequeued_item)
queue = np.delete(queue,0)
print("After dequeue", queue)
