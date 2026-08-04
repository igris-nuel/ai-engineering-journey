Lesson 4 — Methods

Most tutorials say:

"self refers to the current object."

That's true.

But it doesn't explain why.

Today, we'll understand what a method really is.

Start with a Function
def greet(name):
    print(f"Hello {name}")

Calling it:

greet("Pelumi")

Nothing new.

Now look at this:

class User:

    def greet(self):
        print("Hello")

Question:

What is greet?

Is it special?

No.

It is still a function.

Proof

Conceptually:

class User:

    def greet(self):
        print("Hello")

creates something like:

User.__dict__
    {
        "greet": <function greet>
    }

Notice:

The class stores a function object.

Creating an Instance
user = User()

Now:

user.greet()

Most people think:

The object owns the method.

Not exactly.

The object doesn't store greet.

The class does.

Memory:

User Class

{
    "greet": <function>
}

↓

user Instance

{}

No greet inside the instance.

Attribute Lookup

When Python sees:

user.greet

It performs the same lookup algorithm we learned:

Instance __dict__

↓

Class __dict__

↓

Found "greet"

So it finds:

<function greet>

But here's the interesting part.

Bound Methods

Python does not return the raw function.

It creates a temporary object called a bound method.

Conceptually:

Function

+

Instance

↓

Bound Method

That bound method remembers:

Function → greet

Instance → user
Visual
User Class

greet
 │
 ▼
Function Object

+

user Instance

↓

Bound Method

↓

user.greet
Calling the Method

When you write:

user.greet()

Python conceptually transforms it into:

User.greet(user)

This is one of the most important ideas in Python.

The instance becomes the first argument.

Proof

Suppose:

class User:

    def greet(self):
        print(self)

Now:

user = User()

user.greet()

Conceptually becomes:

User.greet(user)

So inside:

def greet(self):

self

is simply:

user

Nothing magical.

Example with Parameters
class BankAccount:

    def deposit(self, amount):
        self.balance += amount

Calling:

account.deposit(500)

Conceptually:

BankAccount.deposit(account, 500)

Notice:

Python automatically supplied:

account

as the first argument.

Why It's Called self

It isn't a keyword.

You could write:

class User:

    def greet(me):
        print(me)

Python accepts it.

Or:

class User:

    def greet(banana):
        print(banana)

Still valid.

But don't.

self is a convention followed by the entire Python community.

Professional Example — PyTorch

When you write:

model.forward(x)

Conceptually:

Model.forward(model, x)

Notice:

model

is passed automatically.

Another example:

optimizer.step()

Conceptually:

Optimizer.step(optimizer)

Same rule.

Professional Example — FastAPI
app.include_router(router)

Conceptually:

FastAPI.include_router(app, router)
PocketFlow Example

Imagine:

class Schedule:

    def pause(self):
        self.status = "PAUSED"

Now:

salary.pause()

Conceptually:

Schedule.pause(salary)

The function receives the schedule instance.

That's why it knows which schedule to pause.

Multiple Objects
salary.pause()

rent.pause()

Conceptually:

Schedule.pause(salary)

Schedule.pause(rent)

Same function.

Different first argument.

Different object.

Why This Design?

Suppose methods worked differently.

Every object would need its own copy of every method.

Imagine:

10,000 Schedule objects.

If each object stored its own pause() function:

Huge memory waste.

Instead:

One Class

↓

One Function

↓

10,000 Objects use it

Efficient.

Common Beginner Mistake
class User:

    def greet():
        print("Hello")

Calling:

user.greet()

Fails.

Why?

Because Python still tries:

User.greet(user)

But the function expects:

0

arguments.

Python supplied:

1
Another Mistake
User.greet()

Without an instance.

Conceptually:

User.greet()

No object is passed.

self is missing.

Python complains because it expected the first argument.

Code Review

Junior understanding:

"self is the current object."

Good enough to get started.

Senior understanding:

"self is simply the first parameter of an instance method. When a method is accessed through an instance, Python creates a bound method that automatically passes that instance as the first argument when the method is called."

That explains how it works, not just what it is.

Interview Question

Why doesn't Python require this as a keyword like Java or C++?

A strong answer:

Because Python passes the instance explicitly as the first parameter (self). It's an ordinary parameter supplied automatically by the bound method mechanism, not a special keyword.

Exercises
Exercise 1

Without running the code:

class Dog:

    def bark(self):
        print("Woof")

dog = Dog()

dog.bark()

Conceptually rewrite the method call the way Python sees it.

Exercise 2

Explain why this works:

class User:

    def greet(self, name):
        print(f"Hello {name}")

user = User()

user.greet("Pelumi")

How many arguments are actually passed to greet?

Exercise 3

Why does this fail?

class User:

    def greet():
        print("Hello")

user = User()

user.greet()

Explain the error using your mental model of bound methods.

Exercise 4 (PocketFlow)

Consider:

class Schedule:

    def execute(self):
        print(f"Executing {self.amount}")

When you write:

salary.execute()
rent.execute()

Explain why the same method can operate on different schedules without storing separate copies of execute in every instance.

Next Lesson

Lesson 5 — Constructors

We'll finally answer the full object creation timeline:

schedule = Schedule(50_000)

What happens internally?

The class is called.
__new__ creates the object.
__init__ initializes it.
The object is returned and bound to schedule.