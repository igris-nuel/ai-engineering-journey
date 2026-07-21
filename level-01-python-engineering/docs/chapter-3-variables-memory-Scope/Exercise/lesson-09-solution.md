# Exercises


## Exercise 1 — What Do These Keywords Actually Change?

In your own words:

What does global change?
What does nonlocal change?
What do they not change?

Global Keyword

What it changes: It forces a name inside a local function to bind directly to the global (module-level) namespace.

What it does not change: It does not create a new variable in the local namespace, nor does it affect any intermediate enclosing (closure) namespaces.

Nonlocal KeywordWhat it changes: It forces a name inside a nested function to bind to the nearest variable in an enclosing (parent) function's namespace.

What it does not change: It never looks at or modifies the global namespace, and it cannot bind to a name in the absolute local namespace


## Exercise 2 — Three Namespaces

Consider conceptually:

    x = 1

    def outer():
        x = 2

        def inner():
            ...

Without writing code:

Which namespace owns each x?
If inner reads x, which one does it find?
If inner assigns x = 3 without nonlocal, what happens?
If inner uses nonlocal, what changes?

Namespace Ownership
x = 1 is owned by the global (module) namespace.
x = 2 is owned by the outer() function's local namespace (enclosing scope for inner).
inner() initially owns no x variable in its own local namespace.

Reading and Assignment BehaviorReading x: If inner() reads x, it searches upward and finds x = 2 from the outer() namespace.

Assigning x = 3 (No nonlocal): Python creates a brand-new local variable x inside inner(). The x in outer() and the global x remain completely unchanged.

Using nonlocal: Python binds inner's reference of x directly to outer's namespace. Assigning x = 3 changes the value of outer's x to 3.

## Exercise 3 — Architecture Thinking

Suppose an AI training system has a global variable:

current_model

Every helper function modifies it using global.

Explain why this is usually considered poor software design.

Think about:

testing,
maintainability,
concurrency,
debugging.

Also explain why using nonlocal inside a small, well-contained nested workflow is often a much safer design.


Testing: It destroys test isolation. Tests cannot run in isolation because one test modifying current_model pollutes the environment for subsequent tests.

Maintainability: It creates tight coupling. Any change to how current_model is structured requires updating every single helper function across the codebase.

Concurrency: It causes race conditions. If you try to train or evaluate multiple models concurrently using threads, they will overwrite each other's data.

Debugging: It makes state tracking difficult. Because any helper can mutate the global state, finding exactly where a model bug or corruption occurred requires auditing every single function line by line.

Why Nonlocal is a Safer Design

Strict Encapsulation: The scope is tightly bounded. The state variable is hidden inside a specific container workflow and cannot be accessed or corrupted by outside scripts.

Safe Lifecycles: The state only lives as long as the parent function executes. Once the workflow finishes, the memory is cleared safely without leaving lingering global debris.