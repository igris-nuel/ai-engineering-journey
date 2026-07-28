# Lesson 3 — List Comprehensions

Why Do They Exist?

Suppose you want the square of every number.

The traditional approach:

    numbers = [1, 2, 3, 4, 5]

    squares = []

    for number in numbers:
        squares.append(number ** 2)

    print(squares)

Output:

    [1, 4, 9, 16, 25]

This works.

But notice the pattern:

Create an empty list.

    Loop.
    Transform each element.
    Append it.

Python saw this pattern repeated millions of times and introduced a concise syntax.

The Same Code with a Comprehension

    numbers = [1, 2, 3, 4, 5]

    squares = [number ** 2 for number in numbers]

    print(squares)

Exactly the same result.

A comprehension is not magic.

Conceptually, Python is still:

    iterating,
    evaluating an expression,
    building a new list.

## The Mental Model

Think of a comprehension as answering one question:

"What should every element in the new list look like?"

General form:

    [
        expression
        for item in iterable
    ]

Read it almost like English:

"Create a list of expression for every item in iterable."

## Mapping

Transform every element.

    prices = [10, 20, 30]

    taxed = [price * 1.1 for price in prices]

    print(taxed)

AI Example:

Normalize pixels.

    pixels = [0, 64, 128, 255]

    normalized = [
        pixel / 255
        for pixel in pixels
    ]

## Filtering

Keep only some elements.

    numbers = [-3, -1, 0, 2, 5]

    positive = [
        number
        for number in numbers
        if number >= 0
    ]

    print(positive)

Output:

    [0, 2, 5]

Production example:

    active_users = [
        user
        for user in users
        if user.is_active
    ]

Very common.

Transform + Filter

Both together.

    numbers = [1, 2, 3, 4, 5]

    squares = [
        number ** 2
        for number in numbers
        if number % 2 == 0
    ]

Output

    [4, 16]

AI Example

    embeddings = [
        model.encode(text)
        for text in documents
        if text.strip()
    ]

Notice how readable this is.

## Calling Functions
    values = [-4, -2, 0, 2, 4]

    absolute = [
        abs(value)
        for value in values
    ]

Calling methods:

    documents = [
        "  Hello",
        " World  ",
        " Python "
    ]

    clean = [
        document.strip().lower()
        for document in documents
    ]

Output:

    ['hello', 'world', 'python']

This style is extremely common in NLP preprocessing.

Creating Tuples
    pairs = [
        (number, number ** 2)
        for number in range(5)
    ]

Output

    [(0,0), (1,1), (2,4), (3,9), (4,16)]

Production example:

    indexed_tokens = [
        (index, token)
        for index, token in enumerate(tokens)
    ]

Very common.

Nested Comprehensions

Suppose

    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

Flatten it.

Traditional:

    flat = []

    for row in matrix:
        for value in row:
            flat.append(value)

Professional:

    flat = [
        value
        for row in matrix
        for value in row
    ]

Read it carefully.

The order is:

Iterate rows.
Iterate values.
Produce value.

Output

    [1, 2, 3, 4, 5, 6]

## Cartesian Products

Your earlier example.

    pairs = [
        (x, y)
        for x in [1, 2, 3]
        for y in [3, 1, 4]
        if x != y
    ]

Production AI example:

    experiments = [
        (learning_rate, batch_size)
        for learning_rate in [0.001, 0.0001]
        for batch_size in [16, 32, 64]
    ]

This generates all hyperparameter combinations.

## Conditional Expressions

Don't confuse filtering with conditional expressions.

Filtering:

    [number for number in numbers if number > 0]

Conditional expression:

    labels = [
        "positive" if score > 0 else "negative"
        for score in scores
    ]

Notice:

The if...else comes before the for.

Another example:

    parity = [
        "even" if number % 2 == 0 else "odd"
        for number in range(6)
    ]

Output:

    ['even', 'odd', 'even', 'odd', 'even', 'odd']

When NOT to Use Comprehensions

A mistake juniors often make:

    results = [
        process(image)
        for image in dataset
        if validate(image)
        if resize(image)
        if normalize(image)
        if augment(image)
    ]

Technically valid.

Practically awful.

Too much logic.

Prefer:

    results = []

    for image in dataset:
        if not validate(image):
            continue

        image = resize(image)
        image = normalize(image)
        image = augment(image)

        results.append(process(image))

Readable.

Maintainable.

Another Bad Example

    [
        complicated_function(
            another_function(
                transform(value)
            )
        )
        for value in values
    ]

Just because you can doesn't mean you should.

## Senior Engineer Rule

A comprehension should answer one simple question.

Good:

"Create a new list."

Bad:

"Run an entire workflow."

## Comprehension vs map()

Instead of

    result = list(map(abs, values))

Most Python engineers write

    result = [
        abs(value)
        for value in values
    ]

It's often easier to read.

## Comprehension vs Loop

Loop:

    processed = []

    for image in dataset:
        processed.append(preprocess(image))

Comprehension:

    processed = [
        preprocess(image)
        for image in dataset
    ]

Both are correct.

The comprehension is usually preferred for straightforward transformations.

## AI Examples
### Tokenization
    tokens = [
        tokenizer(text)
        for text in documents
    ]

### Embeddings
embeddings = [
    model.encode(text)
    for text in documents
]

### Batch Processing
    batches = [
        dataset[index:index + batch_size]
        for index in range(0, len(dataset), batch_size)
    ]

You'll see similar code in training pipelines.

### Image Preprocessing

    processed_images = [
        preprocess(image)
        for image in images
        if image.is_valid
    ]

### Performance

Compared to a manual loop, comprehensions are usually a little faster in CPython because the looping and list-building are optimized internally.

However, the real reason professionals use them is clarity, not micro-optimizations.

If a comprehension becomes difficult to read, the performance gain is not worth it.
