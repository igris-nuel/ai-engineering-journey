## Lesson 7 — break and continue

Most beginners learn:

"break stops a loop."

"continue skips an iteration."

True.

But that doesn't explain why they exist.

The real mental model is:

Both keywords change the normal execution path of a loop.

Normally a loop executes like this:

    Start Iteration
        │
        ▼
    Execute Body
        │
        ▼
    Next Iteration

break and continue let you interrupt this normal flow.

## Part 1 — break

Imagine you're searching for one book in a library.

Once you've found it, do you keep checking every shelf?

Of course not.

You stop.

That's exactly what break does.

## Example
    names = ["Alice", "Bob", "Charlie", "David"]

    for name in names:
        print("Checking:", name)

        if name == "Charlie":
            print("Found!")
            break

    print("Search finished")

Output

    Checking: Alice
    Checking: Bob
    Checking: Charlie
Found!
Search finished

Notice something.

Python never checks "David".

Why?

Because break immediately exits the loop.

### Timeline

Iteration 1

    Alice

      ↓

    Condition False

      ↓

    Continue Loop

Iteration 2

    Bob

    ↓

    Condition False

    ↓

    Continue Loop

Iteration 3

Charlie

↓

Condition True

↓

BREAK

↓

Leave Loop

The remaining iterations never happen.

## Memory Doesn't Change

Suppose

number = 10

inside a loop.

Using break doesn't destroy variables.

It simply tells Python:

"Stop creating future iterations."

The execution frame continues after the loop.

Example with while
    count = 1

    while True:
        print(count)

        if count == 3:
            break

        count += 1

    print("Done")

Output

1
2
3
Done

Without break, this would never stop.

## Real AI Example

Imagine scanning thousands of images looking for corruption.

    for image in dataset:

        if is_corrupted(image):
            print("Corrupted image found")
            break

The moment corruption is detected, there's no need to scan the remaining images.

This saves computation.

## Part 2 — continue

continue is different.

It doesn't stop the loop.

It skips the rest of the current iteration.

Imagine inspecting passengers at an airport.

If someone's passport is invalid,

you don't shut down the airport.

You simply skip that passenger and move to the next.

That's continue.

Example
    numbers = [1, 2, 3, 4, 5]

    for number in numbers:

        if number == 3:
            continue

        print(number)

Output

1
2
4
5

Notice

3 isn't printed.

But 4 and 5 still are.

Timeline

Iteration

    1

    ↓

    Condition False

    ↓

    Print 1

Iteration

    2

    ↓

    Condition False

    ↓

    Print 2

Iteration

    3

    ↓

    Condition True

    ↓

    CONTINUE

    ↓

    Next Iteration

Everything below continue is skipped.

Another Example
    for number in range(6):

        if number % 2 == 0:
            continue

        print(number)

Output

1
3
5

The even numbers are ignored.

continue Doesn't Restart the Program

It only skips the remainder of one iteration.

The loop itself continues normally.

### Compare Them
break
    for x in range(10):

        if x == 5:
            break

        print(x)

Output

0
1
2
3
4

Stops completely.

continue
    for x in range(10):

        if x == 5:
            continue

        print(x)

Output

0
1
2
3
4
6
7
8
9

Only skips 5.

## Visual Comparison

Normal loop

    Iteration

    ↓

    Body

    ↓

    Next Iteration

With continue

    Iteration

    ↓

    Condition

    ↓

    continue?

    ↓

    Skip Remaining Body

    ↓

    Next Iteration

With break

    Iteration

    ↓

    Condition

    ↓

    break?

    ↓

    Exit Loop

    ↓

    Continue Program

## Real AI Example — Skip Bad Data

Suppose your dataset contains missing images.

    for image in dataset:

        if image is None:
            continue

        preprocess(image)

Instead of crashing,

you ignore the bad sample.

This is extremely common in production pipelines.

### Another AI Example — Early Stopping

Suppose validation loss suddenly becomes terrible.

    for epoch in range(100):

        train()

        if validation_loss > threshold:
            break

Training stops early.

This saves GPU time.

Modern training frameworks often implement versions of this idea.

Combining Both
    for sample in dataset:

        if sample is None:
            continue

        if is_corrupted(sample):
            break

        process(sample)

Meaning

    Missing sample?

    ↓

    Skip it

    Corrupted sample?

    ↓

    Stop training

    Otherwise

    ↓

    Process sample

## Common Beginner Mistake
    for number in range(5):

        continue

        print(number)

Output

Nothing.

Why?

Because continue skips everything below it in that iteration.

The print() statement is unreachable.

### Another Mistake
    while True:

        if ready:
            continue

        break

If ready is always True,

the break is never reached.

The loop becomes infinite.

Control flow matters.

## Best Practices

Use break when:

    The job is finished.
    Continuing would waste work.
    You found what you were searching for.

Examples:

    Search algorithms
    AI early stopping
    Finding a configuration
    Retry loops

Use continue when:

    The current item is invalid.
    You want to ignore one iteration.
    The remaining items are still useful.

Examples:

    Skip corrupted files
    Ignore missing values
    Filter bad records

Avoid deeply nesting multiple break and continue statements.

If your loop has many exit points, consider extracting the logic into a function.

