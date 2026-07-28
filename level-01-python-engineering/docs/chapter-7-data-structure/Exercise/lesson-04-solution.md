# Exercises
## Exercise 1 — Packing and Unpacking

Without running the code, explain what happens conceptually.

    point = 12, 30

    x, y = point

Answer:

What object is created?
What names exist after unpacking?
How many references point to the tuple after unpacking?

## Exercise 2 — Lists vs Tuples

For each scenario, decide whether a list or a tuple is the better choice, and explain why.

    A shopping cart that users can add to and remove from.
    A GPS coordinate (latitude, longitude).
    A neural network tensor shape (32, 3, 224, 224).
    A list of log messages collected during program execution.
    A dictionary key representing (model_name, batch_size, learning_rate).

## Exercise 3 — Professional Code

Write code for each task.

A. Swap Values

Create two variables a and b and swap them using tuple unpacking.

B. Multiple Return Values

Write a function min_max(numbers) that returns both the minimum and maximum value from a list. Then call it and unpack the result into two variables.

C. Dictionary with Tuple Keys

Create a dictionary where the keys are (row, column) coordinates and the values are characters.

Example:

    {
        (0, 0): "S",
        (0, 1): ".",
        (1, 0): "#",
    }

Retrieve and print one value using a tuple key.