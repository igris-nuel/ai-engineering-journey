## Lesson 3 — if, elif, and else

Now that you understand Boolean values and truthiness, it's time to use them to make decisions.

This is one of the most fundamental ideas in all of programming.

Every AI framework, every backend service, every operating system, and every compiler constantly asks questions like:

Should I execute this code?

That's exactly what if is for.

A Program Doesn't Have to Execute Every Line

Look at this:

    print("Program started")

    print("Loading model")

    print("Training complete")

Every line executes.

The CPU simply moves from top to bottom.

But what if training should only happen when a dataset exists?

We need a decision.

The Simplest if
    dataset_loaded = True

    if dataset_loaded:
        print("Training started")

Output:

Training started

If we change it:

    dataset_loaded = False

    if dataset_loaded:
        print("Training started")

Output:

    (nothing)

The condition is false.

Python skips the indented block.

## Mental Model

Conceptually:

    Evaluate condition

    ↓

    True?

    ↓

    Yes
        Execute block

    No
        Skip block

The block either executes completely or not at all.

The Colon (:)
if dataset_loaded:

The colon tells Python:

"A new block begins here."

Everything indented underneath belongs to the if.

Indentation Defines Blocks

    logged_in = True

    if logged_in:
        print("Welcome")
        print("Loading dashboard")
        print("Loading profile")

    print("Done")

If logged_in is True:

    Welcome
    Loading dashboard
    Loading profile
    Done

If it's False:

Done

Only the indented block is skipped.

Why Indentation Matters

Many languages use braces:

if (logged_in) {
    ...
}

Python instead uses indentation.

Bad indentation changes the meaning.

Correct:

if True:
    print("A")

print("B")

Produces

A
B

Different indentation:

    if True:
        print("A")
        print("B")

Produces

A
B

Looks similar.

But now both statements belong to the if.

If the condition becomes False:

First version:

B

Second version:

(nothing)

Indentation is syntax in Python.

    else

Sometimes we want two possible paths.

    age = 20

    if age >= 18:
        print("Adult")
    else:
        print("Minor")

Exactly one branch executes.

Never both.

Mental Model
    Evaluate condition

    ↓

    True?

    ↓

    Yes
        Run if block

    No
        Run else block
Example
    temperature = 35

    if temperature > 30:
        print("Hot")
    else:
        print("Cool")
AI Example
    dataset = []

    if dataset:
        print("Start training")
    else:
        print("Dataset is empty")

This combines yesterday's lesson (truthiness) with today's lesson (branching).

elif

Sometimes there are more than two possibilities.

    score = 82

    if score >= 90:
        print("A")

    elif score >= 80:
        print("B")

    elif score >= 70:
        print("C")

    else:
        print("Fail")

Output

B
Important

Python checks conditions from top to bottom.

The first true condition wins.

The rest are ignored.

Example:

    age = 25

    if age > 10:
        print("Older than 10")

    elif age > 20:
        print("Older than 20")

Output:

    Older than 10

Even though 25 is also greater than 20.

Why?

Because Python never reaches the second condition.

The first one already matched.

Correct ordering:

    age = 25

    if age > 20:
        print("Older than 20")

    elif age > 10:
        print("Older than 10")

Now the more specific condition comes first.

A Common Beginner Mistake

Writing:

    if score >= 90:
        ...

    if score >= 80:
        ...

    if score >= 70:
        ...

These are three independent if statements.

All of them are evaluated.

Example:

    score = 95

    if score >= 90:
        print("A")

    if score >= 80:
        print("B")

    if score >= 70:
        print("C")

Output:

A
B
C

Probably not what you wanted.

Using elif:

    score = 95

    if score >= 90:
        print("A")

    elif score >= 80:
        print("B")

    elif score >= 70:
        print("C")

Output:

A

Exactly one branch executes.

Nested if

An if block can contain another if.

    logged_in = True
    is_admin = False

    if logged_in:

        print("Welcome")

        if is_admin:
            print("Admin Panel")

        print("Dashboard")

Output

Welcome
Dashboard

The second condition is only checked if the first one succeeds.

AI Engineering Example

Imagine a training pipeline.

    model_loaded = True
    dataset_loaded = True
    gpu_available = False

    if model_loaded:

        if dataset_loaded:

            if gpu_available:
                print("Training on GPU")
            else:
                print("Training on CPU")

This is how real software often works.

One decision leads to another.

Combining Conditions

Python supports logical operators too.

model_loaded = True
dataset_loaded = True

if model_loaded and dataset_loaded:
    print("Ready")

We'll study and, or, and not in much greater depth later in this chapter.

Real AI Example
    loss = 0.023

    if loss < 0.01:
        print("Excellent")

    elif loss < 0.05:
        print("Good")

    elif loss < 0.10:
        print("Acceptable")

    else:
        print("Needs more training")

This style appears everywhere in ML pipelines.

Another Example
accuracy = 96

if accuracy >= 99:
    print("Production Ready")

elif accuracy >= 95:
    print("Almost Ready")

else:
    print("Needs Improvement")
Mental Model of Branching

Think of an if statement as a railway switch.

             Condition
                 │
          ┌──────┴──────┐
          │             │
        True          False
          │             │
      Execute A     Execute B

Execution doesn't split.

It chooses one path.

Then continues.

Mini Code Challenge

Without running it, predict the output.

x = 15

if x > 20:
    print("A")
else:
    print("B")

print("Done")

Predict:

score = 85

if score >= 90:
    print("A")

elif score >= 80:
    print("B")

else:
    print("C")

Predict:

logged_in = False

if logged_in:
    print("Dashboard")

print("Home")

Predict:

value = 0

if value:
    print("True")
else:
    print("False")
Best Practices

✅ Keep conditions simple.

if users:

instead of

if len(users) > 0:

when you're simply checking if it's empty.

Order conditions from most specific to least specific.

Bad:

if age > 10:

before

elif age > 20:

Good:

if age > 20:

before

elif age > 10:

Avoid deeply nested if statements when possible.

This:

if A:
    if B:
        if C:
            ...

often becomes harder to read than restructuring the logic.

Summary

Today you learned:

if executes code conditionally.
else provides an alternative path.
elif allows multiple mutually exclusive choices.
Python checks conditions from top to bottom.
The first matching branch executes.
Indentation defines code blocks.
Separate if statements behave differently from an if/elif chain.
This control flow forms the backbone of AI pipelines, web applications, games, and nearly all non-trivial software.
