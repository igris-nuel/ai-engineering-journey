## Lesson 2 — List Internals & Professional Usage


## Part 1 — Lists Are Dynamic Arrays

This is probably the most important fact about Python lists.

A Python list is implemented as a dynamic array.

Notice the wording.

Not:

Linked List

Not:

Tree

Not:

Hash Table

It is a dynamic array.

Imagine memory like this:

Address

    1000
    1008
    1016
    1024
    1032
    1040

A Python list tries to reserve contiguous memory.

Example

    numbers = [10, 20, 30]

Conceptually:

    numbers

    ↓

    +------+------+------+
    |  •   |  •   |  •   |
    +------+------+------+

Those boxes sit next to one another.

Each box contains a reference.

Not the object itself.

Why Contiguous Memory Matters

Suppose you want:

    numbers[500]

Python can compute its location instantly.

Conceptually:

    base_address

    +

    500 × pointer_size

No searching.

No walking through nodes.

Just arithmetic.

That's why indexing is extremely fast.

Time complexity:

Index lookup

    O(1)

Constant time.

Whether the list has

    10 elements

    or

    10 million elements.

Why append() Is Usually Fast

Consider

    numbers = []

    numbers.append(10)
    numbers.append(20)
    numbers.append(30)

Many beginners imagine:

    append()

    ↓

    allocate new array

    ↓

    copy everything

    ↓

    repeat

That would be terrible.

Python doesn't do that.

Instead,

Python allocates extra capacity.

Imagine

    Capacity = 8

    Used = 3
    +----+----+----+----+----+----+----+----+
    | •  | •  | •  |    |    |    |    |    |
    +----+----+----+----+----+----+----+----+

Notice the empty slots.

Appending simply fills one.

    O(1)

When full

Python grows the array.

Conceptually

Capacity

    4

    ↓

    8

    ↓

    16

    ↓

    32

    ↓

    64

This is called overallocation.

Python intentionally allocates slightly more memory than needed.

Why?

To avoid reallocating every append.

## Professional Insight

People often say

    append() is O(1)

More accurately:

    append() is amortized O(1).

Occasionally,

Python must allocate a larger block and copy references.

That single append is expensive.

But averaged across many appends,

the cost is constant.

## Why insert(0, value) Is Slow

Suppose

    numbers = [10,20,30]

Now

    numbers.insert(0,5)

Python must shift everything.

Before

    10
    20
    30

    ↓

    After

    5
    10
    20
    30

Every reference moves.

Time complexity:

    O(n)

because all following elements must shift one position.

The same applies to

    numbers.pop(0)

Everything shifts left.

This is why Python has deque.

We'll study that later.

## Professional Rule

Append to the end.

Avoid inserting at the beginning repeatedly.

Good

    queue.append(item)

Bad

    queue.insert(0,item)

unless the list is tiny.

## Professional List Methods

Senior engineers don't memorize methods.

They understand what each one costs.

append
    numbers = []

    numbers.append(10)
    numbers.append(20)
    numbers.append(30)

Used constantly.

extend

Instead of

    a = [1,2]

    for x in [3,4]:
        a.append(x)

Write

    a = [1,2]

    a.extend([3,4])

Cleaner.

Faster.

AI Example

    batch = []

    batch.extend(new_samples)
    insert
    numbers.insert(2,99)

Rare.

Usually avoid if performance matters.

pop
    last = stack.pop()

Excellent.

Implements a stack naturally.

remove
    users.remove(current_user)

Removes by value.

Not index.

clear
    cache.clear()

Instead of

    cache = []

Notice the difference.

clear() empties the existing list object.

Rebinding creates a new list object.

That distinction matters if other references point to the same list.

## Sorting

Professional Python rarely writes custom sorting loops.

Instead:

    users.sort()

        Or

    sorted(users)

Difference?

    users.sort()

Modifies the original list.

Returns

None
    sorted(users)

Returns a new sorted list.

Leaves original untouched.

Sorting Objects

Suppose

    employees = [
        {"name":"Alice","salary":8000},
        {"name":"Bob","salary":5000},
        {"name":"Carol","salary":9000}
    ]

Professional code

    employees.sort(
        key=lambda employee: employee["salary"]
    )

Or

    highest_paid = sorted(
        employees,
        key=lambda employee: employee["salary"],
        reverse=True
    )

You'll see this everywhere.

AI Example

Sorting model predictions.

    predictions = [
        ("cat",0.92),
        ("dog",0.76),
        ("bird",0.61)
    ]

    predictions.sort(
        key=lambda prediction: prediction[1],
        reverse=True
    )

Very common.

Membership
    if user in users:
        ...

Works.

But remember

Lists search sequentially.

    O(n)

Later,

you'll see why

Sets

are much faster.

    enumerate()

## Professional Python

    for index, token in enumerate(tokens):
        print(index, token)

Instead of

    for i in range(len(tokens)):
        print(i,tokens[i])

The first version is clearer and avoids repeated indexing.

## zip()

Suppose

    names = ["Alice","Bob","Carol"]

    scores = [80,95,88]

Instead of

    for i in range(len(names)):
        print(names[i],scores[i])

Professionals write

    for name, score in zip(names, scores):
        print(name, score)

Cleaner.

More Pythonic.

## AI Example

    for image, label in zip(images, labels):
        train(image, label)

You'll see this constantly.

List Comprehensions (Preview)

Instead of

    squares = []

    for x in range(10):
        squares.append(x*x)

Professionals write

    squares = [
        x * x
        for x in range(10)
    ]

Same result.

More expressive.




