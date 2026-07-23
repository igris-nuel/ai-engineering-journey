# Lesson 5 — Duck Typing

Let's begin with a question.

Suppose you write:

    def greet(name):
        print(name.upper())

What kind of object must name be?

A beginner might answer:

"It must be a string."

That seems reasonable.

But Python says:

Not necessarily.

A Different Way of Thinking

Many languages ask:

"What type is this object?"

Python usually asks:

"Can this object do what I need?"

This is the heart of Duck Typing.

The Famous Quote

You may have heard:

"If it walks like a duck and quacks like a duck, treat it as a duck."

In programming this means:

If an object behaves correctly, Python doesn't care what its declared type is.

Behavior matters more than labels.

First Example
    def print_length(item):
        print(len(item))

Can this function accept a list?

    numbers = [1, 2, 3]

Yes.

Can it accept a string?

    name = "Alice"

Yes.

Can it accept a tuple?

    coordinates = (10, 20)

Yes.

Can it accept a dictionary?

    person = {"name": "Alice"}

Yes.

Why?

Not because they're the same type.

They aren't.

Instead,

they all support

    len(...)

The behavior is what matters.

Notice Something

Python never asks:

    if type(item) == list:

before calling

len(item)

It simply tries to use the object.

If the object supports the operation,

everything works.

Another Example
    def make_upper(text):
        return text.upper()

Will this work?

    "alice"

Yes.

Will this work?

    "My Name"

Yes.

Will this work?

    100

No.

Why?

    Because integers don't have

    upper()

Python doesn't reject the integer because it isn't a string.

It rejects it because it lacks the required behavior.

## Behavior Over Identity

Think about this.

These objects are all different.

    "hello"

    ["a", "b"]

    {"x": 1}

    (1, 2)

Different types.

Different memory layouts.

Different purposes.

Yet they all answer one question:

"How many elements do you contain?"

using

    len(...)

This shared behavior makes them interchangeable for many functions.

## Real AI Example

Imagine writing:

    def count_samples(dataset):
        return len(dataset)

Could dataset be

    a list?
    a tuple?
    a pandas DataFrame?
    a NumPy array?
    a PyTorch Dataset?

Yes.

Why?

Because all of them implement the behavior required by len().

Your function doesn't care about their concrete types.

## What Python Actually Does

When Python evaluates

len(item)

it doesn't think

Is this a list?

Instead it asks something closer to:

Can this object tell me its length?

If yes,

the call succeeds.

Otherwise,

Python raises an error.

Compare With a Strictly Typed Mindset

Imagine writing:

    If object is List:
        ...

    Else if object is Tuple:
        ...

    Else if object is String:
        ...

    Else if object is DataFrame:
        ...

    Else if object is Tensor:
        ...

    Else if object is Dataset:
        ...

This becomes a maintenance nightmare.

Every time a new compatible type appears,

you must modify your function.

Duck Typing avoids this.

Bad Python
    if isinstance(data, list):
        process(data)

Later someone passes

    numpy_array

Even though it behaves perfectly,

your function rejects it.

Better Python

Just use it.

process(data)

If the object supports the required behavior,

everything works.

If not,

Python naturally raises an exception.

This Doesn't Mean "Ignore Types"

This is an important distinction.

Duck Typing does not mean

Every object works everywhere.

It means

Write your code around the behaviors you need, not around specific concrete types.

## PyTorch Example

Consider

optimizer.step()

Does PyTorch ask

if type(optimizer) == SGD:

No.

Why?

Because there are many optimizers.

    SGD
    Adam
    RMSProp
    AdamW

They all implement

step()

The training loop simply calls

optimizer.step()

It doesn't care which optimizer object it receives.

This is classic Duck Typing.

Another AI Example

Imagine:

    def save(model):
        model.save()

Could this work with

    TensorFlow models?
    scikit-learn models?
    your own custom model?

Yes—

as long as they all provide a compatible save() method.

The function depends on behavior, not inheritance.

## The Mental Model

Think of an electrical outlet.

A lamp.

A phone charger.

A laptop charger.

Different manufacturers.

Different designs.

Different internal circuits.

But if they all have the correct plug,

they work.

Python cares about the plug.

Not the manufacturer.

## Why This Makes Python Extensible

Suppose a new ML library is released tomorrow.

If its dataset implements

len(dataset)

and

dataset[index]

many existing Python functions will work immediately.

No modifications required.

That's an incredibly powerful ecosystem design.

The Trade-off

Duck Typing has enormous flexibility.

But it also shifts some errors to runtime.

This will fail only when executed:

    number = 42

    number.upper()

Output:

    AttributeError

The mistake isn't caught before execution.

Python assumes you know what you're doing until proven otherwise.

## Modern Python

Today, Python also supports

    type hints
    static analysis
    tools like mypy and pyright

These improve developer experience.

But they do not replace Duck Typing.

Duck Typing remains part of Python's core philosophy.

## AI Engineering Perspective

Nearly every major AI framework embraces Duck Typing.

Examples include:

    NumPy arrays
    pandas DataFrames
    PyTorch tensors
    TensorFlow tensors
    Hugging Face datasets

They often expose similar behaviors, allowing generic utilities to work across different implementations.

This flexibility is one reason Python became the dominant language for AI.

## Mental Model

Don't think:

"This function accepts lists."

Think:

"This function accepts any object that behaves like a sequence."

Don't think:

"This function accepts a PyTorch optimizer."

Think:

"This function accepts any object that knows how to perform step()."

That shift in thinking is what makes Python code feel elegant and reusable.

## Key Takeaways
Python emphasizes behavior over concrete type.

Objects are accepted based on what they can do, not what they are called.

Duck Typing enables reusable, extensible code.

It reduces unnecessary type checks.

Most AI libraries are designed around this philosophy.

