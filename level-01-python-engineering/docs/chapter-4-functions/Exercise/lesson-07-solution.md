# Exercises

As always, don't run the code. Build the answer from your mental model.

## Exercise 1 — Why a Stack?

In your own words:

Why does Python use a stack instead of storing execution frames randomly?
What property of function calls makes a stack the perfect data structure?
What does "Last In, First Out" mean in the context of function execution?


Why a stack instead of random storage: Python must maintain a strict, chronological record of which function called which function. Storing frames randomly would break this hierarchy, making it impossible to know where to return control when a function completes.

The perfect property of function calls: Function calls are inherently nested. If Function A calls Function B, Function A cannot finish until Function B finishes. The last function to start must be the very first one to end.

What "Last In, First Out" (LIFO) means here: The most recently created execution frame (the "Last In" onto the stack) is the one actively executing on the CPU. It must complete and pop off the stack (the "First Out") before any parent frame underneath it can resume.

## Exercise 2 — Following the Frames

Consider:

def C():
    pass

def B():
    C()

def A():
    B()

A()

Without running the code:

Which frame exists first?
Which frame is pushed next?
Which frame is on top while C() executes?
Which frame disappears first?
Which frame remains until the entire program finishes?


Which frame exists first: The Global (Module) Frame.

Which frame is pushed next: Frame A, when A() is invoked from the global scope.

Which frame is on top while C() executes: Frame C sits at the absolute top of the stack as the active workspace.

Which frame disappears first: Frame C disappears first the moment it hits pass and returns.

Which frame remains until the end: The Global Frame remains active until the entire script finishes execution.

## Exercise 3 — Stack Traces

Suppose this happens:

main()

↓

train()

↓

evaluate()

↓

predict()

↓

Error

Conceptually explain:

Why can Python print the entire sequence of function calls?
Where is this information stored?
Why is this invaluable when debugging large software systems?

Why Python can print the full sequence: Because a stack trace is literally just a snapshot copy of the current live call stack. Python simply reads the stack from bottom to top, printing the file name, line number, and function name of every frame currently waiting in line.

Where this information is stored: It is stored directly in call stack memory, where each execution frame preserves its own tracking metadata (like the exact line of code that triggered the next inner call).

Why it is invaluable for large systems: In a large codebase, a utility function might be called from hundreds of different places. A raw error message telling you what failed is useless without the stack trace telling you the exact execution pathway how the program arrived there

## Exercise 4 — AI Engineering Thinking

Imagine a PyTorch training loop:

train()
    ↓
forward()
    ↓
transformer_block()
    ↓
self_attention()
    ↓
softmax()

During softmax(), an exception occurs.

Explain:

Why are the other functions not executing at the same time?
How does Python know where to resume if no exception occurs?
Why is the call stack essential for understanding deep learning framework error messages?


Why functions aren't executing concurrently: Python's standard execution model is synchronous and single-threaded. When self_attention() calls softmax(), the self_attention frame is frozen and paused. It completely cedes control to softmax() and cannot resume until softmax() finishes its computation.

How Python knows where to resume: Every execution frame contains a "return address" pointer. When softmax() returns successfully, Python pops its frame off the stack, looks at the top frame now exposed (self_attention), reads its stored instruction pointer, and resumes execution on the exact line immediately following the softmax() call.

Why the call stack is essential for deep learning debugging: Deep learning frameworks like PyTorch feature deep layer nesting. If softmax() crashes (e.g., due to a NaN tensor value), looking at the error inside softmax() alone won't tell you anything. The stack trace allows you to trace the bad data backward: from softmax rightarrow self_attention rightarrow transformer_block rightarrow forward, showing you exactly which specific layer or block configuration in your architecture passed the malformed tensor.