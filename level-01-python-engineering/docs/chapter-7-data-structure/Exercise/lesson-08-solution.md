# Exercises
## Exercise 1 — Mental Model

In your own words:

Why is Counter more expressive than manually counting with a dictionary?

How does defaultdict differ from a normal dictionary?

Why is namedtuple easier to work with than a plain tuple?

When would ChainMap be preferable to merging dictionaries?

## Exercise 2 — Professional Code

Given:

from collections import Counter

    languages = [
        "Python",
        "Go",
        "Python",
        "Rust",
        "Go",
        "Python",
    ]

Write code to:

Count the occurrences of each language.

Print the two most common languages.

Print the count for "Go".

## Exercise 3 — Grouping Data

Given:

    employees = [
        ("AI", "Alice"),
        ("Backend", "Bob"),
        ("AI", "Carol"),
        ("Frontend", "Dave"),
    ]

Use defaultdict(list) to produce:

    {
        "AI": ["Alice", "Carol"],
        "Backend": ["Bob"],
        "Frontend": ["Dave"],
    }

## Exercise 4 — AI Engineering

Suppose you're building an LLM evaluation pipeline. Millions of predictions are generated, each labeled "correct" or "incorrect".

Explain:

Why is Counter a natural choice for tracking prediction counts?

Why might defaultdict(list) be useful for grouping prediction errors by category?

Why do these specialized containers make production AI code easier to maintain than manually managing dictionaries?