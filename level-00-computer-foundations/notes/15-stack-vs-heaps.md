# Lesson 15
## Stack vs Heap (Conceptual)

Imagine you have only one big block of RAM.

Could we simply throw everything into that block?

Program instructions
Function calls
Variables
Objects
Lists
Dictionaries
Images
AI model parameters

Why not?

Because different kinds of data have different lifetimes and access patterns.

That's why memory is organized.

Think About an Office

Imagine you're working in an office.

You have two places to put things.

Your Desk

Things you're actively using.

today's notebook
your keyboard
a cup of coffee

Easy to reach.

Temporary.

The Storage Room

Things you don't need every second.

filing cabinets
archived documents
extra chairs
printer paper

Much larger.

Not as immediate.

A running program is organized similarly.

### The Stack

Think of the stack as:

The workspace for active function calls.

It stores information that is needed right now.

Conceptually:

+-------------+
| function C  |
+-------------+
| function B  |
+-------------+
| function A  |
+-------------+

Notice the name:

Stack.

Like a stack of plates.

### The Heap

The heap is different.

It stores objects whose lifetime is not tied directly to a single function call.

Conceptually:

+----------------------+
| Integer Object       |
+----------------------+

+----------------------+
| List Object          |
+----------------------+

+----------------------+
| Dictionary Object    |
+----------------------+

+----------------------+
| Image                |
+----------------------+

Objects can remain there as long as something still refers to them.

### Why Two Different Areas?

Imagine every function call had to search through millions of objects.

Function calls would become slow.

Instead:

temporary execution information goes on the stack,
dynamically allocated objects go on the heap.

Each area is optimized for its purpose.

Function Calls

Suppose we have:

    def add(a, b):
        c = a + b
        return c

    x = add(2, 3)

Conceptually:

Before calling add:

Stack

    +---------+
    | main    |
    +---------+

When add() is called:

    +---------+
    | add()   |
    +---------+
    | main    |
    +---------+

The new function is placed on top.

Returning

After:

return c

the function finishes.

Its stack frame disappears.

Back to:

    +---------+
    | main    |
    +---------+

Everything local to add() is gone.

### Stack Frame

Each function call gets its own stack frame.

Think of a stack frame as a folder containing:

parameters
local variables
return address
bookkeeping information

Example:

    def greet(name):
        message = "Hello"

Conceptually:

Stack Frame

name

message

return address

other information

Every function gets its own folder.

Recursion

Suppose:

    def countdown(n):
        if n == 0:
            return
        countdown(n - 1)

Calling:

countdown(3)

creates:

    +--------------+
    | countdown(0) |
    +--------------+
    | countdown(1) |
    +--------------+
    | countdown(2) |
    +--------------+
    | countdown(3) |
    +--------------+
    | main         |
    +--------------+

Every recursive call creates another stack frame.

Stack Overflow

What happens if recursion never ends?

    def f():
        f()

The stack grows:

+------+
| f()  |
+------+
| f()  |
+------+
| f()  |
+------+
| f()  |
+------+
| f()  |
+------+

Eventually...

No space remains.

Python raises:

RecursionError

On lower-level languages, this may become a stack overflow.

### What Lives on the Heap?

Now consider:

    numbers = [1, 2, 3]

The list object is created on the heap.

Conceptually:

Heap

    +----------------+
    | List Object    |
    | 1              |
    | 2              |
    | 3              |
    +----------------+

The variable:

numbers

does not contain the list itself.

It contains a reference to the list object.

We'll make this precise in Level 1.

Why Put Objects on the Heap?

Suppose a function creates a huge image:

    image = load_image(...)

The image might be:

500 MB

If it were placed directly on the stack:

Every function call would require copying enormous amounts of memory.

That would be terribly inefficient.

The heap is designed for large, dynamically sized objects.

Stack Is Fast

The stack is extremely efficient because it follows one simple rule:

Last In, First Out (LIFO)

Add to the top.

Remove from the top.

No searching.

No fragmentation.

Very fast.

Heap Is Flexible

The heap allows:

objects of different sizes,
objects created at unpredictable times,
objects that outlive a single function.

But this flexibility comes with extra bookkeeping.

Lifetime

This is one of the biggest ideas in programming.

Suppose:

    def test():
        x = 5

When test() returns:

Its stack frame disappears.

But what about objects on the heap?

They remain as long as something still refers to them.

This distinction is fundamental.

## Python's Perspective

In CPython:

function call information is stored on the call stack,
Python objects are allocated on the heap,
variables (names) are associated with objects through references.

This is why understanding both regions matters.

##  AI Connection

Imagine training a neural network.

The model may contain:

billions of weights,
tensors,
gradients,
optimizer state.

These are enormous data structures.

They live on the heap (or on GPU memory in deep learning frameworks).

The stack only tracks the active function calls managing them.

Common Misconceptions
x "Everything lives on the stack."

No.

x "Everything lives on the heap."

No.

x "The stack stores all variables."

Not quite.

In Python, local names are part of a function's execution state, but the Python objects they refer to are generally heap-allocated.

We'll refine this in Level 1.

## Mental Model

Imagine a restaurant.

The stack is the waiter's tray.

Small.

Fast.

Temporary.

The heap is the kitchen.

Large.

Flexible.

Long-lived.

The waiter doesn't carry the entire kitchen.

He carries references to what's needed right now.



## Key Insights

- The stack manages active function calls.
- Each function call creates a stack frame.
- The heap stores dynamically allocated objects.
- Stack memory is fast and follows LIFO.
- Heap memory is flexible and allows objects to outlive function calls.
- Python generally stores objects on the heap while function execution state is tracked through stack frames.

Commit:

git add .
git commit -m "Complete stack vs heap lesson"
git push
👨‍🏫 Supervisor's Preview

After this lesson, Chapter 1 is complete.

Then we begin Level 1: Python Fundamentals.

And here's the exciting part: you are not going to learn Python the way most people do.

Most courses start with:

x = 10

and say:

"This is a variable."

We're going to ask a much deeper question:

What actually happens inside CPython, in memory, when you execute x = 10?

Everything you've learned over the past lessons has been laying the groundwork for answering that question properly.


