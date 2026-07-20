# Exercises

As always, don't run the code. Reason from the mental model we've built.

Exercise 1 — The Core Idea

In your own words:

What problem do closures solve?

Why can't Python simply destroy every local variable when a function returns?

Think beyond "because the inner function needs it."

What language design principle is Python preserving?

Exercise 2 — The Mental Model

Suppose conceptually:

def outer():
    x = "AI"

    def inner():
        print(x)

    return inner

Answer conceptually:

Does x behave like an ordinary local variable?
Why not?
Is the string copied into inner?
What is actually shared?
Why is sharing better than copying?
Exercise 3 — Architecture Thinking

Imagine Python did not support closures.

Nested functions could exist,

but they could not remember variables from their enclosing scope.

Describe at least four major limitations this would create for:

decorators
callbacks
AI preprocessing pipelines
configuration
asynchronous programming
web frameworks

Don't just describe syntax.

Think about how software architecture itself would change.