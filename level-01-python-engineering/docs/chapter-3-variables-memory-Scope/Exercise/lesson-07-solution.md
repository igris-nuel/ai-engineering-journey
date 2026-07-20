# Exercises
## Exercise 1 — Names vs Objects

In your own words:

What is the difference between the lifetime of a name and the lifetime of an object?
Why are they independent?


Difference: A name is just a sticky note with a label on it. An object is the actual box of data in memory. The label (name) can be created and destroyed, but the box of data (object) will stay in memory as long as at least one person is holding onto it.

Independence: Because multiple names can point to the same object, destroying one name only removes one label; the underlying object survives as long as another name (or system component) references it

## Exercise 2 — Function Frames

Conceptually reason about:

def create():
    x = [1, 2, 3]

create()

Answer:

When does the name x stop existing?
What happens to its namespace?
What happens to the list object?
Why?

When does the name x stop existing? The name x stops existing the exact moment the create() function finishes running.

What happens to its namespace? The local namespace (which acts as a temporary dictionary holding the function's variables) is completely erased.

What happens to the list object? The list object ([1, 2, 3]) is temporarily orphaned in memory because its only label was just destroyed.

Why? Shortly after the function ends, Python’s memory manager (the garbage collector) notices the list has no names pointing to it and deletes it to free up space

## Exercise 3 — Returning Objects

Consider:

def create():
    x = [1, 2, 3]
    return x

numbers = create()

Without running it:

Does the name x still exist?
Does the list still exist?
Which namespace now owns a reference to the list?
Why isn't the list destroyed?


Does the name x still exist? 
No, the local name x is destroyed when the create() function ends.

Does the list still exist? Yes, the list stays in memory.

Which namespace now owns a reference to the list? The global namespace now holds a reference, specifically attached to the variable numbers.

Why isn't the list destroyed? When create() finished, the list object was returned out of the function and assigned to numbers. Because it still has a label/reference, the garbage collector knows not to delete it.

## Exercise 4 — AI Engineering Thinking

Suppose an inference function loads a 12 GB model every time it is called:

def predict():
    model = load_model()

Explain why this design is inefficient.

How would managing object lifetime differently improve performance in a production AI system?

Focus on:

loading time,
memory,
repeated inference,
architecture.

Why this is inefficient: Loading a 12 GB AI model into memory every time you call predict() takes a massive amount of time (input/output wait times) and processor power. Once the function ends, that 12 GB is deleted, forcing the system to repeat this slow process from scratch on the next call.

Managing object lifetime differently: Instead of a local variable, the model object should be loaded once globally (or instantiated as part of a service class) at server startup. By keeping the model object alive continuously, subsequent inference calls simply reference the already-loaded object, eliminating massive loading delays and keeping memory states ready instantly

## Exercise 5 — Challenge

A junior engineer says:

"If a variable disappears, then the object it pointed to must disappear too."

Correct this statement.

Explain:

what actually disappears,
what determines whether an object survives,
why Python was designed this way,
why this distinction is especially important for AI systems that work with large models and datasets.



Correction of the statement: When a variable disappears, only the name (label) vanishes. The data object it points to does not automatically disappear.

What actually disappears: The symbolic name and its reference to the memory address.

What determines whether an object survives: The object survives as long as there is at least one active reference (label or system connection) pointing to it. Python’s garbage collector counts these references; if the counter hits zero, the object is destroyed.

Why Python was designed this way: It allows for flexible programming where objects can be passed around between functions or stored in lists without forcing developers to manually manage computer memory.

Why it matters for AI: Large AI models and datasets take a long time to load. If AI systems do not manage object lifetimes carefully—for example, if they let a massive 50 GB dataset get destroyed and reloaded during a loop—it will drain system memory and cause severe performance lags