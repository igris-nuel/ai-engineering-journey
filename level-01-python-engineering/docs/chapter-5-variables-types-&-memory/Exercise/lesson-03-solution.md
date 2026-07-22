# Exercises
## Exercise 1 — Objects All the Way Down

In your own words:

What is a type object?
Is int just a keyword?
What two major responsibilities does a type object have?
Why do many objects share the same type object instead of each object storing its own behavior?
## Exercise 2 — Following the Chain

Without running the code:

numbers = [1, 2, 3]

Describe the complete chain from:

the name,
to the object,
to the type object.

Where does the data live?

Where does the behavior (like append) live?

## Exercise 3 — Comparing Objects

Suppose you create:

a = [1]

b = [2]

c = [3]

Conceptually answer:

How many list objects exist?
How many list type objects exist?
Why don't three separate copies of append() exist?
## Exercise 4 — AI Engineering Thinking

Imagine a deep learning framework creates one million tensor objects during training.

Conceptually explain:

Does each tensor carry its own implementation of matrix multiplication?
Where is that behavior actually stored?
Why is this architecture important for memory efficiency and maintainability?
How does it relate to Python's own list, dict, and int objects?