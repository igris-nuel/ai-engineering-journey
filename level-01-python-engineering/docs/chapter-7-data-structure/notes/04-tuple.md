# Lesson 4 — Tuples

### First Principle

A tuple is an ordered, immutable sequence.

    point = (10, 20)

    rgb = (255, 120, 0)

    user = ("Alice", 25, True)

Looks similar to a list.

But mentally, don't think:

"List that cannot change."

Instead think:

"Fixed data."

## Why Does Immutability Matter?

Suppose you store a person's birth date.

    birth_date = (2000, 5, 18)

Should someone accidentally do

    birth_date[0] = 2010

Absolutely not.

A birthday is a fact.

Facts should not change.

Tuples express this idea directly.

## Lists Represent Collections

    shopping_cart = [
        "Laptop",
        "Mouse",
        "Keyboard"
    ]

A shopping cart changes.

Add items.

Remove items.

Reorder items.

Lists are perfect.

## Tuples Represent Records

    location = (
        6.5244,
        3.3792
    )

Latitude and longitude form one coordinate.

Changing one accidentally would produce nonsense.

A tuple communicates

"These values belong together."

## Memory

Create a tuple.

    point = (5, 8)

Exactly like a list:

    tuple object lives on the heap
    name lives in a namespace
    name points to tuple object

The difference is internal.

A tuple does not allocate extra space for future growth.

A list must.

Why?

Lists expect:

    append()

    extend()

    insert()

    remove()

Tuples support none of these.

Because their size never changes.

## Tuples Are Smaller

    numbers = [1, 2, 3]

    coords = (1, 2, 3)

The tuple typically occupies less memory than the equivalent list because it doesn't maintain spare capacity for resizing.

When millions of objects exist, this matters.

## Tuples Are Faster

Reading

    point[0]

is extremely fast.

Creating

(1, 2, 3)

is slightly faster than

[1, 2, 3]

Again,

not because Python developers like speed,

but because immutability simplifies implementation.

## Packing

Python automatically packs values into a tuple.

point = 10, 20

No parentheses required.

This creates

(10, 20)

Exactly the same object.

Professionals use this constantly.

## Unpacking

Probably the most common tuple feature.

point = (10, 20)

x, y = point

print(x)
print(y)

Output

10
20

This is called sequence unpacking.

## Professional example

    user = ("Alice", 25)

    name, age = user

Cleaner than

name = user[0]
age = user[1]


## Swapping Variables

One of Python's nicest features.

Instead of

    temp = a
    a = b
    b = temp

Write

    a, b = b, a

What happens conceptually?

Python creates a temporary tuple.

    (b, a)

Then unpacks it.

    a = old_b
    b = old_a

Elegant.

Returning Multiple Values

This is where tuples become essential.

    def divide(a, b):
        quotient = a // b
        remainder = a % b

        return quotient, remainder

Usage

q, r = divide(17, 5)

print(q)
print(r)

Output

3
2

Did Python return two objects?

Not exactly.

Conceptually,

it returned

    (3, 2)

which the caller unpacked.

You'll see this pattern everywhere.

    height, width = image.shape

    loss, accuracy = evaluate(model)

    host, port = server_address
   
## Iterating
    colors = (
        "red",
        "green",
        "blue"
    )

    for color in colors:
        print(color)

Exactly like lists.

## Membership

if "red" in colors:
    print("Found")

Exactly like lists.

## Tuple Methods

Tuples have only two methods.

    numbers = (1, 2, 3, 2)

    numbers.count(2)

    numbers.index(3)

## Why only two?

Because tuples never change.

No

append()

remove()

pop()

extend()


## Nested Tuples

    matrix = (
        (1, 2),
        (3, 4),
        (5, 6)
    )

Common for fixed structures.

## Named Records

Instead of

    student = (
        "Alice",
        22,
        "Computer Science"
    )

Ask yourself:

What is

    student[2]

Without remembering the order, it's unclear.

For richer records, a dataclass or namedtuple (which we'll study later) often provides better readability.

## Tuples as Dictionary Keys

This is one of the biggest reasons tuples exist.

Lists cannot be keys.

    prices = {
        [1, 2]: "value"
    }

Error.

Why?

Because lists can change.

If a key changed after insertion, the dictionary would no longer know where to find it.

Tuples solve this.

    distances = {
        (0, 0): "Origin",
        (10, 20): "City"
    }

Perfectly valid.

## AI Example

## Caching.

    cache = {}

    key = (
        model_name,
        batch_size,
        learning_rate
    )

cache[key] = trained_model

A fixed configuration makes an excellent dictionary key.

## Coordinates

Computer vision

    pixel = (250, 120)

Bounding boxes

    box = (x1,y1,x2,y2)

RGB

    color = (255,128,64)

Tensor Shapes

PyTorch

    shape = (32,3,224,224)

Meaning

    Batch
    Channels
    Height
    Width

Notice something.

Should the tensor shape change accidentally?

Absolutely not.

Tuple.

## Function Arguments

Sometimes APIs accept tuples because they represent one logical value.

    resize(image, size=(224, 224))

The width and height belong together.

## Professional Uses

Returning Multiple Values

    def min_max(values):
        return min(values), max(values)

Enumerate
    names = [
        "Alice",
        "Bob",
        "Carol"
    ]

    for index, name in enumerate(names):
        print(index, name)

enumerate() produces tuples like (index, value), which unpack naturally in the loop.

## Dictionary Iteration

    scores = {
        "Alice": 90,
        "Bob": 82,
    }

    for name, score in scores.items():
        print(name, score)

Each item is a tuple (key, value).

## Sorting

    employees = [
        ("Alice", 25),
        ("Bob", 20),
        ("Carol", 30),
    ]

    employees.sort(key=lambda employee: employee[1])

Very common.

Later, when we study lambda functions, you'll understand this deeply.

When Should You Choose a Tuple?

Use a tuple when:

    The number of elements is fixed.
    The values belong together as one record.
    The object should not change.
    It needs to be hashable (usable as a dictionary key or set element).
    You're returning multiple values from a function.

Choose a list when:

Items will be added or removed.
Order may change.
The collection grows over time.

## Common Beginner Mistake
    student = ("Alice", 25)

    student = ("Bob", 30)

People say:

"But tuples are immutable!"

The tuple wasn't modified.

The name was rebound.

Old tuple:

    ("Alice", 25)

New tuple:

    ("Bob", 30)

Exactly the same distinction we learned with immutable strings and integers.

Objects don't change.

Names can point somewhere else.
