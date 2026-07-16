# Exercises
## Exercise 1

In your own words:
What problem does a compiler solve?
A compiler translates human-readable code into raw computer instructions (machine code) all at once before the program runs. It solves the problem of bridging the gap between how humans naturally write logic and the strict, 1-and-0 binary language the CPU requires

Exercise 2

What problem does an interpreter solve?
How is it different from a compiler?
An interpreter translates and executes human-readable code line-by-line while the program runs. Unlike a compiler that creates a permanent, standalone file before you can play or test the code, an interpreter allows you to run it immediately. It acts as a live translator sitting next to the computer.


Exercise 3

Why does Go usually produce an executable file, while Python usually doesn't?
Why does Go produce an executable, while Python usually doesn't?Go is statically typed and uses a heavy compiler to translate all source code directly into a single, standalone machine-code file. Python, however, uses a system that relies on a software program (the interpreter) to read and execute your script on-the-fly, meaning the raw Python code must be translated every single time it runs

Exercise 4

Conceptually, what is bytecode?
Why do you think Python uses it?


Bytecode is a low-level, platform-independent intermediate language. it's like a universal translation: it is not raw machine code for a specific computer, but it is much closer to what the machine needs than plain English code. Python uses it to be portable. You can share your code, and the Python Virtual Machine (PVM) on any operating system takes that bytecode and executes it

Exercise 5

Which statement is more accurate?

A.

Python is interpreted.

B.

CPython compiles Python source code into bytecode, which is then executed by the Python Virtual Machine.

Explain why.
Statement B is much more accurate. Python is not purely interpreted line-by-line from plain text. Instead, CPython first converts your .py files into  bytecode files, and then a piece of software called the Python Virtual Machine (PVM) reads and acts on that bytecode

Exercise 6 (Thinking)

Suppose Python were changed tomorrow so that it compiled directly into machine code like Go.

What advantages might that bring?
What Python features might become more difficult to support?

Compiling to machine code would make Python run blazingly fast because the CPU could execute instructions instantly. However, this would make highly dynamic features—like modifying classes or functions while the program is running, or using the eval() function to run text as code—much more difficult or impossible to support, as those actions depend on having a live interpreter present

Exercise 7 (Challenge)

Imagine you write an AI model in Python.

Most of the time is spent multiplying huge matrices.

Why can Python still be fast even though Python itself isn't compiled directly into native machine code?

In Python, heavy-duty tasks like multiplying huge matrices are handed off to compiled, low-level libraries (like NumPy) written in C or C++. Even though you type your commands in Python, you are actually triggering ultra-fast, pre-compiled machine-code operations in the background. The Python code acts simply as a lightweight "remote control" telling a fast, native machine to do the heavy lifting.


Exercise 8 

Imagine two people write the exact same AI algorithm:

Person A writes it in pure Python.
Person B writes the performance-critical parts in C and exposes them to Python.

Why will Person B's version often be dramatically faster, even though both are "using Python"?

Don't answer with:

In Python, code must pass through the Python Virtual Machine (PVM) during execution, which checks types and manages memory dynamically. This adds a lot of steps and slows down the CPU. Person B's C code, on the other hand, was sent through a compiler beforehand, meaning it was translated directly into raw CPU instructions. During the heavy matrix operations, the CPU skips the slow, line-by-line PVM translation and processes the C instructions directly at peak hardware speed



