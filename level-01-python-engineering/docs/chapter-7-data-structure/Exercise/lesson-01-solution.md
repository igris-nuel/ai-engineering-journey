# Exercises
## Exercise 1 — Mental Model

In your own words:

Why is a Python list better described as a container of references rather than a container of objects?
How is a list similar to a namespace?
Why can a list contain integers, strings, functions, and even other lists without any special handling?

## Exercise 2 — Predict the Output

Without running the code, determine the output and explain why.

A
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[-1])
print(numbers[1:3])
B
letters = ["A", "B", "C", "D"]

print(letters[:2])
print(letters[2:])
print(letters[:])
C
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])
print(matrix[1][0])

## Exercise 3 — Write Code
Program 1 — Student Scores

Create a list of five student scores.

Print:

The first score.
The last score.
The middle three scores using slicing.
Program 2 — Mixed Data

Create a list containing:

An integer
A float
A string
A boolean
Another list

Loop through the list and print each item.

Program 3 — Matrix

Create this matrix:

1 2 3
4 5 6
7 8 9

Store it as a nested list.

Print:

5
9
2

using indexing only.