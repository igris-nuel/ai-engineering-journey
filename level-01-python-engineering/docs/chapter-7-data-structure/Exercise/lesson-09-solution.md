

Exercises
Exercise 1 — Mental Model

In your own words:

Why is inserting at the front of a list O(n)?
Why can a deque perform appendleft() and popleft() in O(1)?
Why is a deque not ideal for random indexing?
When would you choose a deque over a list?
Exercise 2 — Professional Code

Using deque, write code to:

Create an empty queue.
Add "Task A", "Task B", and "Task C".
Process tasks one by one using popleft().
Continue until the queue is empty.
Exercise 3 — Sliding Window

Create a deque with maxlen=5.

Write code that appends the numbers:

10, 20, 30, 40, 50, 60, 70

Without running it, explain:

What will the final deque contain?
Why are the first two values removed automatically?
Exercise 4 — AI Engineering

Suppose you're building a real-time fraud detection system that evaluates incoming transactions.

Explain:

Why is a deque with maxlen=1000 a good structure for storing the latest transactions?
Why would a list be less suitable if old transactions are constantly removed from the front?
Give two other AI or systems applications where a deque is the most appropriate data structure.