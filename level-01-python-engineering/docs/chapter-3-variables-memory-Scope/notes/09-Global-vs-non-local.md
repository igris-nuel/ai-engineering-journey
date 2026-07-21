## Lesson 9 — global vs nonlocal
Start with a Question

Suppose you have:

    x = 10

Now inside a function:

def work():
    x = 20

Question:

What happened?

Most beginners say:

"The function changed x."

But we already know that isn't true.

Why?

Because of everything we've learned.

## What Assignment Really Means

Remember Chapter 2.

Assignment never means:

    change an object

Assignment means:

    bind a name to an object.

Now remember Chapter 3.

Every function has its own namespace.

So when Python sees

    x = 20

inside a function, it thinks:

    "Create a name called x in the local namespace."

Not:

    "Find another namespace and modify it."

Why?

    Because Python protects local scope.

## Visualizing It

Suppose we start with:

    x = 10

Memory:

    Global Namespace

        x ─────► 10

    Call:

        def work():
            x = 20

Python creates:

    Global Namespace

        x ─────► 10


    Local Namespace (work)

        x ─────► 20

Notice something.

There are two names.

Not one.

They simply happen to have the same spelling.

## But What If You Really Mean the Global One?

Sometimes you genuinely want to modify it.

Example:

    total_requests = 0

Every API request:

    total_requests += 1

You don't want a local counter.

You want the shared one.

### How can Python know that?

It can't guess.

So you tell it.

    global total_requests

Now Python changes its interpretation.

Instead of:

create a local name

it becomes:

use the name from the global namespace.

Conceptually:

Without global

    Assignment

        ↓

    Create Local Name

With global

    Assignment

        ↓

    Use Global Namespace

## Why Doesn't Python Do This Automatically?

Imagine:

    config = ...

Inside a helper:

    config = {}

If Python automatically modified globals,

one accidental assignment could destroy your application's configuration.

The default behavior is therefore:

    assignment is local

because local changes are much safer than global changes.

## Now Let's Look at nonlocal

This one is even more interesting.

Remember nested functions.

def outer():
    x = 10

    def inner():
        ...

There are two namespaces now.

    Global

      ↓

    Outer

      ↓

    Inner

Suppose:

    def outer():
        count = 0

        def inner():
            count = count + 1

What does Python do?

Exactly what it always does.

It sees an assignment.

Therefore:

create a local name.

But then the right side says:

    count + 1

Python now tries to read the local count.

Problem:

The local one doesn't exist yet.

This is why this kind of code fails.

Not because Python is confused.

Because Python has already decided:

"count is local because you assigned to it."

nonlocal

Suppose instead we say:

nonlocal count

Now Python changes its interpretation.

Instead of creating a local name,

it says:

    "Use the nearest enclosing namespace."

Notice something beautiful.

nonlocal does not mean:

global.

It means:

enclosing function.

Conceptually:

    Global

    ↓

    Outer

    count ─────► 0

    ↓

    Inner

    nonlocal count

Now:

    count += 1

updates the outer namespace.

No new local name is created.

## Why Separate global and nonlocal?

Imagine there was only one keyword.

Python wouldn't know whether you meant:

    Global Namespace

    or

    Nearest Enclosing Function

Those are completely different places.

So Python makes you be explicit.

## Why AI Engineers Care

Imagine a training pipeline.

    def trainer():

        processed = 0

        def process_batch():
            ...

Every batch finishes.

You want:

    processed

    0

    ↓

    1

    ↓

    2

    ↓

    3

You don't want:

    processed

    0

    0

    0

    0

nonlocal allows the inner helper to update the outer state without exposing it globally.

This is much cleaner than putting everything into global variables.

## Mental Model

Never think:

"global lets me access globals."

You already had access.

Remember LEGB.

You could always read globals.

Instead think:

"global changes where assignment happens."

Likewise:

Don't think:

"nonlocal lets me see outer variables."

You could already see them.

Closures proved that.

Instead think:

"nonlocal changes where assignment happens."

That is the real job of both keywords.

They don't change lookup.

They change binding.

That single sentence explains both keywords.

## Summary

When Python sees an assignment:

name = value

its default behavior is:

Bind in Local Namespace

global changes that to:

Bind in Global Namespace

nonlocal changes that to:

Bind in Nearest Enclosing Namespace

Everything else remains exactly the same.

