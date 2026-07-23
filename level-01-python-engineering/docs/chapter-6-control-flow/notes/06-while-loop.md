# Lesson 6 — while Loops

A common beginner explanation is:

"A while loop repeats until a condition becomes false."

That's correct.

But the real mental model is:

A while loop keeps asking a question before every iteration.

## The Mental Model

Imagine a security guard at a door.

Before letting someone through, he asks:

"Are you allowed in?"

If the answer is Yes, the person enters.

After they leave, he asks the same question again.

    Question?

        ↓

    True?

        ↓

    Run body

        ↓

    Question?

        ↓

    True?

        ↓

    Run body

        ↓

    ...

        ↓

    False?

        ↓

    Exit

A while loop is simply repeated decision-making.

### First Example
    count = 1

    while count <= 3:
        print(count)
        count += 1

Output

1
2
3

## Timeline

Initially

    count ──► 1

Python evaluates

    count <= 3

Result

    True

Execute body

    print(count)
    count += 1

Now

    count ──► 2

Python goes back.

Notice something.

It doesn't continue where it left off.

It jumps back to the top and asks the question again.

### Iteration 2

    count = 2

        ↓

     2 <= 3

       ↓

     True

      ↓

    Run body

      ↓

    count = 3

### Iteration 3

    count = 3

       ↓

    3 <= 3

      ↓

    True

     ↓

  Run body

     ↓

  count = 4

### Iteration 4

    count = 4

       ↓

    4 <= 3

       ↓

    False

      ↓

    Loop ends

Compare with for

A for loop asks:

"Is there another value?"

A while loop asks:

"Is this condition still true?"

Different questions.

Different tools.

## Forgetting to Update

Consider

    count = 1

    while count <= 3:
        print(count)

Python prints

    1
    1
    1
    1
    1
    ...

Forever.

Why?

Because

count

never changes.

The condition never becomes false.

This is called an infinite loop.

### Another Example
    password = ""

    while password != "openai":
        password = input("Password: ")

    print("Access Granted")

Notice something.

Python has no idea how many attempts the user will need.

That makes while the natural choice.

### Countdown
    seconds = 5

    while seconds > 0:
        print(seconds)
        seconds -= 1

    print("Done")

Output

    5
    4
    3
    2
    1
    Done
Reading Until Finished

Suppose you're reading data from a file.

You don't know how many lines exist.

    line = read_line()

    while line is not None:
        process(line)
        line = read_line()

Perfect use case.

## AI Example

Suppose you're waiting for GPU memory.

    gpu_ready = False

    while not gpu_ready:
        print("Waiting...")
        gpu_ready = check_gpu()

    print("Training Started")

Again,

You don't know how many checks are needed.

### Another AI Example

Imagine polling an inference job.

    status = "PENDING"

    while status != "COMPLETED":
        status = check_status()

    print("Inference Finished")

Production systems do this all the time.

## Training Until Convergence

Sometimes we don't know how many epochs are needed.

Instead we stop when loss is sufficiently small.

    loss = 10.0

    while loss > 0.01:
        loss = train_one_epoch(loss)

Notice

No fixed number.

Just a condition.

## Memory View

Suppose

    count = 1

Memory

Global Frame

    count ──► 1

Later

    count += 1

Remember Chapter 2.

Integers are immutable.

Conceptually

    Old Integer (1)

        ↓

    Create Integer (2)

        ↓

    Rebind count

        ↓

    Old integer eventually disappears

Nothing special because it's inside a loop.

It follows exactly the same rebinding rules we've already learned.

Common Beginner Mistake
    items = []

    while len(items) < 5:
        print(items)

Output

    []
    []
    []
    []
    ...

Why?

Nothing changes.

The condition never changes.

Always ask yourself:

What changes that will eventually make the condition false?

## while True

Sometimes infinite loops are intentional.

    while True:
        command = input("> ")

        if command == "quit":
            break

We'll study break next.

This pattern is extremely common.

## Choosing Between for and while

Use a for loop when you already know what you're iterating over.

    for image in dataset:

Use a while loop when you only know the stopping condition.

    while loss > threshold:

    or

    while not connected:
## Real AI Example

Suppose you're training until validation accuracy reaches 95%.

    accuracy = 0.82

    while accuracy < 0.95:
        accuracy = train_next_epoch(accuracy)

    print("Target reached!")

No one knows in advance how many epochs it will take.

That's why production ML systems often use condition-based loops.

## Best Practices

Always ensure something inside the loop changes the condition.

count += 1

Prefer for when iterating over collections.

for batch in train_loader:

Prefer while for waiting, polling, retries, or condition-driven processes.

