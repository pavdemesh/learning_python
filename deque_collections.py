from collections import deque


# Type is collections.deque
stack_queue = deque()
print(type(stack_queue))

stack_queue.append("first element")
stack_queue.append("second_element")
stack_queue.append("third element")
stack_queue.append("fourth element")

# Work like with stack
last_item = stack_queue.pop()
print(last_item)

# Work like with queue
first_item = stack_queue.popleft()
print(first_item)

print(stack_queue)
