## lesson 3 — Attributes

If I asked:

Where is user.name stored?

Most Python developers answer:

"Inside the object."

That's correct, but incomplete.

Today we'll understand how Python finds an attribute.

Creating an Instance
    class User:
        pass

    user = User()

At this point, the instance has no custom attributes.

Now:

user.name = "Pelumi"
user.age = 25

Conceptually, Python creates something like:

user
 │
 ▼

Instance Object
───────────────
{
    "name": "Pelumi",
    "age": 25
}

That dictionary is called the instance namespace.

__dict__

Every normal Python object has a dictionary that stores its attributes.

class User:
    pass

user = User()

user.name = "Pelumi"
user.age = 25

Conceptually:

user.__dict__

contains

{
    "name": "Pelumi",
    "age": 25
}

We'll inspect it later.

For now, understand the mental model.

Attribute Assignment
user.country = "Nigeria"

Python conceptually performs:

user.__dict__["country"] = "Nigeria"

Nothing magical.

Just inserting a new key.

Attribute Access

Now:

print(user.name)

Python conceptually performs:

user.__dict__["name"]

returns

"Pelumi"

Simple.

Dynamic Attributes

One of Python's strengths.

class User:
    pass

user = User()

user.name = "Pelumi"

Later:

user.email = "pelumi@example.com"

Later again:

user.role = "admin"

The object grows over time.

Unlike Java or C++, Python objects can gain attributes dynamically.

Professional Example

Imagine:

class Request:
    pass

Middleware may do:

request.user = current_user

Authentication middleware:

request.permissions = permissions

Logging middleware:

request.request_id = uuid

Different layers enrich the same object.

You'll see this in frameworks like FastAPI and Django.

Attribute Lookup

Consider:

class User:

    country = "Nigeria"

Now:

user = User()

print(user.country)

Question:

Where does Python look?

The instance?

The class?

Both?

The answer is both.

Lookup Algorithm

When Python evaluates:

user.country

It follows this order:

1. Instance __dict__

↓

2. Class __dict__

↓

3. Parent classes (Inheritance)

↓

AttributeError

This lookup order explains many "strange" behaviors.

Example
class User:

    country = "Nigeria"

user = User()

Memory

User Class
───────────────
country

↓

"Nigeria"


Instance

{}

Now:

user.country

Instance?

Nothing.

↓

Class?

Found.

↓

Return "Nigeria".

Shadowing

Now:

user.country = "Canada"

Memory

Class

country

↓

Nigeria

Instance

country

↓

Canada

Question:

Which one wins?

The instance.

Python always checks the instance first.

Example
class User:

    role = "user"

u1 = User()
u2 = User()

u1.role = "admin"

Results:

u1.role

↓

admin
u2.role

↓

user

The class wasn't modified.

Only u1.

Class Attributes

Good uses:

class User:

    MAX_LOGIN_ATTEMPTS = 5

    DEFAULT_COUNTRY = "Nigeria"

These are shared constants.

Bad use:

class User:

    balance = 0

Every user would appear to share the same balance.

That's almost certainly wrong.

Balances belong to instances.

Instance Attributes

Good:

class BankAccount:

    def __init__(self):

        self.balance = 0

Each account owns its own balance.

Exactly what we want.

PocketFlow Example

Bad:

class Schedule:

    amount = 50000

Every schedule would share the same amount.

Wrong.

Better:

class Schedule:

    def __init__(self, amount):

        self.amount = amount

Now:

salary.amount

and

rent.amount

can be different.

PyTorch Example

When you create:

linear1 = nn.Linear(10, 5)

linear2 = nn.Linear(10, 5)

Each object has its own:

weights
biases

If these were class attributes,

every neural network layer in the world would share the same weights.

Training would be impossible.

Code Review

Bad:

class Student:

    grades = []

Every student shares one list.

Very common bug.

Good:

class Student:

    def __init__(self):

        self.grades = []

Each student gets a different list.

Interview Question

Difference between instance and class attributes?

A strong answer:

Instance attributes belong to individual objects and are typically stored in the instance's namespace (__dict__). Class attributes belong to the class object itself and are shared across all instances unless shadowed by an instance attribute.

Exercises
Exercise 1

Without running the code:

class User:

    country = "Nigeria"

u = User()

u.name = "Pelumi"

Explain:

Where is country stored?
Where is name stored?
How does Python find each attribute?
Exercise 2

Predict conceptually:

class Config:

    debug = False

a = Config()
b = Config()

a.debug = True

Explain:

What does a.debug return?
What does b.debug return?
Why?
Exercise 3

Critique this design:

class Wallet:

    transactions = []

Why is this dangerous?

How would you redesign it?

Exercise 4 (PocketFlow)

You're designing:

class Schedule

Classify each of these as either a class attribute or an instance attribute, and justify your decision:

amount
frequency
status
provider_name
DEFAULT_TIMEZONE
MAX_RETRY_COUNT

Think in terms of what should be shared by every schedule versus what belongs to one specific schedule.

Next Lesson

Lesson 4 — Methods

We'll answer one of the most misunderstood questions in Python:

What exactly is self?

We'll go beyond "it's the instance" and see how:

user.pause()

is conceptually transformed into:

User.pause(user)

Understanding this will make method binding, decorators, and even parts of PyTorch much easier to grasp.