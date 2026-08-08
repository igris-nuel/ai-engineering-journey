Lesson 6 — Encapsulation

Most tutorials define encapsulation as:

"Hiding data."

That's an oversimplification.

A better definition is:

Encapsulation is controlling how an object's state can be accessed and modified.

The goal isn't to hide data. The goal is to protect invariants (rules that should always remain true).

Example 1 — No Encapsulation
class BankAccount:

    def __init__(self, balance):
        self.balance = balance

Usage:

account = BankAccount(5000)

account.balance = -1000000

Problem?

A bank account should never have an arbitrary negative balance (assuming no overdraft).

The object allowed an invalid state.

Better Design

Instead of modifying the balance directly:

account.deposit(500)

account.withdraw(100)

Now the object controls the rules.

def withdraw(self, amount):

    if amount > self.balance:
        raise ValueError("Insufficient funds")

    self.balance -= amount

The balance cannot become invalid accidentally.

Encapsulation ≠ Secrecy

Many beginners think:

"Users shouldn't see the balance."

No.

Users should absolutely see it.

They just shouldn't be able to put the object into an invalid state.

Python Doesn't Enforce Privacy

Unlike Java:

private int balance;

Python doesn't have true private fields.

Instead it relies on conventions.

Public Attributes
class User:

    def __init__(self):
        self.name = "Pelumi"

Accessible everywhere.

user.name

No restrictions.

Protected Attributes (Convention)

Single underscore.

class User:

    def __init__(self):
        self._password_hash = "..."

Meaning:

"Internal implementation. Don't touch unless you know what you're doing."

Python does not enforce this.

It's a convention respected by developers.

Private Attributes (Name Mangling)

Double underscore.

class User:

    def __init__(self):
        self.__token = "abc123"

Now:

user.__token

fails.

Why?

Python secretly renames it.

Conceptually:

_User__token

This is called name mangling.

It prevents accidental access and accidental name collisions in inheritance. It is not meant as strong security.

What is Name Mangling?

Internally, Python transforms:

__token

into something like:

_User__token

Notice:

The attribute still exists.

It just has a different name.

Why Does Python Do This?

Imagine:

class Parent:

    __value = 10

Child:

class Child(Parent):

    __value = 20

Without name mangling:

Both would define __value, causing a collision.

With name mangling:

_Parent__value

_Child__value

No collision.

Properties

One of Python's best features.

Suppose you start with:

class Temperature:

    def __init__(self):
        self.celsius = 25

Usage:

temp.celsius

Simple.

Later you decide:

Celsius should never go below absolute zero.

If you expose the attribute directly:

temp.celsius = -500

Bad.

Solution — @property
class Temperature:

    def __init__(self):
        self._celsius = 25

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):

        if value < -273.15:
            raise ValueError("Invalid temperature")

        self._celsius = value

Usage:

temp.celsius = 30

Looks like attribute access.

Internally:

temp.celsius = 30

becomes conceptually:

temp.celsius.setter(30)

The syntax stays clean while validation is enforced.

Professional Example — PocketFlow

Bad:

schedule.status = "RANDOM"

Better:

schedule.pause()

schedule.resume()

schedule.cancel()

The object controls the valid state transitions.

Imagine:

ACTIVE

↓

PAUSED

↓

ACTIVE

↓

CANCELLED

Can a cancelled schedule become active again?

Maybe not.

The object should enforce that rule.

Professional Example — PyTorch

Consider:

model.training

You read it.

But to change the mode, you usually use:

model.train()

model.eval()

Why?

Because changing training mode affects many internal components (like dropout and batch normalization).

The framework exposes methods to ensure all related state changes consistently.

Professional Example — Database Session

Instead of:

session.connected = False

You use:

session.close()

The method performs all required cleanup, not just flipping a flag.

When to Use Properties

Good candidates:

temperature
age
balance
email
password
status

Things that need validation or computed values.

When NOT to Use Properties

Don't wrap every attribute.

This is unnecessary:

@property
def name(self):
    return self._name

if you're not adding:

validation
computation
lazy loading
logging
caching

Keep it simple.

Code Review
Over-engineered
class User:

    @property
    def first_name(self):
        return self._first_name

No validation.

No logic.

Probably unnecessary.

Better
class User:

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value

Now the property has a purpose.

Interview Question

Why use a property instead of exposing an attribute directly?

A strong answer:

Properties let you keep attribute-style access while adding validation, computation, lazy loading, logging, or other behavior without changing the public API.

Exercises
Exercise 1

You're designing:

class Wallet

Should balance be:

a public attribute,
a property,
or only modified through methods like deposit() and withdraw()?

Explain your design.

Exercise 2

Why is this dangerous?

schedule.status = "COMPLETED"

instead of:

schedule.complete()

Think about business rules.

Exercise 3

Without running the code, explain what Python conceptually does:

class User:

    def __init__(self):
        self.__secret = "token"

Why does:

user.__secret

fail?

Exercise 4 (PocketFlow)

You're designing the Transfer class.

Decide which of these should be:

Public
Protected (single underscore)
Private (double underscore, if justified)
Property
Method-controlled only

Attributes:

id
status
amount
provider_reference
signature
created_at

Justify each choice briefly.