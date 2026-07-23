Exercises
Exercise 1 — Why Reuse Objects?

In your own words:

Why does Python reuse immutable objects when possible?
Why is this safe?
Why wouldn't the same strategy work for mutable objects?
Exercise 2 — Following the Lifetime

Suppose:

def build():
    values = [1, 2, 3]

Conceptually explain:

When is the list created?
When does values disappear?
Under what condition can Python reclaim the list?
Why doesn't Python need the programmer to manually free the memory?
Exercise 3 — Sharing vs Copying

Suppose an AI model occupies 40 GB of memory.

Conceptually explain:

Why is sharing references dramatically more efficient than copying the model?
Why would copying every object make Python unusable for AI?
How does Python's object model naturally support efficient large-scale systems?
Exercise 4 — Bringing Everything Together

Using only concepts (not syntax), explain how these ideas fit into one complete mental model:

Objects
Names
References
Types
Constructors
Function Calls
Execution Frames
Scope
Object Lifetime
Memory Optimization

Imagine you're explaining Python's runtime model to a new AI engineer who wants to understand what really happens in memory.