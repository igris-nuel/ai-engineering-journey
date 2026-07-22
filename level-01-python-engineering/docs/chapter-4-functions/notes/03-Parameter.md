# Lesson 3 — Parameters

This lesson is surprisingly important.

Most Python developers use the words parameter and argument interchangeably.

Technically, they're different.

If you're interviewing for a Python or AI Engineering role, you should know the difference instinctively.

## Start with a Mental Model

Imagine a hotel.

Before any guests arrive, the hotel has empty rooms.

    Room 101
    Room 102
    Room 103

The rooms already exist.

They simply don't contain anyone yet.

Now guests arrive.

    Room 101 ← Alice
    Room 102 ← Bob
    Room 103 ← Charlie

The room isn't the guest.

The room is merely a place where a guest can stay.

Parameters are like those rooms.

Arguments are like the guests.

Today's lesson is only about the rooms.

## What Is a Parameter?

Consider

    def greet(name):
        ...

Notice something.

No one has called this function yet.

There is no actual data.

There is only

name

## What is name?

It is not a string.

It is not an object.

It is not holding any value.

It is simply a placeholder.

Python records:

"Whenever someone calls this function, I will create a local name called name."

That's all.

## Parameters Are Part of the Function's Blueprint

Think back to the function object.

Inside it is information like:

    bytecode
    defaults
    globals
    name

Another thing stored is the parameter list.

Conceptually:

    Function Object

    ├── name
    ├── bytecode
    ├── defaults
    ├── globals
    └── parameters
        │
        └── name

Notice something.

The parameter itself is metadata.

It isn't a variable yet.

## When Does a Parameter Become a Variable?

Only when the function is called.

Before the call:

    def square(number):
        ...

Conceptually:

    Function Object

    parameter:

    number

Nothing exists in any execution frame.

Now suppose someone calls it.

    square(5)

Python creates

    Execution Frame

    number ─────► 5

Now number is a genuine local variable.

Before the call, it was merely part of the function's description.

## Parameters Live in the Function Definition

Suppose

    def add(a, b):
        ...

Conceptually:

    Function Object

    Parameters

    a

    b

Those names are stored inside the function object.

No execution frame exists.

No namespace exists.

No objects are attached.

## Parameters Are Not Objects

This is subtle.

Many beginners think

    def hello(name):

creates a string called name.

It doesn't.

Nothing exists except the function object.

The parameter is simply an instruction saying:

"When called, create a local name called name."

## Why Python Does It This Way

Imagine Python immediately created variables for every parameter.

    def predict(model, image, threshold):
        ...

Suppose the function is never called.

Creating variables would waste memory.

Instead Python waits.

Only when the function executes does it allocate an execution frame and create those names.

This is lazy and efficient.

## AI Engineering Connection

Consider a PyTorch training function.

    def train(model, optimizer, loader):
        ...

At import time:

no model exists
no optimizer exists
no loader exists

Only the blueprint exists.

Hours later, after you've loaded data and initialized the neural network, the framework finally calls

train(...)

Only then are those parameter names bound to actual objects.

This design lets frameworks define behavior long before the data is available.

## Common Misconception

Many people think this happens:

    Function Definition

            ↓

    Create parameter variables

            ↓

    Wait for call

It doesn't.

The real process is

    Function Definition

            ↓

    Store parameter metadata

            ↓

    (wait)

            ↓

    Function Call

            ↓

    Create execution frame

            ↓

    Create local namespace

            ↓

    Bind parameter names to objects

That distinction matters.

## Mental Model

Definition Time

    Function Object

    parameter:

         data

          ↓

    (No variable exists.)

    ──────────────

    Call Time

    Execution Frame

    data ─────► object

The parameter becomes a variable only during execution.

