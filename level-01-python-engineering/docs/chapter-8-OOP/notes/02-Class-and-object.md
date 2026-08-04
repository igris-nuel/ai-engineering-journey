Lesson 2 — Classes & Objects

This is one of the most misunderstood topics in Python.

Most tutorials say:

"A class is a blueprint."

It's a useful analogy for beginners, but it breaks down quickly.

We'll build the correct mental model.

First Question

What is this?

class User:
    pass

Most people answer:

"It's a class."

True.

But internally?

It is an object.

Let's prove it.

class User:
    pass

print(type(User))

Output:

<class 'type'>

Notice something.

User is an instance of type.

Mental Model

Everything you've learned still applies.

Names point to objects.

User is just another name.

Global Namespace

"User"
   │
   ▼
+------------------+
|  Class Object    |
|------------------|
| __name__         |
| __dict__         |
| __bases__        |
| methods          |
+------------------+

A class is not syntax.

A class is a real object in memory.

Creating a Class

When Python executes:

class User:
    species = "human"

    def greet(self):
        print("Hello")

Conceptually, Python does something like:

Read the class body.
Create a namespace (dictionary).
Store:
{
    "species": "human",
    "greet": <function>,
}
Call type(...).
Produce a class object.
Bind it to the name User.

Think of it like:

Class Definition

↓

Namespace Dictionary

↓

type()

↓

Class Object

↓

User
A Class is a Factory

Now consider:

user = User()

What happens?

Not:

"Python creates a variable."

Instead:

User (Class Object)

↓

Create Instance

↓

Return Instance

↓

Bind to "user"

Exactly like:

numbers = list()

or

items = dict()

Classes are callable objects that create other objects.

Memory Model

After:

class User:
    pass

user = User()

Memory looks like:

Global Namespace

"User" ───────────────┐
                      │
                      ▼
              +----------------+
              | Class Object   |
              +----------------+
                      │
         creates      │
                      ▼
"user" ─────────────► +----------------+
                      | Instance Object|
                      +----------------+

Notice:

The class and the instance are different objects.

One Class, Many Objects
u1 = User()
u2 = User()
u3 = User()

Memory:

           User (Class)

           │
           │ creates
           ▼

+---------+ +---------+ +---------+
|   u1    | |   u2    | |   u3    |
+---------+ +---------+ +---------+

One class.

Many independent objects.

Exactly like:

list()

list()

list()

Each call creates a different list.

Identity
u1 = User()
u2 = User()

Question:

Are they the same object?

No.

Each call creates a new instance.

Conceptually:

User()

↓

Object A

Another call:

User()

↓

Object B

Different identities.

Professional Example — PyTorch

When you write:

import torch.nn as nn

model = nn.Linear(10, 5)

You're doing exactly this:

model = Linear(...)

Linear is a class.

model is an instance.

Later:

optimizer = Adam(...)

Again:

Class → Instance.

Frameworks are full of class instantiation.

Professional Example — FastAPI
from fastapi import FastAPI

app = FastAPI()

Here:

FastAPI

is a class.

app

is an object.

Professional Example — SQLAlchemy
Session()

Creates:

Session Object

Every database session is its own instance.

PocketFlow Example

Imagine:

class Schedule:
    pass

Now:

salary = Schedule()

school_fees = Schedule()

rent = Schedule()

All are schedules.

Each represents a different payment schedule.

If you pause one:

salary.pause()

The others shouldn't pause.

Why?

Because each schedule is a separate object with its own state.

Classes are Objects Too

This is where Python becomes interesting.

You already know:

x = 10

10 is an object.

You learned:

def greet():
    ...

Functions are objects.

Now:

class User:
    ...

Classes are also objects.

In Python:

Integers

↓

Objects

Functions

↓

Objects

Lists

↓

Objects

Classes

↓

Objects

Everything follows the same object model.

Objects Have Types
type(10)

↓

int
type([])

↓

list
type(User())

↓

User

Notice the pattern.

Instances know which class created them.

Code Review
Beginner

A class is a blueprint.

Acceptable, but incomplete.

Senior

A class is a first-class object that defines how instances are created and how they behave. It stores shared behavior (methods) and class-level attributes, and is itself an instance of type.

That explanation matches Python's implementation more closely.

Common Misconception

People think:

User

is "special."

It's not.

It behaves like other objects.

For example:

Alias = User

u = Alias()

This works because you're simply binding another name to the same class object.

The name doesn't matter; the object does.

This reinforces a principle you've already learned:

Names are labels. Objects hold the actual behavior and data.

