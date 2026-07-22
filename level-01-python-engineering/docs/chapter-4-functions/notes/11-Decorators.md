# Lesson 11 — Decorators

## Why Were Decorators Invented?

Imagine you have three functions.

    train()
    evaluate()
    predict()

Now your team says:

"Log whenever a function starts."

Easy.

You add logging.

Later...

"Also measure execution time."

So you edit every function.

Later...

"Also check permissions."

Edit every function.

Later...

"Retry if it fails."

Edit every function.

Eventually every function becomes:

Start logging

Start timer

Check permissions

Retry logic

Actual work

Stop timer

Write logs

Notice something.

The actual business logic is now buried under infrastructure code.

## The Problem

There are two different concerns.

Business logic:

    Train a model.

Infrastructure:

    Logging

    Timing

    Authentication

    Caching

    Retries

    Monitoring

They are completely different responsibilities.

Yet they're mixed together.

Good software engineering tries to separate them.

## What Is a Decorator?

A decorator is simply:

A higher-order function that takes one function, wraps it with additional behavior, and returns a new function.

Nothing more.

No magic.

Let's break that down.

### Step 1 — We Already Know This

Functions are objects.

train

is simply a name pointing to a function object.

### Step 2 — Functions Can Be Passed

We've already learned:

logger(train)

passes the function object.

Nothing executes yet.

### Step 3 — Functions Can Return Functions

We also learned:

    make_processor()

          ↓

      returns

        ↓

     process

Again...

Nothing new.

### Step 4 — Put Them Together

Imagine:

    decorate(train)

Inside decorate:

        Receive function object

                ↓

        Create another function

                ↓

        That new function calls the original one

                ↓

        Return the new function

That's literally a decorator.

## Mental Picture

Original:

    train

      ↓

    Decorator:

    wrapper(train)

        ↓

    Produces

    better_train

Now everyone calls:

better_train()

instead of

train()

## What Does the Wrapper Do?

Imagine the wrapper says:

    Start timer

        ↓

    Call original train()

        ↓

    Stop timer

        ↓

    Print elapsed time

Notice something.

The original function never changed.

It still only knows how to train.

The wrapper added new behavior.

Timeline

Imagine someone calls:

    train()

But...

After decoration...

The name actually points here:

wrapper()

Execution becomes:

    Caller

       ↓

    wrapper()

       ↓

    logging

       ↓

    timing

       ↓

    calls original train()

       ↓

    returns

       ↓

    wrapper finishes

The caller doesn't even know.

## Why Closures Matter

Remember closures?

A wrapper must remember:

Which function am I wrapping?

That wrapped function lives inside the closure.

Conceptually:

    wrapper remembers:

           ↓

    original_function

Even after the decorator finishes,

the wrapper still knows exactly which function to call.

Without closures,

decorators couldn't exist.

This is why I insisted we study closures before decorators.

## Why Higher-Order Functions Matter

Decorators are impossible unless:

Functions can be passed.

Functions can be returned.

Exactly what we learned.

## AI Engineering Example

Imagine PyTorch.

Instead of writing:

Start profiler

Forward pass

Stop profiler

inside every model,

the framework wraps the function.

Now profiling becomes reusable.

Imagine FastAPI.

Instead of manually registering every endpoint,

you simply write:

This function handles "/users"

FastAPI stores the function object,

attaches metadata,

and later calls it when an HTTP request arrives.

That mechanism is powered by decorators.

Imagine a training framework.

It wants:

    logging
    checkpointing
    retries
    distributed synchronization
    GPU profiling

Instead of rewriting every training function,

it wraps them.

Business logic stays clean.

Infrastructure stays reusable.

Decorators Don't Modify Functions

This is an important misconception.

Many beginners think:

"The decorator changes the function."

Not really.

Conceptually it does this:

    Original Function

          ↓

    Wrapper Function

          ↓

    Return Wrapper

          ↓

     Rebind Name

The original function object still exists.

The name simply points to the wrapper now.

Exactly like rebinding any other variable.

Remember Chapter 2?

       x

       ↓

    Object A

       ↓

    x = Object B

Same idea.

Now:

      train

        ↓

    Original Function

        ↓

    train = wrapper

The name now points somewhere else.

The Beautiful Connection

Everything we've learned now connects.

Chapter 2

    Names → Objects → References

    ↓

    Chapter 3

    Namespaces

    Frames

    Closures

    ↓

    Chapter 4

    Function Objects

    Higher-Order Functions

    ↓

    Decorators

Nothing new had to be invented.

Decorators are simply an elegant combination of concepts you already know.

## Mental Model

Think of decorators like gift wrapping.

You have:

Gift

Wrap it:

Wrapper

↓

Gift

The gift hasn't changed.

You've simply added another layer around it.

Functions work exactly the same way.
