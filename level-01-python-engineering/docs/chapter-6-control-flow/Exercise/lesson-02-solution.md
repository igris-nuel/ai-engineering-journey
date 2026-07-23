
# Exercises
## Exercise 1 — Explain Truthiness

In your own words:

What is truthiness?

Does a list become a Boolean?

What question is Python actually asking when it evaluates if object:?


## Exercise 2 — Predict the Output

Without running the code, determine what will be printed and explain why.

    names = []

    if names:
        print("A")
    else:
        print("B")

  count = 5

    if count:
        print("A")
    else:
        print("B")
text = ""

    if text:
        print("Hello")
    else:
        print("Empty")
value = None

    if value:
        print("Found")
    else:
        print("Missing")
## Exercise 3 — Mental Model

Describe the complete timeline for:

items = ["apple"]

    if items:
        print("Processing...")

Start from:

    Looking up items.
    Retrieving the list object.
    Determining its truth value.
    Choosing the correct branch.
    Executing print().
## Exercise 4 — AI Engineering Thinking

You're writing a data pipeline:

    batch = load_batch()

Compare these two styles:

    if len(batch) > 0:
        train(batch)

and

    if batch:
        train(batch)

Explain:

Why both work.
Why the second is generally preferred in Python.
When you might still choose the first for clarity or to express a specific condition.

In the next lesson, we'll finally start using Boolean values to control execution with if, elif, and else, where you'll begin writing more realistic program logic.