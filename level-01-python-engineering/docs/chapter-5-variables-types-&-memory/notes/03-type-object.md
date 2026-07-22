## Lesson 3 — Type Objects

By the end of the last lesson, we established this fact:

Objects have types. Names do not.

But that immediately raises a deeper question.

When we write:

    x = 10

    print(type(x))

    we get:

    <class 'int'>

What exactly is int?

Is it just a label?

A keyword?

Something built into the compiler?

The answer is much more interesting.

Let's start with code
  x = 10

  print(type(x))

Output:

    <class 'int'>

Now try another one.

    name = "Alice"

    print(type(name))

Output:

    <class 'str'>

Another.

    numbers = [1, 2, 3]

    print(type(numbers))

Output:

    <class 'list'>

We see:

  int
  str
  list

But what are these things?

First Observation

Notice something.

Python prints

    <class 'int'>

not

    <int>

Why the word class?

Because int is itself an object created from the class type.

This is one of Python's most elegant ideas.

Everything Is an Object (Again)

Earlier we said:

Everything is an object.

Most beginners think that means

  integers
  strings
  lists

But Python takes this much further.

Even these are objects:

  int
  str
  list
  dict

Even functions.

Even classes.

Almost everything you interact with in Python is an object.

Let's prove it
  print(type(int))

Output:

    <class 'type'>

Interesting.

Now:

  print(type(str))

Output:

    <class 'type'>

Again.

Now:

print(type(list))

Output:

    <class 'type'>

Again.

Wait...

Let's draw this.

For an integer:

    x = 10

Memory:

    x
    │
    ▼
    10
    │
    ▼
    int
    │
    ▼
    type

There are three layers.

Layer 1

  The name.

  x

Layer 2

  The integer object.

  10

Layer 3

  The type object.

  int

Layer 4

  Even int has a type.

  type

This is called Python's object model.

Everything is connected.

What does the int object actually do?

Imagine Python didn't have int.

Then what would happen here?

  10 + 20

How would Python know

  how to add?
  how to subtract?
  how to print?
  how to compare?

It wouldn't.

Those behaviors are defined by the type object.

Think of it like this.

The object

  10

contains data.

The type object

  int

contains behavior.

So when Python executes

  10 + 20

it conceptually asks

"Hey int, how do two integer objects perform addition?"

The int type provides that implementation.

Another example
  numbers = [1, 2]

The list object stores

  1

  2

But where is

  append()

stored?

Not inside every individual list.

Instead,

the list type object contains the implementation.

That's why every list can do

  numbers.append(3)

without each list carrying its own separate copy of the code.

This saves memory and keeps behavior consistent.

Code Example
    a = [1]

    b = [5]

There are now

two list objects

but only

one list type object.

Diagram:

  a ─────► List Object
              │
              ▼
              list

  b ─────► List Object
              │
              ▼
              list

Both objects share the same behavior.

## Why this is brilliant

Imagine if every list carried its own implementation of

  append
  extend
  insert
  remove
  pop
  reverse
  copy

Every list would waste memory.

Instead,

Python stores behavior once,

inside the shared list type object.

## AI Engineering Example

Suppose you create

  weights1 = Tensor(...)

  weights2 = Tensor(...)

  weights3 = Tensor(...)

Each tensor contains different numerical data.

But every tensor knows how to

  add
  multiply
  move to GPU
  compute gradients

Why?

Not because each tensor stores those algorithms.

Instead,

every tensor shares one common Tensor type that defines those operations.

PyTorch follows the exact same design philosophy as Python.

## Type Objects Are Factories

There's another interesting property.

Remember this:

  x = int("42")

Who creates the integer?

The answer:

The int object.

That's why we say

int is both

  a type description

  and

  a constructor (factory) for integer objects.

Similarly,

  list()

creates a list.

  dict()

creates a dictionary.

  str()

creates a string.

These aren't keywords.

They're callable objects.

## Mental Model

Think of Python like a factory.

                  type
                    │
          ┌─────────┴─────────┐
          │         │         │
        int       list      str
          │         │         │
      creates   creates   creates
          │         │         │
        objects   objects   objects

Objects hold data.

Type objects define behavior and create new objects.

## Why AI Engineers Should Care

When you use

torch.Tensor

or

numpy.ndarray

you're interacting with type objects.

Understanding this makes concepts like:

  methods
  classes
  inheritance
  operator overloading
  PyTorch modules

feel much more natural later.

You'll realize they're all built on the same object model you've been studying.

Key Takeaways
  A name points to an object.
  Every object has a type.
  Types are themselves objects.
  Type objects define behavior.
  Type objects can create new objects.
  Many objects share one type object.

This recursive design is one of Python's defining characteristics.

