# Lesson 12
## The Python Interpreter

I want to correct a very common misconception.

Many people think:

"Python is installed on my computer."

That's not technically accurate.

What you install is a Python implementation.

The most common one is called CPython.

That distinction matters.

The First Big Question

Imagine your computer has:

CPU ✅
RAM ✅
SSD ✅

Now you create a file:

print("Hello")

and save it as:

app.py

Question:

Can the CPU execute app.py directly?

No.

We already know why.

The CPU only understands machine instructions.

So something has to sit between your Python code and the CPU.

That "something" is the Python interpreter.

## What Is the Python Interpreter?

The Python interpreter is a program.

That's it.

It's not hardware.

It's not part of the CPU.

It's simply another program stored on your computer.

For example:

    SSD

    ├── python.exe
    ├── chrome.exe
    ├── vscode.exe
    └── app.py

Notice something.

python.exe is just another application.

Just like Chrome.

Just like VS Code.

Wait…

This raises an interesting question.

If the Python interpreter is just another program...

## Who runs the interpreter?

Excellent question.

The operating system loads it into RAM.

The CPU executes the interpreter's machine instructions.

The interpreter then processes your Python program.

Think of it like this:

    CPU
        ↑
    Runs
        ↑
    Python Interpreter
        ↑
    Processes
        ↑
    Your Python Code

Notice the order.

The CPU never executes Python source code.

It executes the interpreter.

Mental Model

Imagine a chef.

The chef (CPU) only understands recipes written in one language.

You bring a recipe written in French (Python).

A translator (the interpreter) stands beside the chef.

The translator reads one instruction from the recipe and tells the chef what to do.

The chef never reads French.

The chef only follows instructions from the translator.

## What Happens When You Run
python app.py

Let's simplify the sequence.

### Step 1

The operating system finds:

python.exe

on your SSD.

### Step 2

The operating system loads python.exe into RAM.

Remember:

Programs live on SSD.

Running programs live in RAM.

You've already mastered this.

### Step 3

The CPU begins executing the machine instructions inside python.exe.

Notice something important.

The CPU is not executing app.py.

It is executing the interpreter.

### Step 4

The interpreter opens:

app.py

and reads its contents.

Example:

x = 10
print(x)

At this point it's just text stored in memory.

Nothing has executed yet.

### Step 5

CPython compiles the source into bytecode.

    Conceptually:

    Python Source

        ↓

    Bytecode

This happens automatically.

You usually don't notice it.

### Step 6

The Python Virtual Machine (inside CPython) executes that bytecode.

As it executes bytecode, it performs operations that eventually become machine instructions executed by the CPU.

Putting It All Together

Here's the complete conceptual pipeline:

    app.py (SSD)

        ↓

    Operating System

        ↓

    python.exe loaded into RAM

        ↓

    CPU executes python.exe

        ↓

    CPython reads app.py

        ↓

    Compiles to bytecode

        ↓

    Python Virtual Machine executes bytecode

        ↓

    CPU executes resulting machine instructions

        ↓

    Output

Read that diagram several times.

This is one of the most important diagrams you'll ever learn.

The Interpreter Is Also Software

This surprises many people.

The interpreter itself was written by programmers.

Mostly in C.

That means:

    Python Code

        ↓

    CPython (written in C)

        ↓

    Machine Code

        ↓

       CPU

Notice the recursion.

Python runs because another program understands Python.

## Why Multiple Python Implementations Exist

You may have heard names like:

CPython
PyPy
Jython
IronPython

These are all Python implementations.

They all aim to execute Python code, but they use different internal strategies.

For now, just know:

CPython is the standard implementation and the one we'll use throughout this course.

## CPU vs Interpreter

This distinction is critical.

CPU	                            Python Interpreter
Hardware	                    Software
Executes machine instructions	Processes Python programs
Physical chip	                Program on disk
Doesn't understand Python	    Understands Python syntax

Never confuse the two.

## Common Misconception

People often say:

"Python executes my code."

That's not precise.

A better statement is:

The CPython interpreter processes my Python source code, and the CPU executes the interpreter's machine instructions.

It's longer.

But it's accurate.

As engineers, we value accurate mental models.

## AI Connection

When you write:

import torch

The interpreter loads the PyTorch module.

Later, when you call:

output = model(x)

The interpreter coordinates the work, but the heavy numerical computation is carried out by optimized native code (often C/C++ and, on GPUs, CUDA) that the CPU or GPU executes.

Again:

Python orchestrates.

Native code computes.


## Key Insight

The Python interpreter is a software program, not hardware.

When running a Python program, the CPU executes the interpreter, and the interpreter processes the Python source code by compiling it to bytecode and executing that bytecode through the Python Virtual Machine.


 Supervisor Challenge

I'm raising the bar again.

I don't want a one-sentence answer.

I want a complete execution story.

Imagine someone asks you:

"What exactly happens from the moment I press Enter after typing python app.py until print("Hello") appears on the screen?"

Don't skip steps.

Start from:

the operating system,
loading programs from SSD,
RAM,
CPU,
the interpreter,
bytecode,
the Python Virtual Machine,
and end at the output.

If you can explain that pipeline clearly, you've crossed an important threshold. It means you're no longer treating Python as a black box—you understand how the pieces fit together.