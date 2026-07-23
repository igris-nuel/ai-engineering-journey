Exercises
Exercise 1 — Construction vs Mutation

In your own words:

Why doesn't int("42") change the string object?
What does int() actually do?
Why is constructing a new object safer than changing the old one?
Exercise 2 — Following the Objects

Consider:

text = "123"

number = int(text)

Without running the code:

How many objects exist afterward?
Which names point to which objects?
Does the string still exist?
Why?
Exercise 3 — Following the Timeline

Conceptually describe the complete sequence when Python executes:

items = [1, 2, 3]

coords = tuple(items)

Explain:

What object already exists?
Which callable object is invoked?
What new object is created?
Why doesn't the list change?
Exercise 4 — AI Engineering Thinking

Suppose an AI pipeline reads:

"42"

from a CSV file.

Later it executes:

age = int(age)

Explain:

Why isn't the original CSV data modified?
Why is constructing a new integer object the correct design?
Why is this important when multiple parts of an AI system may still rely on the original textual data?
