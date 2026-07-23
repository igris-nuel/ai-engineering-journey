# Lesson 4 — Pattern Matching (match)

This feature was introduced in Python 3.10.

Many beginners think it's just a prettier if.

It isn't.

It solves a different class of problems.

Imagine This

Suppose you're writing an AI assistant.

The user sends a command.

    train
    evaluate
    predict
    export
    quit

One approach is:

    command = "train"

    if command == "train":
        print("Starting training")

    elif command == "evaluate":
        print("Running evaluation")

    elif command == "predict":
        print("Generating predictions")

    elif command == "export":
        print("Exporting model")

    else:
        print("Unknown command")

This works.

But as commands grow...

20...

50...

100...

the code becomes long and harder to scan.

## Enter match

    command = "train"

    match command:

        case "train":
            print("Starting training")

        case "evaluate":
            print("Running evaluation")

        case "predict":
            print("Generating predictions")

        case "export":
            print("Exporting model")

        case _:
            print("Unknown command")

Produces

    Starting training

Notice how it almost reads like a menu.

## Mental Model

Conceptually:

    Evaluate one value

    ↓

    Compare against pattern 1

    ↓

    Match?

    ↓

    Yes

    Execute that case

    ↓

    Stop

Unlike if, you're saying:

"Take this one value and compare it against many possible patterns."

The Wildcard _

The final case usually looks like this:

    case _:

Think of it as:

"Everything else."

It is similar to:

    else:

## Matching Numbers
    status = 404

    match status:

        case 200:
            print("Success")

        case 404:
            print("Not Found")

        case 500:
            print("Server Error")

        case _:
            print("Unknown")

## Matching Strings

    color = "green"

    match color:

        case "red":
            print("Stop")

        case "yellow":
            print("Slow")

        case "green":
            print("Go")
    
## Matching Enums (very common)

Later we'll study Enums.

Imagine:

    status = "FAILED"

    match status:

        case "PENDING":
            print("Waiting")

        case "RUNNING":
            print("Processing")

        case "FAILED":
            print("Retry")

        case "SUCCESS":
            print("Done")

You'll see this style frequently in production code.

## AI Example

Suppose your model supports several tasks.

    task = "classification"

    match task:

        case "classification":
            print("Load classifier")

        case "regression":
            print("Load regressor")

        case "clustering":
            print("Load clustering pipeline")

        case _:
            print("Unsupported task")

## Pattern Matching Isn't Just Equality

Here's where match becomes much more powerful than a long chain of if statements.

It can match the structure of data.

For example:

    point = (0, 0)

    match point:

        case (0, 0):
            print("Origin")

        case (0, y):
            print("Y axis")

        case (x, 0):
            print("X axis")

        case (x, y):
            print("General point")

This is called structural pattern matching.

We're not just comparing values.

We're describing the shape of the data.

## Matching Lists

    data = [1, 2]

        match data:

            case [x, y]:
                print(x, y)

            case _:
                print("Different shape")

If the list has exactly two elements:

    1 2

## Matching Dictionaries
    message = {
        "type": "login",
        "user": "Alice"
    }

    match message:

        case {"type": "login", "user": name}:
            print(f"Welcome {name}")

        case _:
            print("Unknown message")

Notice something amazing.

Python extracts data while matching.

## Guards

You can even add conditions.

    age = 22

    match age:

        case n if n >= 18:
            print("Adult")

        case _:
            print("Minor")

The if here is called a guard.

The pattern must match and the condition must be true.

## When Should You Use match?

Use match when:

    you're checking one value
    against many possibilities
    especially if the possibilities have structure

Good:

    match command:

Less good:

    if x > y:

match isn't designed for arbitrary comparisons.

### When if Is Better

This:

    if temperature > 35:

is naturally an if.

Trying to write it with match becomes awkward.

Use the right tool.

## Real AI Example

Imagine inference requests.

    request = {
        "task": "translate",
        "language": "French"
    }

    match request:

        case {"task": "translate", "language": lang}:
            print(f"Translating into {lang}")

        case {"task": "summarize"}:
            print("Summarizing")

        case {"task": "classify"}:
            print("Classifying")

        case _:
            print("Unknown request")

This is much cleaner than many nested if statements checking dictionary keys.

Another Example

Imagine your orchestration platform (the one we've been designing).

    job_status = "FAILED"

    match job_status:

        case "PENDING":
            print("Waiting")

        case "PROCESSING":
            print("Worker claimed job")

        case "COMPLETED":
            print("Notify user")

        case "FAILED":
            print("Schedule retry")

        case _:
            print("Invalid state")

As your system grows, this is often easier to maintain than a long if/elif chain.

## Best Practices

Use match when one value has many known cases.

    match status:

Keep patterns simple.

Always include:

    case _:

unless you're certain every possible value has been handled.

Don't force match where if is clearer.

