## Lesson 4 — The LEGB Rule
Let's Start With a Question

Imagine you're in a huge office.

You ask:

"Where is the project report?"

Should the receptionist immediately search the entire building?

No.

A sensible search strategy is:

Check your own desk.
Check your team's office.
Check the department archive.
Check the company library.

Python does exactly the same thing.

It searches from the closest place outward.

## Why Search the Closest Scope First?

Imagine this.

x = 100

def calculate():
    x = 5
    print(x)

What should Python print?

5

Why?

Because the function created its own local name.

Imagine if Python searched the global namespace first.

It would find:

x = 100

before it ever looked inside the function.

Then local variables would become almost useless.

So Python always asks:

"Do I already have a nearby definition?"

Closest wins.

The Four Places Python Searches

Every time Python encounters a name like

value

it performs a lookup.

Conceptually:

    Need name

    ↓

    Search Local

    ↓

    Found?

    ↓

    Yes → Stop

    ↓

    No

    ↓

    Search Enclosing

    ↓

    Found?

    ↓

    Yes → Stop

    ↓

    No

    ↓

    Search Global

    ↓

    Found?

    ↓

    Yes → Stop

    ↓

    No

    ↓

    Search Built-in

    ↓

    Found?

    ↓

    Yes → Stop

    ↓

    No

    ↓

    NameError

Notice something.

Python stops immediately when it finds the name.

It never keeps searching.

L — Local

This is the namespace belonging to the current function call.

    def greet():

        name = "Taki"

        print(name)

Python asks:

Does the current function have name?

Yes.

Done.

No further searching.

E — Enclosing

This one confuses beginners because we haven't studied nested functions yet.

Imagine:

def outer():

    message = "Hello"

    def inner():

        print(message)

Where does inner() find message?

Not locally.

Not globally.

It finds it in the surrounding function.

That surrounding function is called the enclosing scope.

We'll spend an entire lesson on this later.

## G — Global

If Python doesn't find the name locally or in an enclosing function,

it checks the module's global namespace.

Example:

language = "Python"

def show():

    print(language)

Search:

Local?

No.

Enclosing?

No.

Global?

Yes.

Done.

Again...

No copying.

Just lookup.

B — Built-in

Suppose you write:

print("Hello")

Where did print come from?

You never defined it.

Python did.

It lives inside the built-in namespace.

Same for:

    len()

    sum()

    min()

    max()

    range()

    int()

    str()

    list()

    dict()

    zip()

    enumerate()

They're simply names stored in another namespace.

This surprises many people.

Even print is "just" a name.

A Huge Realization

Everything we've learned still applies.

Namespaces contain:

Name

↓

Object

The built-in namespace is simply another namespace.

Instead of:

    x

    ↓

    10

it contains:

    print

      ↓

    Function Object

    len

      ↓

    Function Object

    list

      ↓

    Class Object

Nothing magical.

Just another dictionary of names.

Why This Order Makes Sense

Suppose Python searched like this instead:

    Built-in

    ↓

    Global

    ↓

    Local

Now imagine:

len = 100

print(len)

Should Python print

100

or the built-in function?

If built-ins were searched first,

you could never override names intentionally.

That would make Python much less flexible.

The closest scope should always have priority.

Shadowing

Suppose:

    x = 100

    def work():

        x = 5

        print(x)

The local x hides the global x.

This is called shadowing.

The global variable still exists.

It's simply hidden by a closer name during that function call.

Think of two people named "John":

John in your room.
John somewhere else in the building.

If someone in your room says:

"John."

You naturally think of the nearest John.

Not the distant one.

That's shadowing.

## Why AI Engineers Should Care

Imagine a training framework.

Global

model
optimizer
config
device

Inside training:

    def train():

        batch
        loss
        optimizer

Notice something.

The local optimizer could intentionally shadow another name.

Python resolves this automatically.

Large AI frameworks rely heavily on this predictable lookup behavior.

Another Insight

LEGB is not just about variables.

It applies to every name.

Variables.

Functions.

Classes.

Modules.

Even built-ins.

Everything is resolved through the same lookup algorithm.

That's elegant language design.

One rule.

Applies everywhere.

The Bigger Picture

Notice how all of Chapter 3 is fitting together:

Chapter 2 taught us that names point to objects.
Lesson 1 taught us that names live inside namespaces.
Lesson 2 introduced local namespaces.
Lesson 3 introduced global namespaces.
Now LEGB explains how Python chooses which namespace to search.

Nothing new contradicts the earlier lessons. Each lesson extends the same mental model.

## AI Engineering Insight

Many dependency injection frameworks work by making dependencies explicit instead of relying on LEGB lookups for important objects.

Instead of this:

    train()

    ↓

    looks up model globally

they encourage:

train(model, optimizer, config)

Why?

Because the function's dependencies are visible in its signature. That makes the code easier to understand, test, and reuse.

As systems grow, making dependencies explicit usually beats relying on distant names.

