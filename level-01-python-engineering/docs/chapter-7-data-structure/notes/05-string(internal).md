# Lesson 5 — Strings (Internals)

### First Principle

A string is an immutable sequence of Unicode characters.

    name = "Alice"

Mentally:

Global Namespace

    name
    │
    ▼
    +----------------+
    |   "Alice"      |
    +----------------+

Exactly like every other Python object.

The string lives on the heap.

The name points to it.

## Strings Are Immutable

This is probably the single most important fact.

    name = "Alice"

    name[0] = "B"

Error.

Why?

Because strings never change after creation.

Instead,

Python creates an entirely new string whenever you appear to "modify" one.

Example

    name = "Alice"

    name = "Bob"

Did Python modify "Alice"?

No.

It created

"Bob"

and rebound the name.

Exactly like integers.

Exactly like tuples.

## Why Immutability?

Suppose strings were mutable.

    username = "admin"

    config = username

    log = username

Three names now reference one string.

If one piece of code did

username[0] = "A"

every reference would instantly change.

Admin

Imagine debugging that in a million-line codebase.

Disaster.

Immutable strings eliminate this entire class of bugs.

## Strings Are Sequences

word = "Python"

Conceptually

    P
    y
    t
    h
    o
    n

Each character has an index.

word[0]

word[1]

word[-1]

Nothing new is created here.

Python simply reads from the existing string object.

## Slicing

word = "Python"

    part = word[0:3]

Question:

Does part point into the original string?

No.

Python creates a new string object.

Original

Python

↓

New

Pyt

Because strings are immutable, sharing writable memory isn't necessary.

Another example

word = "MachineLearning"

    prefix = word[:7]

    suffix = word[7:]

Two entirely new string objects.

Concatenation
    first = "Machine"

    second = "Learning"

    result = first + second

Python cannot modify either original string.

Instead

Machine

    Learning

    ↓

    MachineLearning

A third string object is created.

This becomes important later.

Imagine

    text = ""

    for word in words:
        text += word

Every iteration creates another string.

    A

    AB

    ABC

    ABCD

    ABCDE

Thousands of allocations.

We'll learn professional alternatives shortly.

## Strings Support Iteration

    for char in "Python":
        print(char)

Output

P
y
t
h
o
n

Professionals rely on this constantly.

## Membership
    if "AI" in sentence:
        ...

    Or

    if "@" in email:
        ...

Very common.

    Length
    len(name)

    Returns

    5

Python stores the length internally, so len() is extremely fast.

It doesn't count characters every time you call it.

## Unicode

This is where Python shines.

    english = "Hello"

    japanese = "こんにちは"

    arabic = "مرحبا"

    emoji = "🚀"

All are strings.

Python uses Unicode, not ASCII.

This is one reason Python became so popular for NLP.

## Escape Characters

message = "Hello\nWorld"

Produces

Hello
World

Other common ones

"\t"

"\\"

"\""

You'll use these constantly when building prompts, JSON, and file paths.

## Raw Strings

Very useful.

Instead of

path = "C:\\Users\\Alice\\Desktop"

Write

    path = r"C:\Users\Alice\Desktop"

The r tells Python:

Don't interpret escape sequences.

Professionals use raw strings for

    Windows paths
    Regular expressions
    Some prompt templates

## Common String Methods

Python's string API is enormous.

Let's focus on the methods professionals use daily.

### Lower
    text = "HELLO"

    text.lower()

Produces

"hello"

Notice

text itself is unchanged.

### Upper
    text.upper()

### Strip

One of the most used methods.

name = "   Alice   "

    clean = name.strip()

Useful when reading

    CSV files
    User input
    Configuration files
    APIs

### Replace

    text = "cat"

    text.replace("cat", "dog")

Produces

dog

Again,

new string.

### Startswith

    filename.startswith("IMG")

Common in automation.

### Endswith
    filename.endswith(".jpg")

Very common.

### Split

One of the most important methods.

    sentence = "AI changes everything"

    words = sentence.split()

Produces

    [
        "AI",
        "changes",
        "everything"
    ]

Notice.

A list is created.

Not a tuple.

Split by comma

csv = "Alice,Bob,Carol"

names = csv.split(",")

### Join

One of Python's greatest performance optimizations.

Instead of

    text = ""

    for word in words:
        text += word


## Professionals write

    text = "".join(words)

Why?

Because join() calculates the required memory once and builds the final string efficiently, instead of repeatedly creating intermediate strings.

Example

    words = [
        "Machine",
        "Learning",
        "Engineer"
    ]

    title = " ".join(words)

Result

Machine Learning Engineer

### Find

    email.find("@")

Returns

    position

    or

    -1

### Count

    sentence.count("AI")

Useful for quick statistics.

### F-Strings (Professional Standard)

Old style

name = "Alice"

age = 25

text = name + " is " + str(age)

Messy.

## Professional code

    text = f"{name} is {age}"

Cleaner.

Faster.

More readable.

Formatting

    price = 19.999

    print(f"${price:.2f}")

Output

    $20.00

### Alignment

name = "Alice"

print(f"{name:>10}")

Useful for logs and reports.

## Strings in AI

Prompt building

    prompt = (
        f"Summarize the following:\n\n"
        f"{document}"
    )

### JSON

import json

    payload = json.dumps(data)

### Logging

    print(f"Epoch {epoch}: loss={loss}")

### File names

    filename = f"checkpoint_{epoch}.pt"

### URLs

url = f"{base_url}/users/{user_id}"

### SQL (using parameterized queries, not string concatenation)

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE id = %s
        """,
        (user_id,)
    )

Notice we don't build SQL with f-strings because that can introduce SQL injection vulnerabilities. We'll cover this in detail when we study databases.

### Performance Trap

Bad

    result = ""

    for line in lines:
        result += line

Every iteration creates a new string.

Professional

    result = "".join(lines)

You'll see this pattern in production code constantly.
