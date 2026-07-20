# Lesson 7 — Variable Lifetime

Most beginners think:

"Variables exist until my program ends."

That's completely wrong.

Variables live only as long as their namespace lives.

Notice I didn't say objects.

That's the key distinction.

First Question

Forget Python for a moment.

Imagine a company.

Every morning, a worker gets a temporary desk.

They put papers on the desk.

At 5 PM the worker leaves.

The desk is cleaned.

The papers are removed.

Tomorrow the worker gets another desk.

The company building still exists.

The worker still exists.

But yesterday's desk contents are gone.

Python functions work exactly like this.

Calling a function creates a temporary workspace.

Returning from the function destroys that workspace.

Important distinction

There are two different lifetimes:

### Lifetime of a name

How long does a variable exist?

Example:

        def work():
            x = 10

The name x exists only while work() is executing.

Once the function returns:

x

doesn't exist anymore.

The namespace was destroyed.

###  Lifetime of an object

Objects don't disappear merely because a variable disappeared.

Example:

def work():
    x = SomeHugeObject()

When work() ends:

the name disappears

but the object only disappears if nothing else references it.

Remember Chapter 2:

Reference counting.

Garbage collection.

Exactly why we spent so much time there.

Everything connects.

## Visual intuition

Imagine this.

Function Frame

    x ───────► Huge Model

Function returns.

Frame disappears.

Huge Model

### Question:

Does it disappear?

### Answer:

Only if no other references exist.

Suppose instead:

saved = None

def work():
    global saved
    saved = HugeModel()

During execution:

Global Namespace

    saved ─────► HugeModel

When the function returns:

The local namespace dies.

But

saved

still exists globally.

The object survives.

The object's lifetime is determined by references,

not by where it was created.

This is one of the deepest ideas in Python.

## Why AI engineers should care

Imagine loading:

7 GB LLM

inside a helper function.

def load():
    model = load_llm()

If nothing is returned,

the function ends.

The name dies.

Reference count becomes zero.

The model is destroyed.

You just wasted 20 seconds loading it.

Instead:

model = load()

or

self.model = load()

Now another namespace owns the object.

The model survives.

This is why production systems carefully manage object lifetimes.

## Common misconception

People often think:

Local variables are deleted.

Not exactly.

Python doesn't go through deleting variables one by one.

Instead:

The entire local namespace (frame) is discarded.

It's like throwing away the whole desk, not removing papers individually.

## Another misconception

People often think:

Returning from a function destroys every object created inside it.

Wrong.

Returning destroys the names.

Objects survive if something else still references them.

Example:

    def build():
        data = [1, 2, 3]
        return data

After return:

data

is gone.

But the list is still alive because the caller now references it.

## Mental Model

Never think:

Variables hold data.

Think:

Namespaces hold names.

Names reference objects.

Namespaces have lifetimes.

Objects have independent lifetimes.

That sentence explains nearly every "weird" behavior beginners encounter in Python.

