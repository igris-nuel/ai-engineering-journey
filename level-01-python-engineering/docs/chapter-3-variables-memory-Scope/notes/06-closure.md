# Lesson 6 — Closures

Start with a mystery

Imagine I write this:

    def outer():
        x = 10

        def inner():
            print(x)

        return inner

Don't think about the syntax.

Instead, think about the memory.

When outer() finishes...

what have we learned?

Local namespace disappears.
Local variables disappear.
Stack frame disappears.

So...

Where did x go?

Shouldn't it have been destroyed?

If x disappeared...

how can inner() still print it?

This looks like Python is breaking its own rules.

It isn't.

Let's build the intuition

Imagine a company.

The CEO hires an assistant.

The assistant receives a confidential notebook.

Inside the notebook is important information.

Now the CEO retires.

Question:

Does the notebook disappear?

No.

The assistant still has it.

The assistant can continue using it.

Closures work exactly like this.

The outer function disappears.

The inner function keeps the notebook.

Notice something important.

The notebook is not the CEO.

The notebook is the captured state.

That distinction is everything.

Another analogy

Imagine you're baking a cake.

The recipe says:

2 eggs
flour
sugar

Once the cake is baked...

the recipe can be thrown away.

Does the cake lose the eggs?

No.

The ingredients became part of the finished cake.

Similarly,

the outer function can disappear,

but the inner function keeps the pieces of state it needs.

The wrong mental model

Many beginners imagine this:

outer()

↓

x exists

↓

outer finishes

↓

x dies

↓

inner somehow magically remembers x

That isn't what happens.

Python doesn't use magic.

Python changes what gets kept alive.

The correct mental model

Normally...

outer()

↓

Local namespace

↓

x

↓

outer returns

↓

namespace destroyed

↓

x reference count becomes 0

↓

x dies

But if a nested function needs x...

Python does something clever.

Instead of treating x like an ordinary local variable...

Python stores it somewhere safe.

Then both

the outer function
the inner function

can reference it.

Conceptually:

           outer()

               │
               │

        Local Namespace

               │

               ▼

          x = 10
               ▲
               │

        Shared Cell

               │
               ▼

         inner function

Notice something.

The inner function is not copying x.

It is holding a reference to the same object.

That should sound familiar.

Everything in Python comes back to references.

Why didn't Python just copy x?

Suppose x is not an integer.

Suppose it's

a neural network
a tokenizer
a huge configuration
a database connection
a GPU tensor

Copying it would be absurd.

Instead,

Python shares the object.

Exactly like assignment.

Exactly like function arguments.

Exactly like we've been studying since Chapter 2.

Closures continue the same philosophy.

Think like an AI engineer

Imagine this:

build_model(config)

Inside it:

preprocess(data)

Should preprocess() receive the config every single time?

preprocess(data, config)
preprocess(data, config)
preprocess(data, config)
preprocess(data, config)

Or...

could the preprocessing function simply remember the configuration?

That's what closures allow.

Another intuition

Imagine you manufacture calculators.

Each calculator remembers a tax rate.

Calculator A remembers:

7%

Calculator B remembers:

15%

Calculator C remembers:

22%

The factory closes.

Do the calculators forget their tax rates?

No.

Each calculator remembers the value it was built with.

Closures work exactly like that.

This is why closures are powerful

They combine

behavior

and

state

into one object.

Not a class.

Not inheritance.

Just a function carrying memory with it.

Real-world examples

You don't realize it yet,

but you've already seen APIs designed around closures.

For example:

dataset.map(...)

Often the function passed into map() remembers configuration from somewhere else.

Likewise:

optimizer.step(...)

Callbacks frequently remember training state.

Even web frameworks:

@app.route(...)

Decorators rely heavily on closures.

We'll understand that later.

The most important idea

A closure is not about nested functions.

Nested functions are only the beginning.

The real idea is:

A function can carry some of the environment in which it was created.

That environment becomes part of the function.

Almost like invisible luggage.

Mental model

Think of a function object as no longer containing only code.

Instead think of it like this:

Function Object

+------------------------+

Instructions

Captured Variables

Metadata

Reference to Globals

Reference to Builtins

+------------------------+

That's much closer to reality.

A function is not just executable code.

It is a rich object.

Why AI engineers should care

Closures appear everywhere.

Examples include:

data preprocessing pipelines
callback systems
asynchronous programming
decorators
retry mechanisms
caching
logging
dependency injection
model factories
optimizer hooks
learning-rate schedulers

If you don't understand closures,

many modern Python libraries feel magical.

Once you understand them,

those libraries suddenly become logical.