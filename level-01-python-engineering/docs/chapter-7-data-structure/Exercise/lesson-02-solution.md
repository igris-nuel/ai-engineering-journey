# Exercises
## Exercise 1 — Mental Model

In your own words:

Why is indexing a list O(1)?
Why is append() described as amortized O(1) instead of always O(1)?
Why is insert(0, value) much slower than append(value)?

## Exercise 2 — Professional Code

Rewrite each snippet in a more Pythonic way.

A

result = []

for item in new_items:
    result.append(item)

B

for i in range(len(names)):
    print(names[i], scores[i])

C

users = sorted(users)

Rewrite it so the original list is modified in place instead.

## Exercise 3 — Reason About Complexity

Without running any code, state the time complexity and explain why.

numbers.append(100)
numbers.pop()
numbers.insert(0, 100)
100 in numbers
numbers[500]

## Exercise 4 — AI Engineering

You have a dataset with 10 million image paths stored in a list.

Explain:

Why iterating through the list is appropriate.
Why repeatedly inserting new images at the beginning would be inefficient.
Why checking whether a path exists using in may become a bottleneck.
Which future data structure (that we'll study later) would be better for fast membership tests, and why.


