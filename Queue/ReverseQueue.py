from queue import Queue

def rev(q):
    # add code here
    stack = []
    while not q.empty():
        item = q.get()
        print(item)
        stack.append(item)
    print(stack)
    while len(stack):
        q.put(stack[-1])
        stack.pop()
    return q


queue = Queue(maxsize=5)

queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)

ans = rev(queue)
print(list(ans.queue))
