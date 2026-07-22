# Exercises

As before, don't run the code. Reason from the mental model.

## Exercise 1 — Defining vs Calling

In your own words:

What is the difference between defining a function and calling a function?
Which one creates the function object?
Which one creates the execution frame?
Why are these two events completely separate?

The core difference: Defining a function is the creation of a tool; calling a function is using that tool. Defining bundles a recipe (bytecode) into an object and stores it. Calling allocates a workspace and runs that recipe.

Which one creates the function object: Defining the function (def).

Which one creates the execution frame: Calling the function (()).

Why they are completely separate events: Separation decouples preparation from execution. It allows a function to be designed once, stored in memory as a reusable executable object, passed around your architecture like data, and triggered only when specific conditions are met.

## Exercise 2 — Following the Timeline

Consider:

    print("Start")

    def greet():
        print("Hello")

    print("Middle")

    greet()

    print("End")

Without running it, answer conceptually:

At what point is the function object created?
At what point does "Hello" actually execute?
How many execution frames are created for greet()?
Is the function object recreated when greet() is called?


At what point is the function object created: Right after "Start" is printed, when Python evaluates the def greet(): block.

At what point does "Hello" execute: Right after "Middle" is printed, when the interpreter encounters the explicit call invocation greet().

How many execution frames are created for greet(): Exactly one execution frame is created, which spawns when greet() is called and collapses when it returns.

Is the function object recreated when called: No. Python uses the exact same function object created during the definition phase. Calling it simply looks up that existing object via its reference and runs its bytecode.

## Exercise 3 — AI Engineering Thinking

Imagine a deep learning framework loads this callback:

def save_checkpoint():
    ...

The callback is registered when training starts but isn't called until the end of every epoch.

Explain conceptually:

Why is it useful that defining the function doesn't execute it immediately?
Why can the framework safely store the function object for later?
What problems would occur if def automatically executed the function body?

Why deferred execution is useful: It allows the framework to configure blueprint behaviors ahead of time. You can define what should happen during an event (e.g., saving a checkpoint) long before the data or the conditions required to execute that event (e.g., completing 10,000 steps of training data) even exist.

Why the framework can safely store it: Because a function is a first-class object in heap memory. The framework treats the function reference exactly like an integer or a string, storing it in a list of callbacks where it will sit securely until invoked.

What problems would occur if def executed immediately:The framework would attempt to save a model checkpoint before any weights have actually been initialized or trained.The code would run exactly once at startup, making it impossible to reuse the callback loop dynamically at the end of epoch 1, epoch 2, and epoch 3.