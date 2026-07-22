# Lesson 12 — Function Design

This isn't about syntax anymore.

It's about how senior engineers think when writing functions.

By this point you already understand:

function objects
execution frames
parameters
arguments
object sharing
return values
recursion
decorators
higher-order functions

Now we answer a different question:

## How should a function be designed?

This is where junior and senior engineers begin to separate.

The purpose of a function

Many beginners think:

A function is a way to avoid repeating code.

That's true...

...but it's only about 10% of the story.

The real purpose is this:

A function encapsulates one responsibility behind a clear interface.

Think about a TV remote.

You press:

Volume Up

You don't know:

which chip receives the signal

which transistor changes voltage

which amplifier changes gain

You don't care.

The remote exposes one clean interface.

Functions do exactly that.

A function is an abstraction boundary

Imagine PyTorch.

You write:

loss.backward()

You don't implement:

chain rule
graph traversal
gradient accumulation
memory reuse
tensor scheduling

Millions of operations happen.

Yet your interface is:

    loss.backward()

That's excellent function design.

Good functions hide complexity

Bad code:

    Main Program

    ↓

    500 lines

    ↓

    if...

    ↓

    for...

    ↓

    more if...

    ↓

    special cases...

    ↓

    logging...

    ↓

    saving...

    ↓

    network...

    ↓

    math...

Everything mixed together.

Impossible to understand.

Good code:

    train()

    ↓

    load_data()

    ↓

    preprocess()

    ↓

    forward()

    ↓

    compute_loss()

    ↓

    backward()

    ↓

    update_weights()

    ↓

    save_checkpoint()

Each function hides its own complexity.

## Single Responsibility Principle

The biggest idea in function design.

A function should do one thing well.

Not three.

Not ten.

One.

Bad:

    train_model()

    ↓

    loads data

    ↓

    normalizes

    ↓

    trains

    ↓

    logs metrics

    ↓

    sends email

    ↓

    writes CSV

    ↓

    uploads cloud backup

Impossible to test.

Impossible to debug.

Good:

    load_data()

    normalize()

    train()

    log_metrics()

    save_checkpoint()

    send_notification()

Now each function has one job.

## Why this matters

Imagine:

Accuracy suddenly dropped.

Which function is wrong?

If every function has one responsibility...

You immediately know where to look.

If one giant function does everything...

Good luck.

## Inputs and Outputs

A good function should make its dependencies obvious.

Instead of secretly reading globals:

Bad:

    train()

Where does it get the model?

Nobody knows.

Better:

    train(model, dataset)

Now the interface tells the truth.

## Return useful values

Bad:

    train(model)

Internally changes twenty globals.

Returns nothing.

Nobody knows what changed.

Better:

    metrics = train(model)

The output is explicit.

## Avoid hidden state

Hidden state is one of the biggest sources of bugs.

Example:

    train()

    ↓

    changes:

    current_model

    optimizer

    epoch

    device

    seed

    config

    history

Nothing in the interface tells you this.

Another function suddenly behaves differently.

Why?

Because hidden state changed.

## Pure vs Impure functions

Not every function should be pure.

But understanding the distinction is important.

Pure function:

    same inputs

    ↓

    same output

    ↓

    no hidden state

    ↓

    no side effects

Example:

    square(5)

    ↓

    25

Every time.

Impure:

    save_checkpoint()

    Writes files.

    Changes disk.

    Depends on filesystem.

    Has side effects.

That's okay.

Just make it obvious.

Naming

Good names explain intent.

Bad:

    do_it()

    process()

    handle()

    thing()

    run()

Good:

    load_dataset()

    compute_loss()

    normalize_images()

    predict()

    save_checkpoint()

You should almost never need comments to explain these.

## Small functions

Senior engineers usually prefer:

20–40 lines

instead of

400-line monsters.

Not because shorter is always better—

because they're easier to:

    read
    test
    reuse
    debug
    compose

That said, don't split functions so aggressively that the code becomes fragmented. A function should be as long as it needs to be to express one coherent responsibility.

## AI Engineering Example

Bad:

    train()

    ↓

    load files

    ↓

    shuffle

    ↓

    tokenize

    ↓

    pad

    ↓

    move GPU

    ↓

    forward

    ↓

    loss

    ↓

    backward

    ↓

    optimizer

    ↓

    scheduler

    ↓

    logging

    ↓

    checkpoint

    ↓

    evaluation

    One enormous function.

Better:

    train()

    ↓

    prepare_batch()

    ↓

    forward_pass()

    ↓

    compute_loss()

    ↓

    backward_pass()

    ↓

    optimizer_step()

    ↓

    log_metrics()

    ↓

    save_checkpoint()

Exactly how frameworks like PyTorch Lightning, Hugging Face Trainer, and many production ML codebases are structured.

## Mental Model

Think of functions like departments inside a company.

    CEO

    ↓

    Finance

    ↓

    Engineering

    ↓

    Legal

    ↓

    HR

The CEO doesn't do everyone's work.

Each department has a clear responsibility and communicates through defined interfaces.

Good software is organized the same way.