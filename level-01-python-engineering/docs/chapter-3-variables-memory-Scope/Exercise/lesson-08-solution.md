# Exercises

As before, don't run the code. Reason from the mental model.

## Exercise 1 — When Are Default Arguments Created?

In your own words:

When are default argument objects created?
Where are they stored?
Why aren't they recreated every function call?

Default arguments are created exactly once when the Python interpreter reads the function definition, not when you run the function. 

They are stored inside the function object itself . 

Python evaluates them at definition time to save time and memory. Recreating them every single time would slow down your code and consume extra memory, they are being referenced in the function, so every they are being reused

## Exercise 2 — Following the Object

Consider:

    def collect(x, items=[]):
        items.append(x)
        return items

Now imagine:

collect(1)
collect(2)
collect(3)

Without running the code, answer:

How many list objects are created?
How many function objects exist?
Why does each call "remember" the previous values?
Which object owns the reference to the default list?


List objects created: 1 list object. It is made when the function is defined.

Function objects exist: 1 function object.

Why each call "remembers" previous values: Every time you call the function without providing an items argument, Python points to the exact same list in memory. Appending to the list alters this single object.

Who owns the reference: The function object itself owns the reference to this default list

## Exercise 3 — Why None Works

Consider the pattern:

def collect(x, items=None):
    if items is None:
        items = []

    items.append(x)
    return items

Explain:

Why does this create a fresh list each time?
When is the new list actually created?
Why doesn't the function object keep reusing it?

Using if items is None: avoids the shared-list problem because None is a permanent, unchanging (immutable) marker.

Fresh list created each time: The function checks if the variable items points to the None marker. If it does, the code explicitly creates a brand-new, empty list [].

When created: The new list is created at runtime (when the function actually runs), not when the function is defined.

Why no reuse: Because the list is created inside the function body at runtime, it becomes a distinct local variable for that specific call. Future calls will trigger the if block again, making another fresh list

## Exercise 4 — Architecture Thinking

Imagine an AI preprocessing function:

    def preprocess(image, history=[]):
        ...

This function is called millions of times during training.

Conceptually explain:

What kind of bug could this introduce?
Why might the bug be difficult to notice?
Why is this especially dangerous for machine learning experiments?

Kind of bug: The history list becomes a shared memory log across all calls. If an image modifies the default history, that data "sticks" to the function object.

Difficult to notice: The function might work correctly the first few times you run it (while the list is still short). The bug only becomes obvious later, as the list grows uncontrollably large.

Dangerous for ML: In machine learning, preprocessing steps need to happen exactly the same way every time. If data from a previous image accidentally leaks into the current image's processing history, it will skew your data and cause your model to learn incorrect patterns.

## Exercise 5 — Challenge

A developer says:

"Python should simply recreate default arguments every time a function is called. That would eliminate this problem."

Evaluate this idea.

Discuss the trade-offs in terms of:

performance,
consistency,
immutable defaults,
language design.

Would it solve one problem while introducing others? Why?


Performance: Recreating complex lists, dictionaries, or custom objects every single time a function runs requires more processing power and slows down the program.

Consistency: Python creates variables when a function is defined so it can pre-read and quickly run the code. Changing this would violate core rules of how the Python interpreter works.

Immutable defaults: If you use a simple default (like a string or number, which do not change), recreating them every time wastes resources. The current system is highly efficient for these safe defaults.

Language design: Python's design philosophy encourages you to create mutable objects inside the function so it is clear to other programmers that a new object is being made.