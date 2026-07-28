# Exercises
## Exercise 1 — Rewrite with Comprehensions

Rewrite the following using list comprehensions.

A
    numbers = [1, 2, 3, 4]

    result = []

    for number in numbers:
        result.append(number * 3)
B
    words = ["Apple", "", "Banana", "", "Orange"]

    result = []

    for word in words:
        if word:
            result.append(word.lower())
C
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    flat = []

    for row in matrix:
        for value in row:
            flat.append(value)


## Exercise 2 — Explain the Mental Model

In your own words:

Why is a list comprehension more than just "shorter syntax"?

What is the conceptual difference between:

filtering with if at the end, and

using if...else in the expression?

Why should very complex workflows usually be written as regular loops instead of giant comprehensions?

## Exercise 3 — Write Professional Code
Program 1 — Image Normalization

Given:

    pixels = [0, 64, 128, 255]

Create a new list where each pixel is normalized to the range 0.0–1.0.

Use a list comprehension.

Program 2 — Active Users

Given:

    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False},
        {"name": "Carol", "active": True},
    ]

Create a list containing only the names of active users.

Program 3 — Hyperparameter Grid

Create every combination of:

    Learning rates: [0.1, 0.01, 0.001]
    Batch sizes: [16, 32]

Store the combinations as tuples in a list using a nested comprehension.

