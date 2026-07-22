# Exercises

As always, don't run code. Build the answer from the mental model.

## Exercise 1 — What Is a Lambda?

In your own words:

What does a lambda expression create?
Is a lambda a different kind of function?
Why is it often called an anonymous function?

## Exercise 2 — Lambda vs def

Conceptually compare:

creating a function with def,
creating a function with lambda.

Explain:

What do they have in common?
What is the main conceptual difference?
Which one automatically binds a name?


## Exercise 3 — Following the Timeline

Imagine a lambda is passed into another function.

Without writing code, explain the complete timeline:

When is the function object created?
What gets passed?
When is an execution frame created?
When does the function body actually execute?


## Exercise 4 — AI Engineering Thinking

Suppose an AI data pipeline lets users specify a tiny transformation that is used exactly once while loading data.

Conceptually explain:

Why a lambda may be more appropriate than defining a full named function.
Why the pipeline can treat the lambda exactly like any other function.
Why understanding that a lambda is "just a function object" makes it easier to understand frameworks like Pandas, PyTorch, and scikit-learn.