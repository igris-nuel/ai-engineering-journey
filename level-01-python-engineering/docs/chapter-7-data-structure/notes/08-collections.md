## The collections Module

The collections module is part of Python's standard library. It contains data structures designed to solve common problems more efficiently or more cleanly than the basic built-ins.

Some of its most important classes are:

    collections
    │
    ├── Counter
    ├── defaultdict
    ├── OrderedDict
    ├── namedtuple
    ├── ChainMap
    ├── UserDict
    ├── UserList
    └── deque   ← (covered separately next)

In modern Python, Counter and defaultdict are used constantly. OrderedDict is much less common now because normal dictionaries preserve insertion order.

1. Counter

Imagine you have:

    words = [
        "python",
        "ai",
        "python",
        "ml",
        "ai",
        "python",
    ]

A beginner might write:

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

It works.

Professionals write:

    from collections import Counter

    words = [
        "python",
        "ai",
        "python",
        "ml",
        "ai",
        "python",
    ]

    counts = Counter(words)

print(counts)

Output

    Counter({
        "python": 3,
        "ai": 2,
        "ml": 1
    })

Counter is a Dictionary

Mentally,

    Counter

       ↓

    Dictionary

       ↓

    key → count

It behaves like a dictionary.

    print(counts["python"])

returns

3

## Most Common Elements

One of Counter's best features.

from collections import Counter

    text = [
        "apple",
        "banana",
        "apple",
        "apple",
        "orange",
    ]

    counts = Counter(text)

print(counts.most_common(2))

Output

[
    ("apple", 3),
    ("banana", 1)
]

This is extremely useful in NLP.

## AI Example

Vocabulary frequency.

from collections import Counter

    tokens = [
        "the",
        "cat",
        "sat",
        "the",
        "cat",
    ]

    vocab = Counter(tokens)

print(vocab)

This is the first step of many tokenization pipelines.

2. defaultdict

Suppose you want to group students by department.

A beginner writes:

    students = {}

for department, name in data:
    if department not in students:
        students[department] = []

    students[department].append(name)

It works.

Professionals write:

    from collections import defaultdict

    students = defaultdict(list)

    students["AI"].append("Alice")
    students["AI"].append("Bob")
    students["Backend"].append("Carol")

    print(students)

Output

    defaultdict(
        list,
        {
            "AI": ["Alice", "Bob"],
            "Backend": ["Carol"],
        }
    )
Why It Works

When a missing key is accessed,

students["AI"]

defaultdict automatically creates

    []

and stores it.

No need to check

    if key not in dictionary

## Counting Example

    from collections import defaultdict

    counts = defaultdict(int)

    for letter in "banana":
        counts[letter] += 1

    print(counts)

Output

{
    "b": 1,
    "a": 3,
    "n": 2
}

Notice

int()

returns

0

So missing values automatically start at zero.

## AI Example

Grouping predictions.

from collections import defaultdict

predictions = defaultdict(list)

predictions["cat"].append(0.97)
predictions["cat"].append(0.91)
predictions["dog"].append(0.88)

Much cleaner than checking whether "cat" already exists.

3. namedtuple

Sometimes a tuple becomes hard to read.

    user = (
        101,
        "Alice",
        "alice@test.com",
    )

print(user[2])

What is index 2?

You have to remember.

Instead:

    from collections import namedtuple

    User = namedtuple(
        "User",
        ["id", "name", "email"],
    )

    user = User(
        101,
        "Alice",
        "alice@test.com",
    )

print(user.email)

Output

    alice@test.com

A namedtuple is still immutable and lightweight like a tuple, but much more readable.

Today, many projects use dataclass instead, which you'll learn later.

4. OrderedDict

Historically:

    from collections import OrderedDict

was needed when insertion order mattered.

Example:

from collections import OrderedDict

data = OrderedDict()

    data["a"] = 1
    data["b"] = 2

Before Python 3.7, normal dictionaries did not guarantee insertion order.

Today:

data = {}

data["a"] = 1
data["b"] = 2

already preserves insertion order.

So OrderedDict is now mainly used for backward compatibility or for a few specialized methods.

5. ChainMap

Imagine you have configuration from multiple sources:

defaults = {
    "timeout": 30,
}

user = {
    "timeout": 60,
}

environment = {
    "debug": True,
}

Instead of merging them:

combined = {
    **defaults,
    **user,
    **environment,
}

You can write:

from collections import ChainMap

config = ChainMap(
    environment,
    user,
    defaults,
)

print(config["timeout"])

Output

60

ChainMap searches each mapping in order until it finds the key.

This is useful for layered configuration systems.

When Should You Use These?

    Problem	                                Tool

    Count frequencies	                     Counter
    Group values	                         defaultdict(list)
    Automatic numeric counting	             defaultdict(int)
    Lightweight immutable records	         namedtuple
    Combine configuration dictionaries	     ChainMap
    Preserve order (legacy code)	         OrderedDict


## Real AI Engineering Examples
### Word Frequency
    from collections import Counter

    tokens = tokenizer(text)

    word_counts = Counter(tokens)

## Batch Statistics
    from collections import defaultdict

    losses = defaultdict(list)

    losses["train"].append(0.23)
    losses["train"].append(0.18)
    losses["validation"].append(0.31)

## Organizing Dataset Labels
    from collections import defaultdict

    dataset = defaultdict(list)

    dataset["cat"].append(image1)
    dataset["cat"].append(image2)
    dataset["dog"].append(image3)

## Configuration
    from collections import ChainMap

    config = ChainMap(
        command_line,
        environment,
        defaults,
    )

This pattern is common in CLI tools and servers.

## Performance Notes

Counter and defaultdict are built on top of Python's highly optimized dictionary implementation. Their average lookup and insertion performance is still O(1).

Their advantage isn't speed over a normal dictionary—it's clearer, less error-prone code.

Professional Advice

Prefer Counter over manual counting

Instead of:

    counts = {}

    for item in items:
        ...

Use:

    counts = Counter(items)

Prefer defaultdict when grouping

Instead of repeated existence checks:

    if key not in d:
        d[key] = []

Use:

    d = defaultdict(list)
Use the right abstraction

Choosing Counter immediately tells another engineer, "I'm counting occurrences."

Choosing defaultdict(list) immediately tells them, "I'm grouping related values."

Good code communicates intent.

