# Lesson 6 — Type Conversion

Most beginners think this line:

x = int("42")

means:

"Change the string into an integer."

That isn't what Python does.

The First Question

Suppose we have

    text = "42"

What is "42"?

It is a string object.

It lives on the heap.

The name

text

points to it.

Memory looks like this:

    Global Namespace

    text
    │
    ▼
    "42" (str object)

Nothing surprising.

Now we write

    number = int(text)

What happens?

Many people imagine:

    "42"

    ↓

    42

as if Python transformed one object into another.

That mental model is wrong.

Objects Are Immutable

Strings are immutable.

Python cannot open the string object and rewrite it into an integer.

Objects never change their fundamental type.

Instead...

Python creates a new object.

The Real Timeline

### Step 1

Python evaluates

text

and gets a reference to the existing string object.

### Step 2

Python calls the type object

    int(...)

Remember from the previous lesson:

Types are callable.

int is a type object.

Calling it asks:

"Please construct an integer from this object."

### Step 3

The int constructor reads the string.

It interprets

"42"

as a decimal number.

### Step 4

A brand-new integer object is created.

42

This object is completely separate from the string.

### Step 5

The name

number

is bound to the new integer.

Final memory:

    Global Namespace

    text ─────────────► "42"

    number ───────────► 42

Notice:

The string still exists.

Nothing was modified.

## Type Conversion Is Construction

Think about building a statue.

Suppose you have a photograph.

You use it to sculpt a statue.

Did the photograph become the statue?

No.

The photograph remains.

You simply used it as input to create something new.

Python conversions work exactly like this.

Another Example
    value = float(5)

Did the integer become a float?

No.

Timeline:

    5 (int object)

    ↓

    float() reads it

    ↓

    5.0 (new float object)

Two different objects now exist.

## Why This Matters

Suppose

    a = "100"

    b = int(a)

Afterward

a

is still

"100"

It is not secretly an integer now.

Only

b

references the integer object.

## Constructors vs Conversion

This is an important distinction.

When you write

    int(...)

you're calling a constructor.

Sometimes the constructor creates an object from scratch:

    int()

    produces

    0

Sometimes it constructs from another object:

    int("15")

Sometimes it simply returns an existing object when appropriate.

The important idea is:

The type object decides what to do.

Successful Conversion
    int("123")

works because

the string represents a valid integer.

Failed Conversion
    int("hello")

fails.

Why?

Because Python cannot interpret

"hello"

as a valid integer.

The constructor raises

ValueError

Notice:

Nothing happens to the original string.

It remains exactly as it was.

More Examples

String to float

    price = float("19.95")

Creates

19.95

Integer to string

    text = str(500)

Creates

"500"

List from tuple

    numbers = list((1, 2, 3))

Creates

a brand-new list object.

The tuple is unchanged.

Tuple from list

    coords = tuple([1, 2, 3])

Creates

a brand-new tuple.

The list remains exactly as it was.

Memory Picture
    values = [1, 2, 3]

    copy = tuple(values)

Memory:

    values
    │
    ▼
    [1,2,3]

    copy
    │
    ▼
    (1,2,3)

Different objects.

Different types.

Same conceptual data.

## AI Engineering Example

Suppose your dataset comes from a CSV.

Everything arrives as strings.

    "25"

    "180"

    "3.14"

Before training,

you convert them:

    age = int(age)

    height = float(height)

Are the strings modified?

No.

Python constructs numeric objects

from the textual representations.

The original CSV data stays unchanged.

## Why This Design Is Good

Imagine if

    int("42")

actually changed the string object.

What if another variable also referenced that string?

Suddenly,

code in another part of the program would see an integer instead of a string.

That would violate Python's object model and make programs unpredictable.

Constructing a new object avoids this entirely.

Conversion Is Not Mutation

Compare these.

Mutation:

    numbers.append(4)

The existing list changes.

Conversion:

    tuple(numbers)

The list does not change.

A new tuple appears.

This is a huge conceptual distinction.

### Conversion Is Also Not Rebinding

Suppose

    text = "50"

    text = int(text)

What happened?

Not conversion in place.

Timeline:

    text

    ↓

    "50"

    ↓

    int() constructs

    ↓

    50

    ↓

    text now points elsewhere

The original string object still existed until no references remained.

Then garbage collection could eventually reclaim it.

## Mental Model

Never think:

Python changes one object into another.

Think:

Python asks a type object to construct a new object using an existing object as input.

That single sentence explains nearly every conversion in Python.

## AI Engineering Perspective

Conversion happens constantly:

    CSV → integers
    JSON → dictionaries
    Lists → NumPy arrays
    NumPy arrays → PyTorch tensors
    Tensors → NumPy arrays
    Float32 → Float16
    CPU tensors → GPU tensors

Although the mechanisms vary, the core idea remains:

One representation is used to construct another representation.

Understanding this now will make frameworks like NumPy and PyTorch much easier to learn later.

## Key Takeaways
Type conversion does not mutate objects.

Type conversion usually constructs a new object.

Types (int, float, str, list, tuple) are callable constructors.

The original object remains unchanged.

Names are simply rebound to new objects if you assign the result.

