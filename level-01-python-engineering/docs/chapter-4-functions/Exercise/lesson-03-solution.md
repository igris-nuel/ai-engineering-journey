# Exercises

As always, don't run code. Reason from the mental model.

## Exercise 1 — What Is a Parameter?

In your own words:

What is a parameter?
Is a parameter an object?
Is it a variable?
When does it become a local variable?

What it is: A parameter is a placeholder slot defined by a function. It is a contractual blueprint stating, "When someone calls me, they must provide a piece of data to fill this slot.

Is it an object: No. A parameter is not an object in memory; it is merely a text label (metadata) stored inside the function's structural blueprint.

Is it a variable: Not yet. It only represents the future name of a local variable.When it becomes a local variable: It transforms into a real local variable the exact moment the function is called. 

Python spawns an execution frame and registers that parameter name directly into the frame's local namespace dictionary.

## Exercise 2 — Following the Timeline

Consider:

    def process(data):
        return data

Without running it, answer:

After Python executes the def statement, what exists?
Does a variable called data exist yet?
Where is the parameter information stored?
What new thing is created when process(...) is eventually called?

What exists after def executes: A single function object sits in heap memory, bound to the name process in the current namespace.

Does a variable called data exist yet: No. The identifier data does not exist as a variable anywhere in memory yet.

Where the parameter information is stored: It is stored as static structural metadata inside the process function object (specifically within its underlying code object component, tracking that it requires exactly one positional input).

What new thing is created when called: An execution frame is created. Inside this frame's namespace, the name data is officially registered as a local variable and bound to whatever object argument was passed into the call.

## Exercise 3 — AI Engineering Thinking

Imagine an AI framework defines:

    def train(model, optimizer, dataset):
        ...

The framework imports this file but doesn't start training until two hours later.

Explain conceptually:

Why don't model, optimizer, and dataset exist immediately?
Why is storing only the parameter metadata more efficient?
What would happen if Python allocated parameter variables as soon as it read the def statement?

Why they don't exist immediately: At the time of import, the actual objects (the giant neural network weights, the optimizer states, the gigabytes of data tensors) have not been loaded, instantiated, or allocated in memory. The parameters are just empty slots waiting for those heavy assets to be created later.

Why storing only metadata is efficient: It keeps the system's memory footprint incredibly lightweight at startup. Python only needs to store a few bytes of string characters ("model", "optimizer", "dataset") to remember the function's shape, rather than reserving actual runtime memory buffers.

What would happen if Python allocated variables immediately at def:
The namespace would be polluted with unassigned, dangling variables before their actual objects even exist.

It would break reusability entirely. If the parameter names were globally fixed at definition time, you could not run two training runs with different models or datasets simultaneously, because they would fight over the exact same variable slots.