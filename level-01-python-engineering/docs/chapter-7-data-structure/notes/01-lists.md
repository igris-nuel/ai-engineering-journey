# Lesson 1 — Lists

Most Python courses start with:

"A list is a collection of items."

That definition is technically correct.

But it tells you almost nothing.

We want to answer deeper questions:

    Why do lists exist?
    Why are they fast?
    Why are some operations slow?
    How are they stored in memory?
    Why are lists different from tuples?
    Why do NumPy arrays exist if Python already has lists?

Those answers matter to an AI engineer.

## First Mental Model

A Python list is not a box full of objects.

It is better to think of it as:

An ordered container of references to objects.

Notice the wording.

Not:

    "Container of objects."

Instead:

    "Container of references."

This connects directly to everything we've learned in Chapters 2–4.

Consider:

    numbers = [10, 20, 30]

A beginner imagines:

    numbers
    │
    ▼
    +----+----+----+
    |10  |20  |30  |
    +----+----+----+

That isn't how Python thinks about it.

The real mental model is closer to:

    numbers
        │
        ▼
    +-------+-------+-------+
    |   •   |   •   |   •   |
    +-------+-------+-------+
        │       │       │
        ▼       ▼       ▼
        10      20      30

The list stores references.

The integer objects live elsewhere on the heap.

This should feel familiar.

It's exactly how variables work.

Variables don't contain objects.

Lists don't either.

Both contain references.

Let's Prove It Conceptually

    name = "Alice"

    people = [name]

Question:

Did Python duplicate "Alice"?

No.

The list simply stores another reference to the same string object.

Exactly like another variable would.

## Mutability

Lists are mutable.

Meaning:

The container itself can change.

    numbers = [1, 2, 3]

    numbers.append(4)

The list object is still the same object.

Its internal contents changed.

This is exactly what "mutable" means.

By contrast:

    text = "Hello"

    text += "!"

Strings are immutable.

Python creates a new string object.

You've already learned why in Chapter 2.

## Indexing

Lists preserve order.

Every element has an index.

    letters = ["A", "B", "C", "D"]

    print(letters[0])
    print(letters[2])

Output:

A
C

Indexing starts at 0.

Why?

Because internally, Python computes the memory offset from the beginning of the list.

Conceptually:

    address_of_first_element + index

Zero means:

"No offset."

You'll appreciate this even more when we study arrays in Computer Science.

## Negative Indexing

Python also supports:

    letters = ["A", "B", "C", "D"]

    print(letters[-1])
    print(letters[-2])

Output:

D
C

Negative indices count backward.

Very convenient.

## Slicing

Suppose:

    numbers = [10, 20, 30, 40, 50]

You can write:

    print(numbers[1:4])

Output:

    [20, 30, 40]

The rule is:

    [start : stop]

Start is included.

Stop is excluded.

Think of it as:

Take everything

FROM here

UP TO (but not including)

there.

Examples

    numbers = [10, 20, 30, 40, 50]

.

    print(numbers[:3])

Output

    [10, 20, 30]

.

    print(numbers[2:])

Output

    [30, 40, 50]

.

    print(numbers[:])

Output

    [10, 20, 30, 40, 50]

This creates a shallow copy of the list.

Notice how Chapter 2 comes back here.

Lists Can Hold Anything
    data = [
        42,
        "hello",
        3.14,
        True
    ]

Python allows mixed types.

Because every element is just another reference.

Even functions.

    def greet():
        print("Hello")


    actions = [greet]

    actions[0]()

Output:

    Hello

Remember:

Functions are objects.

Even lists.

    matrix = [
        [1, 2],
        [3, 4]
    ]

print(matrix[1][0])

Output:

3

This becomes important when working with tensors later.

## Iterating

The most common pattern:

    fruits = ["Apple", "Banana", "Orange"]

        for fruit in fruits:
            print(fruit)

Output:

Apple
Banana
Orange

Or with indices:

    fruits = ["Apple", "Banana", "Orange"]

    for index, fruit in enumerate(fruits):
        print(index, fruit)

Output:

    0 Apple
    1 Banana
    2 Orange

You'll use enumerate() constantly.

## Real AI Example

Imagine preprocessing images.

    images = [
        "cat.jpg",
        "dog.jpg",
        "bird.jpg"
    ]

    for image in images:
        print(f"Processing {image}")

Later, you'll replace the strings with actual tensors.

The pattern stays the same.

## Why Lists Matter

You'll encounter them everywhere:

    Dataset samples
    Mini-batches
    Layers
    Tokens
    Predictions
    Metrics
    Training history

They're one of Python's fundamental building blocks.

