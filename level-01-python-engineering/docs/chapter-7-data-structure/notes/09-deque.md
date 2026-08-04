# Lesson 9 — deque
### First Principle

A deque (pronounced deck) stands for double-ended queue.

Unlike a list, which is optimized for operations at the end, a deque is optimized for operations at both the front and the back.

Think of it like a train:

    Front                                   Back

                ◄── [A] [B] [C] [D] ──►

You can efficiently add or remove carriages from either end.

## Creating a deque

    from collections import deque

    queue = deque()

Or initialize it with data:

    from collections import deque

    queue = deque([1, 2, 3])

    print(queue)

Output:

    deque([1, 2, 3])

Why Not Just Use a List?

Consider:

    numbers = [1, 2, 3]

    numbers.insert(0, 0)

What happens?

Before

    [1] [2] [3]

        ↓

    Insert at front

        ↓

    [0] [1] [2] [3]

Every existing element must shift one position.

With one million elements, Python must move one million references.

Time complexity:

    O(n)

Now with a deque:

from collections import deque

    numbers = deque([1, 2, 3])

    numbers.appendleft(0)

Internally, no mass shifting is required.

Time complexity:

    O(1)

This difference becomes enormous at scale.

## Adding Elements

### Back
    from collections import deque

    queue = deque()

    queue.append("A")
    queue.append("B")
    queue.append("C")

Result:

    deque(["A", "B", "C"])

### Front
    queue.appendleft("Start")

Result:

    deque(["Start", "A", "B", "C"])

## Removing Elements
### Back
    last = queue.pop()

Removes:

C

### Front
    first = queue.popleft()

Removes:

    Start

Notice the symmetry:

    Add	                    Remove
    append()	            pop()
    appendleft()	        popleft()


## Queue Example (FIFO)

A queue follows First In, First Out.

Imagine processing web requests.

    from collections import deque

    requests = deque()

    requests.append("Request 1")
    requests.append("Request 2")
    requests.append("Request 3")

Processing:

    while requests:
        request = requests.popleft()
        print(request)

Output:

    Request 1
    Request 2
    Request 3

The first request that entered is the first one processed.

Stack Example (LIFO)

A deque can also act as a stack.

from collections import deque

    stack = deque()

    stack.append("A")
    stack.append("B")
    stack.append("C")

Pop:

    print(stack.pop())

Output:

C

Exactly like a list.

Fixed-Length deque

One of deque's most powerful features:

    from collections import deque

    history = deque(maxlen=3)

    history.append(1)
    history.append(2)
    history.append(3)

print(history)

Output:

    deque([1, 2, 3], maxlen=3)

Append another item:

    history.append(4)

    print(history)

Output:

    deque([2, 3, 4], maxlen=3)

The oldest element is automatically discarded.

This is extremely useful.

## AI Engineering Examples
1. Sliding Window

Streaming predictions:

    from collections import deque

    recent_losses = deque(maxlen=100)

    recent_losses.append(loss)

The deque always keeps only the latest 100 losses.

2. Chat History
    chat = deque(maxlen=20)

    chat.append(user_message)
    chat.append(ai_response)

Only the most recent conversations are retained.

3. Sensor Data
    temperatures = deque(maxlen=60)

    temperatures.append(current_temperature)

Always keep the last minute of readings.

4. Breadth-First Search (BFS)

You'll learn BFS in Level 2.

Professionals write:

from collections import deque

    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            queue.append(neighbor)

Using a list here would make BFS significantly slower on large graphs because removing the first element from a list is O(n).

## Rotating a deque
    from collections import deque

    d = deque([1, 2, 3, 4])

    d.rotate(1)

    print(d)

Output:

    deque([4, 1, 2, 3])

Rotate left:

    d.rotate(-2)

Useful for scheduling algorithms and circular buffers.



Notice the trade-off.

Lists are excellent for random indexing:

numbers[500]

A deque is not optimized for repeatedly accessing elements in the middle.

Common Mistakes
Using a list as a queue
    queue = []

    queue.append(item)
    queue.pop(0)

This works.

But pop(0) shifts every remaining element.

Professional code:

from collections import deque

    queue = deque()

    queue.append(item)
    queue.popleft()
Using deque for Random Access

Avoid:

    queue[50000]

A list is the better choice when you frequently need arbitrary indexing.

Professional Patterns

## Rolling Average
from collections import deque

window = deque(maxlen=5)

for value in stream:
    window.append(value)

    average = sum(window) / len(window)

## Undo History
undo_stack = deque()

undo_stack.append(state)

previous = undo_stack.pop()


## Task Scheduler

tasks = deque()

tasks.append(task)

next_task = tasks.popleft()

Exactly how many schedulers work internally.
