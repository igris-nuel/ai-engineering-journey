Exercises
Exercise 1 — Behavior vs Type

In your own words:

What is Duck Typing?
Why does Python focus on behavior instead of concrete types?
Why is this often more flexible than checking type() or isinstance() everywhere?
Exercise 2 — Following the Behavior

Consider:

def display_length(item):
    print(len(item))

Without running the code:

Why can this function work with a list, tuple, string, or dictionary?
What does Python care about when len(item) is called?
What happens if an object doesn't support the required behavior?
Exercise 3 — API Design

Imagine you're writing:

def train(model):
    model.forward()

Conceptually answer:

Why doesn't the function need to know whether model is a CNN, Transformer, or RNN?
What behavior is the function relying on?
Why does this make your code easier to extend?
Exercise 4 — AI Engineering Thinking

Suppose a new deep learning library is released next year.

Its model objects implement:

forward()
save()
train()

Explain:

Why could many existing Python utilities work with these models immediately?
How does Duck Typing encourage interoperability between libraries?
Why is this philosophy one of the reasons Python dominates AI and scientific computing?