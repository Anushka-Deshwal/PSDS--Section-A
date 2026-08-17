#stack using linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None

# Push
def push(data):
    global top
    new_node = Node(data)
    new_node.next = top
    top = new_node
    print(data, "pushed")


# Pop
def pop():
    global top

    if top is None:
        print("Stack is empty")
    else:
        print(top.data, "popped")
        top = top.next


# Display
def display():
    temp = top
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


push(10)
push(20)
push(30)

print("Stack:")
display()

pop()

print("After pop:")
display()

#queue using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


front = None
rear = None

# Enqueue
def enqueue(data):
    global front, rear

    new_node = Node(data)

    if rear is None:
        front = rear = new_node
    else:
        rear.next = new_node
        rear = new_node

    print(data, "enqueued")


# Dequeue
def dequeue():
    global front, rear

    if front is None:
        print("Queue is empty")
    else:
        print(front.data, "dequeued")
        front = front.next

        if front is None:
            rear = None


# Display
def display():
    temp = front
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


enqueue(10)
enqueue(20)
enqueue(30)

print("Queue:")
display()

dequeue()

print("After dequeue:")
display()