# Exercises

As usual, don't run the code. Reason from the mental model.

## Exercise 1 — Why This Order?

In your own words:

Why does Python search:

Local → Enclosing → Global → Built-in

instead of the opposite?

Think about predictability, flexibility, and modularity.


Predictability (Self-Containment): A function should rely on its own internal logic first. If you define x = 5 inside a function, you expect x to be 5. Starting locally guarantees that external code cannot silently hijack or alter the variables your function depends on.

Flexibility (Shadowing): This order allows developers to safely reuse common, intuitive names (like status, data, or count) locally without worrying about whether those names are already used globally or inside Python's core libraries.

Modularity: It allows functions to operate as independent blocks. A function can be written, tested, and moved to an entirely different file or project, and its internal logic will remain unbroken because it resolves its own local variables first.

## Exercise 2 — Following the Lookup

Consider:

    x = "Global"

    def outer():
        x = "Outer"

        def inner():
            print(x)

        inner()

Conceptually answer:

Where does inner() first search for x?

Why doesn't it print "Global"?

Which namespace supplies the name?

Is any string copied?

Where does inner() first search for x?
It searches its own Local namespace (inside the body of inner()).

Why doesn't it print "Global"?
Because Python stops searching the moment it finds a match. Following the LEGB chain, Python looks locally first (finds nothing), then moves to the Enclosing scope (outer). Inside outer, it finds x = "Outer". Because a match is found in the enclosing scope, Python stops looking entirely and never reaches the global scope.

Which namespace supplies the name?The Enclosing namespace of the outer() function supplies the name.

Is any string copied?No. No strings are copied. Python simply passes the memory address reference of the existing string "Outer" to the print() function.


## Exercise 3 — Shadowing

Suppose:

value = 100

def calculate():
    value = 5
    print(value)

calculate()
print(value)

Without running the code, explain:

Why are the two value names different?
Which namespace owns each one?
Why does the global value remain unchanged?


Why are the two value names different?They are different because they exist in two entirely separate namespaces (lookup tables) created at different execution layers. The local variable value inside calculate() shadows (hides) the global variable value, but it does not overwrite it.

Which namespace owns each one?The value = 100 is owned by the Global namespace.The value = 5 is owned by the Local namespace of the calculate() function execution frame.

Why does the global value remain unchanged?Because the assignment value = 5 takes place entirely within the local scope of calculate(). In Python, assigning a variable inside a function automatically creates a new local entry by default. It does not look outside to the global scope for assignments unless explicitly told to do so via the global keyword. Therefore, the global value remains completely untouched at 100.


## Exercise 4 — Architecture Thinking

Imagine Python searched in this order instead:

Global → Local → Built-in

Describe at least four serious problems this would create for:

reusable functions
libraries
debugging
software architecture
AI systems

Focus on why Python's actual design is the better one.

If Python flipped its lookup order to Global → Local → Built-in, it would introduce these four catastrophic architectural failures:

1. Completely Unusable Third-Party LibrariesIf global scopes took priority, importing an external library would become incredibly dangerous. If you wrote a local function using a variable named config, and a library you imported also happened to have a global variable named config, your function would silently read the library's global variable instead of your local one. You would have to know every single global variable name inside every library you use just to write a safe local function.

2. Destruction of Function Reusability and Pure FunctionsFunctions would no longer be black boxes. A function's behavior would completely change depending on the environment it is executed in. If a global variable with an identical name suddenly appears elsewhere in the codebase, your function would immediately stop reading its own local parameters and start reading that global value. This destroys the concept of predictable, reusable code components.

3. Invisible "Spooky Action at a Distance" DebuggingDebugging would become a nightmare. If a local calculation suddenly produces a wrong number, you could no longer debug it just by looking at the function itself. You would have to scan the entire global state of the application to see if some completely unrelated module added a global variable that hijacked your function's inner logic.

4. Severe Vulnerability and Instability in AI SystemsIn modern AI workflows, data pipelines, model weights, and hyperparameters are often held globally in memory (e.g., in a Jupyter Notebook or a production orchestration script). If global took precedence, local training steps, loops, or batch counters (like for epoch in range...) would break if an epoch variable existed globally. A distributed training cluster could experience silent data corruption if one node sets a global variable that unknowingly overrides local computations on another thread.