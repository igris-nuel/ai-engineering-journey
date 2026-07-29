# Sets
### First Principle

A set is an unordered collection of unique objects.

Unlike a list:

    numbers = [1, 2, 2, 3, 3]

duplicates are allowed.

A set automatically removes duplicates.

    numbers = {1, 2, 2, 3, 3}

    print(numbers)

Output

    {1, 2, 3}

The uniqueness property is the defining characteristic of a set.

## Creating Sets
### Literal syntax
    colors = {"red", "green", "blue"}


### From another iterable

    numbers = set([1, 2, 2, 3, 3, 4])

    print(numbers)

Output

    {1, 2, 3, 4}

Professional Python often converts a list to a set simply to remove duplicates.

### Empty Set

One of the classic interview questions.

This is NOT an empty set.

    empty = {}

It creates

dict

Instead

    empty = set()

creates an empty set.

## Sets Store References

Exactly like every container we've studied.

names = {"Alice", "Bob"}

Mentally

    names
    │
    ▼

    Set Object

    ├────► "Alice"
    └────► "Bob"

The set stores references to objects.

Not copies.

No Indexes

Unlike lists

    numbers = [10, 20, 30]

    numbers[0]

works.

But

    numbers = {10, 20, 30}

    numbers[0]

raises

TypeError

A set has no concept of "first" or "last."

## Membership Testing

This is where sets shine.

    users = {
        "Alice",
        "Bob",
        "Charlie",
    }

    if "Bob" in users:
        print("Found")

This lookup is expected to be extremely fast.

Much faster than checking a large list.

Why?

Consider

    target in huge_list

Python may have to examine many elements before finding the target.

With a set

    target in huge_set

Python uses hashing to jump directly to where the object should be.

Average lookup:

    O(1)

This is one of the biggest reasons sets exist.

## Adding Elements
    users = set()

    users.add("Alice")
    users.add("Bob")

Adding an existing value changes nothing.

    users.add("Bob")

Still

    {"Alice", "Bob"}

No duplicate.

## Removing
    users.remove("Alice")

If missing

    users.remove("John")

raises

KeyError

Safer

    users.discard("John")

No error.

Professional code often prefers discard() when absence is acceptable.

## Iteration
    users = {
        "Alice",
        "Bob",
        "Charlie",
    }

    for user in users:
        print(user)

Remember

The order is not guaranteed.

Never write code that depends on the iteration order of a set.

## Set Comprehensions

Exactly like list comprehensions.

    squares = {
        x * x
        for x in range(6)
    }

    print(squares)

Output

{0, 1, 4, 9, 16, 25}

## Filtering

evens = {
    x
    for x in range(20)
    if x % 2 == 0
}

## Set Operations

This is where sets become incredibly powerful.

Suppose

    backend = {
        "Alice",
        "Bob",
        "Charlie",
    }

    ai = {
        "Charlie",
        "David",
        "Alice",
    }

### Union

Everything.

    backend | ai

Result

    {
        "Alice",
        "Bob",
        "Charlie",
        "David",
    }

## Intersection

Only common elements.

backend & ai

Output

    {
        "Alice",
        "Charlie",
    }

One of the most useful operations in production code.

## Difference

Items only in the first set.

    backend - ai

Output

    {
        "Bob",
    }

## Symmetric Difference

Elements that appear in exactly one set.

    backend ^ ai

Output

    {
        "Bob",
        "David",
    }

## Professional Examples

### Removing Duplicates

Instead of

    emails = [
        "a@test.com",
        "b@test.com",
        "a@test.com",
    ]

write

    unique = set(emails)
Fast Lookup

Instead of

    blocked = [
        "spam.com",
        "evil.com",
    ]

Professional

    blocked = {
        "spam.com",
        "evil.com",
    }

Checking

    if domain in blocked:
        ...

is much faster.

### Comparing Two Datasets

Suppose

    training_ids = {
        1, 2, 3, 4
    }

    validation_ids = {
        3, 4, 5
    }

Duplicates between datasets?

    overlap = training_ids & validation_ids

    print(overlap)

Output

    {3, 4}

This kind of check is common before training a machine learning model to ensure your training and validation sets don't accidentally share samples.

### Vocabulary Building

In NLP

    words = [
        "cat",
        "dog",
        "cat",
        "bird",
    ]

Vocabulary

    vocab = set(words)

Output

    {
        "bird",
        "cat",
        "dog",
    }

This is often the first step in text preprocessing.

### Tracking Visited Nodes

Graph algorithms

visited = set()

visited.add(node)

    if node in visited:
        ...

You'll write this pattern many times in Level 2 when we study graphs.

### Frozen Sets

Sometimes you need an immutable set.

    permissions = frozenset({
        "read",
        "write",
    })

You cannot add or remove elements.

permissions.add("delete")

raises

AttributeError

A frozenset is hashable, which means it can itself be used as a dictionary key or stored inside another set.

## Common Mistakes
### Mistake 1

Expecting order.

    users = {"Alice", "Bob", "Charlie"}

    for user in users:
        ...

Never assume which user comes first.

### Mistake 2

Trying to index.

    users[0]

Impossible.

### Mistake 3

Using mutable objects.

    bad = {
        [1, 2],
    }

Produces

TypeError

Exactly the same rule as dictionary keys.

## Performance
    Operation	            List	                        Set
    Membership (in)	        O(n)	                        O(1) average
    Add	                    O(1) amortized	                O(1) average
    Remove	                O(n)	                        O(1) average

This is why choosing the right data structure matters. A simple switch from a list to a set can turn a slow algorithm into a fast one.

## Professional Tips
    Use a set when you need uniqueness
    seen_users = set()
    Use a list when order matters
    tasks = []
    Don't convert back and forth repeatedly

Avoid

    for item in items:
        if item in set(items):
            ...

You're rebuilding the set on every iteration.

Instead

    item_set = set(items)

for item in items:
    if item in item_set:
        ...

Build it once, reuse it.

### Use Set Algebra

Instead of nested loops like

    common = []

    for x in list1:
        if x in list2:
            common.append(x)

write

    common = set(list1) & set(list2)

This is shorter, clearer, and usually much faster.

