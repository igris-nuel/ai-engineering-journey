# Dictionaries

### First Principle

A dictionary is a mapping.

It maps

     key
      ↓
    value

instead of storing values by position.

A list answers:

    "What is the value at index 3?"

A dictionary answers:

"What is the value associated with this key?"

## Creating Dictionaries

    user = {
        "id": 101,
        "name": "Alice",
        "age": 28,
    }

## Mentally

          user
           │
           ▼

        Dictionary Object

"name" ───► "Alice"

"id" ─────► 101

"age" ────► 28

Notice something.

The dictionary does not contain the objects themselves.

It contains references to them.

Exactly like lists.

## Dictionaries Are Objects

    user = {
        "name": "Alice"
    }

Global Namespace

    user
    │
    ▼

    Dictionary Object
        │
        └────► "Alice"

Same object model we've been using since Chapter 2.

Nothing new.

Only a different internal organization.

## Keys Must Be Hashable

This is the first major rule.

Valid keys:

    user = {
        "name": "Alice",
        1: "one",
        True: "yes",
        (1, 2): "tuple",
    }

Invalid

    bad = {
        [1, 2]: "value"
    }

TypeError

Why?

Because lists are mutable.

Python requires dictionary keys to have a stable identity for lookup.

We'll study hashing in depth when we cover Python internals, but for now remember:

### Dictionary keys must be immutable (or otherwise hashable).

### Access
    user = {
        "name": "Alice",
        "age": 28
    }

    print(user["name"])

### Output

    Alice

Unlike lists,

you're indexing by key instead of integer position.

### Missing Keys

    print(user["email"])

Produces

KeyError

Professional Python rarely writes this blindly.

Instead

    email = user.get("email")

Returns

None

instead of crashing.

With default values

    email = user.get(
        "email",
        "Not Provided"
    )

Much safer.

## Adding Entries

user["country"] = "Nigeria"

Python inserts

    country

       ↓

    Nigeria

into the dictionary.

### Updating

user["age"] = 29

The key already exists.

Python simply changes the value reference.

### Deleting

del user["age"]

The key disappears.

The value object is garbage collected only if nothing else references it.

Exactly the same lifetime rules we've studied.

## Membership

Very common.

    if "email" in user:
        ...

Professional.

Instead of

    if user.get("email"):

because the value could legitimately be None.

## Iteration

    Default iteration

    for key in user:
        print(key)

Produces

name

age

country

### Values

    for value in user.values():
        print(value)

### Keys

for key in user.keys():
    print(key)

## Professional Pattern

Almost everywhere.

    for key, value in user.items():
        print(key, value)

Example

    name Alice

    age 29

    country Nigeria

This is the standard way to iterate over dictionaries.

## Dictionary Comprehensions

Just as we had list comprehensions, we also have dictionary comprehensions.

Basic example:

    squares = {
        x: x * x
        for x in range(6)
    }

print(squares)

Output

    {
        0: 0,
        1: 1,
        2: 4,
        3: 9,
        4: 16,
        5: 25,
    }

### Filtering

even = {
    x: x * x
    for x in range(10)
    if x % 2 == 0
}

Output

    {
        0: 0,
        2: 4,
        4: 16,
        6: 36,
        8: 64,
    }

## Transforming an Existing Dictionary

    prices = {
        "apple": 2,
        "banana": 3,
        "orange": 4,
    }

    discounted = {
        item: price * 0.9
        for item, price in prices.items()
    }

Very common in production code.

## Merging Dictionaries

Python 3.9+

    user = {
        "name": "Alice"
    }

    profile = {
        "country": "Nigeria"
    }

    combined = user | profile

Result

    {
        "name": "Alice",
        "country": "Nigeria"
    }

Older style

    combined = {
        **user,
        **profile,
    }

You'll see both in production.

## Nested Dictionaries

Extremely common.

    user = {
        "name": "Alice",
        "address": {
            "city": "Lagos",
            "country": "Nigeria",
        },
    }

Access

    city = user["address"]["city"]

This mirrors JSON almost perfectly.

Example API response

    response = {
        "user": {
            "id": 101,
            "name": "Alice",
        },
        "status": "success",
    }

This is exactly how REST APIs work.

## Counting with Dictionaries

A professional pattern.

Instead of

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

you'll later learn collections.Counter, but understanding the manual version is important.

## Professional AI Examples
### Model Configuration

    config = {
        "hidden_size": 4096,
        "num_layers": 32,
        "dropout": 0.1,
        "learning_rate": 3e-4,
    }

### Dataset Sample

    sample = {
        "question": "What is AI?",
        "answer": "Artificial Intelligence",
    }

### Hugging Face Tokenizer Output

    encoded = {
        "input_ids": [101, 2023, 2003],
        "attention_mask": [1, 1, 1],
    }

### PyTorch State Dictionary

    state_dict = {
        "layer1.weight": weights,
        "layer1.bias": bias,
    }

You'll see this constantly.

## JSON

Python

    user = {
        "name": "Alice",
        "age": 28,
    }

JSON

    {
    "name": "Alice",
    "age": 28
    }

This is why dictionaries dominate backend development.

## Performance

Dictionary lookup

    user["name"]

is approximately

    O(1)

on average.

Meaning

finding "name" in a dictionary with

    10 items

    100 items

    10,000 items

    1,000,000 items

is still expected to be extremely fast.

We'll rigorously prove why when we study hash tables in Level 2.

## Professional Tips

Prefer .get() for Optional Keys
email = user.get("email")

instead of risking a KeyError.

Iterate Using .items()

Instead of

    for key in user:
        print(key, user[key])

write

    for key, value in user.items():
        print(key, value)

Cleaner and avoids repeated lookups.

Use Meaningful Keys

Avoid

    {
        "a": 1,
        "b": 2,
    }

Prefer

    {
        "username": "alice",
        "created_at": "...",
    }

Readable dictionaries make APIs and AI pipelines much easier to maintain.

