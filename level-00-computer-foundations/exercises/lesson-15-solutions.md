# Exercises
## Exercise 1

In your own words:

Why do computers use both a stack and a heap instead of one big memory area?

They are separated because they have different rules for how long data needs to stay in memory. The stack operates like a stack of plates—it automatically adds and removes temporary data in order. The heap is like a giant, messy storage room where you can throw items of any size and leave them there until you are completely done with them. Using both ensures the computer stays organized and doesn't waste time cleaning up tiny pieces of data.

## Exercise 2

What is a stack frame?

What kinds of information does it contain?

A stack frame is a specific block of memory created on the stack every time a function is called. When the function ends, the frame disappears.

It contains:

`Arguments/Parameters`: The inputs given to the function (e.g., a name or number).
Local Variables: Data created inside that specific function.

`Return Address`: A bookmark pointing to exactly where the program left off so it knows where to return when the function is finished.

## Exercise 3

Suppose this function runs:

    def greet(name):
        message = "Hello"

Describe, conceptually, what happens on the stack when greet("Taki") is called.

The computer creates a new stack frame for the greet function.

It pushes the argument name = "Taki" into the stack frame.

It pushes the local variable message = "Hello" into the frame.

The code runs and completes.The stack frame is automatically deleted (popped off), removing "Taki" and "Hello" from memory

## Exercise 4

Why is the stack usually much faster than the heap?

The stack is fast because the computer always adds and removes data from the exact top of the memory pile in a strict, predictable order. The CPU only has to move one pointer to access data, which is highly efficient and cache-friendly. The heap, on the other hand, requires the computer to search through a scattered, unorganized pool of memory to find free space, making it much slower.

## Exercise 5

Consider:

    def make_list():
        numbers = [1, 2, 3]
        return numbers

Why doesn't the list disappear immediately when the function returns?


When the function finishes, the local variable numbers (which is just a tiny reference or "bookmark" on the stack) disappears. However, the actual list data [1, 2, 3] was created on the heap. Because objects on the heap are designed to persist after a function returns, the actual list remains in memory until it is no longer needed or is cleaned up

## Exercise 6 (Thinking)

Imagine a function creates a 2 GB image object.

Why would storing that directly on the stack be a poor design?

The stack is designed to be small, structured, and fast. It has a very limited size. Storing a massive 2 GB object on the stack would immediately fill up all available stack space, causing a stack overflow crash. Furthermore, because of the stack's Last-In-First-Out rule, keeping a 2 GB object there would slow down the entire program.

## Exercise 7 (Challenge)

Suppose a programming language had no heap.

Everything had to be stored on the stack.

Describe at least four major problems that such a language would face.

Think about:

recursion,
large objects,
returning data,
dynamic memory,
AI workloads.


Without a heap, a language would face severe limitations:

No Returning Data (Safely): You could not return objects or arrays from functions. When a function's stack frame disappears, any data inside it would be destroyed, meaning you could never send a newly created object back to the main program.

Limited Recursion: Without heap storage to safely save function states, deep recursion (functions calling themselves over and over) would quickly max out the small stack memory, causing a stack overflow.

No Large Data Objects: All data would be restricted to the tiny size of a stack frame. You could never load large files, high-resolution images, or large AI models into memory.

No Dynamic Memory: You would need to know the exact sizes of all your data before the program runs. You would be unable to build flexible programs that adapt to user inputs or add items to a list on the fly