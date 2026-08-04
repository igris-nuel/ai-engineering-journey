## Lesson 5 — Constructors

You've already written this many times:

    class User:

        def __init__(self, name):
            self.name = name

    user = User("Pelumi")

Today we'll answer:

What actually happens when you call User("Pelumi")?

## Step 1 — The Class is Called

Notice this syntax:

User("Pelumi")

Question:

Why can you "call" a class?

Because classes are callable objects.

Just like:

len(data)

or

print("Hello")

a class can also be called.

## Step 2 — Python Calls __new__

Before __init__ runs, Python does:

User.__new__(User)

Its job is simple:

Allocate memory.
Create a new User object.
Return that object.

At this point, the object exists.

But it's empty.

Conceptually:

+------------------+
| User Instance    |
|------------------|
| name = ?         |
+------------------+
Step 3 — Python Calls __init__

Now Python passes that new object into:

User.__init__(obj, "Pelumi")

Inside:

def __init__(self, name):
    self.name = name

Python performs:

obj.name = "Pelumi"

Now:

+------------------+
| User Instance    |
|------------------|
| name = Pelumi    |
+------------------+
Step 4 — Return the Object

Finally:

user = User("Pelumi")

binds

user

to that initialized object.

Complete Timeline
User("Pelumi")

↓

Class is called

↓

__new__()

↓

Allocate memory

↓

Create object

↓

__init__()

↓

Initialize attributes

↓

Return object

↓

Bind to "user"

This is the complete lifecycle.

Why Two Methods?

Why not one?

Because creating an object and initializing it are different responsibilities.

Imagine building a house.

__new__

Build the house

__init__

Move furniture inside

You can't furnish a house that doesn't exist.

Writing Your Own __new__

Most Python developers never need this.

Example:

class User:

    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")

Conceptual output:

Creating object

Initializing object

Notice the order.

What is cls?

You've seen:

def __init__(self):

Now:

def __new__(cls):

Question:

Why cls?

Because no instance exists yet.

Python passes the class instead.

Think:

Before object exists

↓

Need the class

↓

Create object

↓

Now object exists

↓

Need self
cls vs self
Parameter	Represents
cls	The class object
self	The instance object

Example:

class Dog:

    def __new__(cls):
        ...

    def __init__(self):
        ...

Timeline:

Dog Class

↓

cls

↓

Create Dog Object

↓

self

↓

Initialize Dog Object
Why __new__ Matters

Immutable objects.

Example:

number = int("42")

The integer can't be modified after creation.

So Python must fully create it inside __new__.

The same applies to:

tuple
str
bytes

Their values are fixed at creation.

Professional Example — PyTorch

When you write:

layer = nn.Linear(10, 5)

Conceptually:

Call Linear class

↓

Create Linear object

↓

Initialize weights

↓

Initialize bias

↓

Return object

Every layer follows this lifecycle.

PocketFlow Example
class Schedule:

    def __init__(self, amount, frequency):
        self.amount = amount
        self.frequency = frequency
        self.status = "ACTIVE"

Creating:

salary = Schedule(
    50_000,
    "MONTHLY"
)

Timeline:

Schedule Class

↓

__new__()

↓

New Schedule object

↓

__init__()

↓

amount = 50000

frequency = MONTHLY

status = ACTIVE

↓

salary points to object
Common Mistake 1

Forgetting self.

class User:

    def __init__(name):
        ...

Python actually calls:

User.__init__(obj, "Pelumi")

Two arguments.

Your function accepts one.

Error.

Common Mistake 2

Returning something from __init__.

class User:

    def __init__(self):
        return {}

Wrong.

__init__ must return:

None

Its job is initialization, not object creation.

Common Mistake 3

Thinking __init__ creates the object.

It doesn't.

Remember:

__new__

↓

Creates object

↓

__init__

↓

Configures object
Code Review

Junior explanation:

"__init__ is the constructor."

Good enough for day-to-day coding.

Senior explanation:

"__init__ is the object initializer. Object creation happens first in __new__, which allocates and returns the instance. Python then invokes __init__ to populate the object's state."

Both are useful; the second is more precise.

Interview Question

Why does Python have both __new__ and __init__?

A strong answer:

__new__ is responsible for creating and returning a new instance, while __init__ initializes that instance after it has been created. Separating creation from initialization gives Python flexibility for immutable types and advanced object creation patterns.

Exercises
Exercise 1

Mentally trace:

class Dog:

    def __init__(self, name):
        self.name = name

dog = Dog("Buddy")

List the sequence of events from calling Dog("Buddy") until dog points to the finished object.

Exercise 2

Why does __new__ receive cls while __init__ receives self?

Explain using the object creation timeline.

Exercise 3

Critique this code:

class User:

    def __init__(self):
        return {}

Why is it incorrect?

Exercise 4 (AI Engineering)

When PyTorch executes:

layer = nn.Linear(768, 512)

Conceptually explain:

What object is created?
What happens during initialization?
Why can two Linear objects have different weights even though they come from the same class?