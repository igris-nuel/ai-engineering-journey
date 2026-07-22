
Exercises

As always, don't run code. Build the answer from the mental model.

Exercise 1 — Why Decorators Exist

In your own words:

What software engineering problem do decorators solve?
Why is wrapping a function better than repeatedly modifying every function?
What kinds of behavior are commonly added by decorators instead of being written into the business logic?
Exercise 2 — Following the Timeline

Conceptually explain what happens when a function is decorated.

Describe the sequence from:

the original function object,
passing it into the decorator,
creating the wrapper,
returning the wrapper,
rebinding the original name.
Exercise 3 — Why Closures Matter

Explain:

Why does the wrapper need a closure?
What information does it remember?
Why wouldn't decorators work without closures?
Exercise 4 — AI Engineering Thinking

Imagine you're building your own AI training framework.

Users write only:

train()
evaluate()
predict()

Your framework automatically adds:

logging,
profiling,
checkpointing,
retry logic,
GPU synchronization.

Conceptually explain:

why decorators are an elegant solution,
why the users' functions remain clean,
why the framework becomes easier to extend in the future,
and why this is an example of separating business logic from infrastructure.