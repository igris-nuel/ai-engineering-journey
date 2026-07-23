Exercises
Exercise 1 — The Mental Model

In your own words:

What does an if statement actually do?
Why does only one branch of an if/elif/else chain execute?
Why is indentation part of Python's syntax rather than just formatting?
Exercise 2 — Predict the Output

Without running the code, determine what will be printed and explain why.

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")

print("Finished")
score = 91

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")

else:
    print("Fail")
x = 100

if x > 50:
    print("Large")

if x > 80:
    print("Very Large")

Why are both messages printed?

Exercise 3 — Trace the Execution

Consider:

logged_in = True
premium = False

if logged_in:
    print("Welcome")

    if premium:
        print("Premium Features")

print("Home")

Describe the complete execution timeline, starting from evaluating logged_in and ending with the final print().

Exercise 4 — AI Engineering Thinking

A machine learning pipeline has the following requirements:

If no model is loaded, stop immediately.
If a model is loaded but the dataset is missing, report the problem.
If both are available, start training.

Write a small Python program that implements this logic using if, elif, and else.

New challenge: This is the first exercise where I want you to actually write code rather than only reason about it. From this point onward, you'll be writing progressively more Python alongside the conceptual exercises.