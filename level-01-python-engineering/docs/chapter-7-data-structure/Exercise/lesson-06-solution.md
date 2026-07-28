# Exercises
## Exercise 1 — Mental Model

In your own words:

Why is a dictionary called a mapping?
Why must keys be hashable?
Why are lists invalid dictionary keys?
Does a dictionary store objects or references to objects?

## Exercise 2 — Professional Code

Given

student = {
    "name": "Alice",
    "age": 21,
}

Write code to:

Add "course": "AI Engineering"
Update the age to 22
Safely retrieve "email" with a default value of "Unknown"
Print every key-value pair using the professional iteration pattern.

## Exercise 3 — Dictionary Comprehension

Given

numbers = range(1, 11)

Write a dictionary comprehension that creates:

{
    1: 1,
    2: 4,
    3: 9,
    ...
    10: 100
}

Then write another that includes only the even numbers.

## Exercise 4 — AI Engineering

Imagine an API returns:

response = {
    "model": {
        "name": "Llama",
        "layers": 32,
        "hidden_size": 4096,
    },
    "status": "ready",
}


Without running code, explain:

How many dictionary objects exist?
How would you access the number of layers?
Why are nested dictionaries a natural fit for JSON and API responses?