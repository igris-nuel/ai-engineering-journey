## Lesson 8 — for/else and while/else

Let's clear up the biggest misconception immediately.

This:

    for ...
        ...
    else:
        ...

does not mean:

"Run the else if the loop condition is false."

That is wrong.

Instead, the mental model is:

The else belongs to the loop, not to an if.

It means:

"Run this block if the loop finishes normally."

The important word is normally.

## What Does "Normally" Mean?

A loop can end in two ways.

### Way 1 — Natural Completion

The loop simply runs out of work.

Example:

for number in [1, 2, 3]:
    print(number)

print("Done")

The loop processed every item.

This is a normal completion.

### Way 2 — Premature Exit

Something interrupts the loop.

Usually:

break

Example:

    for number in [1, 2, 3]:
        break

The loop did not finish naturally.

It was interrupted.

The else block exists to distinguish these two situations.

### First Example
    for number in [1, 2, 3]:
        print(number)
    else:
        print("Loop completed")

Output

1
2
3
Loop completed

Why?

Because the loop finished normally.

### Example with break
    for number in [1, 2, 3]:

        if number == 2:
            break

        print(number)

    else:
        print("Loop completed")

Output

1

Notice

The else never runs.

Why?

Because the loop was interrupted.

## Visual Timeline

Normal

    Iteration

    ↓

    Iteration

    ↓

    Iteration

    ↓

    No More Items

    ↓

    ELSE Runs

Interrupted

    Iteration

    ↓

    Iteration

    ↓

    BREAK

    ↓

    Exit Loop

    ↓

    ELSE Skipped

## Why Does Python Have This?

Imagine searching for something.

There are two possibilities.

    You find it.
    break

or

    You never find it.
    else

Instead of writing another flag variable,

Python lets the loop itself tell you what happened.

## Traditional Approach

Without loop-else

    found = False

    for name in names:

        if name == target:
            found = True
            break

    if not found:
        print("Not found")

Works.

But requires extra state.

Pythonic Approach
    for name in names:

        if name == target:
            print("Found")
            break

    else:
        print("Not found")

Cleaner.

The loop already knows whether it finished normally.

## Real AI Example

Suppose you're validating images.

    for image in dataset:

        if image_is_corrupted(image):
            print("Dataset invalid")
             break

    else:
        print("Dataset validated")

Meaning

    If corruption found

    ↓

    Stop

    Otherwise

    ↓

    Entire dataset is valid

Very expressive.

### Another AI Example

Searching for the best checkpoint.

    for checkpoint in checkpoints:

        if checkpoint.score > best_score:
            print("Found better checkpoint")
            break

    else:
        print("No better checkpoint")

Again,

No extra variable needed.

## while/else

Exactly the same rule.

Example

    count = 1

    while count <= 3:
        print(count)
        count += 1
    else:
        print("Finished")

Output

1
2
3
Finished

Loop ended naturally.

Now add break.

    count = 1

    while count <= 5:

        if count == 3:
            break

        print(count)
        count += 1

    else:
        print("Finished")

Output

1
2

No Finished.

The loop did not complete naturally.

Important Clarification

Many beginners think

while condition:
    ...
else:

means

"Run else when condition becomes false."

That happens to be true only if the loop wasn't interrupted by break.

## The real rule is simpler:

Else runs only after normal loop completion.

Does continue Affect else?

No.

Example

    for x in range(5):

        if x == 2:
            continue

        print(x)

    else:
        print("Done")

Output

0
1
3
4
Done

continue skips an iteration.

It does not terminate the loop.

So else still executes.

## What About return?

Suppose

    def search():

        for item in items:

            if good(item):
                return item

        else:
            print("Nothing found")

If return happens,

the function exits immediately.

The else is skipped because the loop never completed normally.

## Production Example

Retry logic.

    MAX_RETRIES = 3

    for attempt in range(MAX_RETRIES):

        if connect():
            print("Connected")
            break

    else:
        print("Connection failed")

Beautiful.

Meaning

    Try

    ↓

    Success?

    ↓

    Stop

    Otherwise

    ↓

    After all retries fail

    ↓

    Connection failed

You'll see this pattern in networking libraries.

### Another AI Example

Waiting for a GPU.

    for _ in range(10):

        if gpu_ready():
            print("GPU Ready")
            break

        wait()

    else:
        raise RuntimeError("GPU never became ready")

Exactly the same idea.

When Should You Use Loop-Else?

Good uses:

    Searching
    Retry loops
    Validation
    Resource discovery
    AI checkpoint search
    Configuration lookup

Less good:

When the loop is doing many unrelated things.

In those cases, explicit logic may be clearer.

## Common Beginner Mistake

Thinking this

for ...
else:

is attached to an if.

It isn't.

It's attached to the loop.

Always ask:

Did the loop finish normally?

If yes,

run else.

