# Lesson 4 — Arguments

This lesson is short, but it fixes one of the most common misconceptions in Python.

By the end of it, you'll never confuse parameters and arguments again.

We Already Know Parameters

We ended the last lesson with this function.

    def greet(name):
        ...

What is name?

It is a parameter.

It is part of the function's blueprint.

It is not an object.

It is not a variable yet.

It simply tells Python:

"When someone calls me, create a local variable named name."

Now let's look at the other side.

## What Is an Argument?

Suppose we write

greet("Alice")

### What is "Alice"?

It is the argument.

An argument is the actual object supplied by the caller.

Notice the difference.

Function Definition

    name

     ↓

    Parameter

    -------------------------

    Function Call

    "Alice"

       ↓

    Argument

A parameter belongs to the function.

An argument belongs to the caller.

### Parameters Live Here
    def greet(name):

Inside the function object.

Conceptually

    Function Object

    Parameters

    name

### Arguments Live Somewhere Else

Suppose

    user = "Alice"

    greet(user)

Before the call happens

    Global Namespace

    user ─────► "Alice"

The argument already exists.

Nothing new is created because of the call.

The caller simply says

"Use this object."

## The Function Does NOT Receive a Copy

This is where many beginners make a mistake.

They imagine

    Caller

    "Alice"

      ↓

    COPY

      ↓

    Function

That is not what happens.

Python simply reuses the same object.

Conceptually

    Before Call

    Global Namespace

    user ─────► "Alice"

After Call

Global Namespace

    user ─────► "Alice"
                    ▲
                    │
    Local Namespace │

    name────────────┘

Both names point to the same object.

Nothing is copied.

## The Timeline

Suppose

    user = "Alice"

    greet(user)

Python conceptually performs these steps.

### Step 1

Find the function object.

    greet

      ↓

    Function Object

### Step 2

Create an execution frame.

Execution Frame

### Step 3

Look at the function's parameter list.

Parameter

name

### Step 4

Take the argument object.

"Alice"

### Step 5

Bind them together.

Execution Frame

name ─────► "Alice"

That's it.

No copying.

No cloning.

No duplication.

Multiple Arguments

Suppose

    def add(a, b):
        ...

Call

    x = 10
    y = 20

    add(x, y)

Before the call

Global Namespace

    x ─────► 10

    y ─────► 20

After the call

Global Namespace

       x ─────► 10
                 ▲
                 │
    Local a ─────┘

       y ─────► 20
                 ▲
                 │
    Local b ─────┘

Again

Nothing is copied.

Only new names are created.

## Why This Matters

Suppose the argument is tiny.

5

No big deal.

Now imagine it's

    a 40 GB AI model
    a 10 GB dataset
    a massive NumPy array
    a PyTorch tensor with billions of parameters

If Python copied those every function call…

Your computer would become unusable.

Instead Python shares the object.

This makes function calls extremely cheap.

Parameters and Arguments Are Different Things

This is the interview definition.

    A parameter is the placeholder recorded in the function definition.

    An argument is the actual object supplied when calling the function.

Example

    def greet(name):
        ...

Parameter

    name

Now

    user = "Alice"

    greet(user)

Argument

    "Alice"

Notice something.

The argument is not the variable user.

The argument is the object referenced by user.

This distinction becomes very important in the next lesson.

## Common Misconception

People often say

"I'm passing the variable."

Not exactly.

Conceptually, Python evaluates the expression inside the parentheses.

greet(user)

The expression user evaluates to the string object "Alice".

That object becomes the argument.

The variable name itself is not transferred into the function.

## Mental Model
Caller

        user

         │
         ▼

      "Alice"

──────────────

Function Object

parameter

name

──────────────

Call

↓

Execution Frame

name ─────► "Alice"

The caller supplies objects.

The function creates names.

Then Python binds those names to those objects.

## Why This Lesson Exists

Most developers casually say

"Pass the parameter."

Technically that's wrong.

You pass arguments.

Parameters receive arguments.

It sounds like a small distinction, but it makes the next lesson—Python's Argument Passing Model—much easier to understand.


