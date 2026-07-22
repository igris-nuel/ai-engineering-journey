# Exercises

As always, don't run the code. Build the answer from the mental model.

## Exercise 1 — Parameter vs Argument

In your own words:

What is a parameter?

What is an argument?

Which one belongs to the function?
Which one belongs to the caller?

Parameter: The placeholder slot defined in the function's signature. It belongs entirely to the function as part of its static structural metadata.

Argument: The actual data value or object passed into the function call. It belongs to the caller, existing in the caller's context before the function ever runs.

## Exercise 2 — Following the Call

Consider:

user = "Alice"

def greet(name):
    return name

greet(user)

Without running it, answer:

Before greet(user) executes, where does the object "Alice" exist?
When the call begins, is a new string created?
What new thing is created?
Which name points to "Alice" before the call?
Which names point to "Alice" during the call?

Where "Alice" exists before the call: It exists as a string object sitting independently in heap memory, with its address referenced by the name user in the global (or caller's) namespace.

Is a new string created: No. Python absolutely does not copy or duplicate the string object.

What new thing is created: A new execution frame for greet(). Inside this frame's local namespace, the parameter name name is registered.

Name pointing to "Alice" before the call: Only the name user.

Names pointing to "Alice" during the call: Both user (in the caller's namespace) and name (in the function's local namespace) point to the exact same string object in heap memory simultaneously.


## Exercise 3 — AI Engineering Thinking

Suppose you have:

model = huge_neural_network()

train(model)

The model occupies 25 GB of RAM.

Conceptually explain:

Is a second 25 GB model created when train(model) is called?
What is actually passed into the function?
Why is this design critical for high-performance AI frameworks like PyTorch, TensorFlow, and JAX?
What would happen if Python copied the model every function call?


Is a second 25 GB model created: No. The model is never duplicated.

What is actually passed: Python passes only a reference (a memory address pointer). This pointer is incredibly lightweight, occupying just 8 bytes of memory on a standard 64-bit system.

Why this design is critical: High-performance AI frameworks rely on sharing massive data arrays (like model weights and dataset tensors) across hardware buffers (RAM and VRAM). Passing lightweight references allows functions like train, evaluate, or checkpoint to manipulate the same underlying data instantly without performance penalties.

What would happen if Python copied the model:

System Crashes: The system would instantly run out of memory (OOM error) because duplicating a 25 GB model would require an immediate 50 GB of RAM.

Extreme Latency: The CPU and GPU would waste massive amounts of clock cycles copying gigabytes of weights back and forth, turning a fast training loop into an incredibly slow process.