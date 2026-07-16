# Lesson 13
## What Happens When Python Runs?

Our Example

We'll use a tiny program:

x = 10
y = 20
print(x + y)

Looks simple.

Under the hood, a lot happens.

## The Big Picture

Here's the full pipeline we'll explore:

        You
         ↓
        Terminal
          ↓
        Operating System
          ↓
        Locate python.exe
          ↓
        Load python.exe into RAM
          ↓
        Create a Process
          ↓
        CPU executes CPython
          ↓
        CPython reads app.py
          ↓
        Compile to Bytecode
         ↓
        Python Virtual Machine executes Bytecode
          ↓
        Objects are created
          ↓
        System Calls
          ↓
        Output appears
          ↓
        Process exits
          ↓
        RAM is released

Every arrow matters.

### Step 1 — You Press Enter

You type:

python app.py

Your terminal isn't running Python.

It's just another program.

Its job is to send your command to the operating system.

### Step 2 — The Operating System Takes Over

The operating system asks:

"What program is named python?"

It searches the executable locations (using the PATH).

Eventually it finds:

python.exe

### Step 3 — Process Creation

This is new.

The operating system creates a process.

What is a process?

A process is:

A running instance of a program together with the resources it needs.

Notice the wording.

Program:

python.exe

Process:

A running copy of python.exe

These are not the same thing.

Program vs Process

Imagine Microsoft Word.

You can open it twice.

word.exe

exists once on disk.

But you can have:

Word Process #1

Word Process #2

Word Process #3

running simultaneously.

Same program.

Different processes.

### Step 4 — Memory Is Allocated

The operating system gives the process memory.

Conceptually:

RAM

+----------------------------+
| CPython Code               |
+----------------------------+

| Python Heap               |
+----------------------------+

| Call Stack                |
+----------------------------+

| Other Runtime Structures  |
+----------------------------+

Don't worry about every section yet.

We'll spend weeks understanding them later.

Today I just want you to know:

A process owns memory.

### Step 5 — CPU Starts Running CPython

Notice something important.

The CPU is still not running your code.

The CPU begins executing the machine instructions that make up CPython itself.

Think of CPython as the engine.

Your Python file is just the input.

### Step 6 — CPython Opens app.py

The interpreter reads:

x = 10
y = 20
print(x + y)

At this moment...

it's still text.

Nothing has executed.

### Step 7 — Parsing

The interpreter checks whether the code is valid Python.

Suppose you wrote:

x ==

The interpreter immediately reports:

SyntaxError

before the program starts executing.

Why?

Because the source couldn't even be understood as valid Python.

### Step 8 — Bytecode Compilation

Valid source becomes bytecode.

Conceptually:

    Python Source

        ↓

    Bytecode

Again:

The CPU does not understand bytecode.

The PVM does.

### Step 9 — Python Virtual Machine Begins Execution

The PVM starts reading bytecode.

Something like:

LOAD_CONST

STORE_NAME

LOAD_NAME

CALL

RETURN

Don't memorize these names.

Just understand:

The PVM is executing instructions designed specifically for Python.

### Step 10 — Objects Are Created

Now something fascinating happens.

When Python sees:

x = 10

It does not simply write 10 into memory.

Instead, Python creates an integer object representing the value 10.

Then it creates the name:

x

which refers to that object.

We'll spend many lessons on this.

For now, remember:

Names are not objects.

That sentence is incredibly important.

### Step 11 — More Objects

Next:

y = 20

Another integer object.

Another name.

Again:

Names point to objects.

They are not the objects.

### Step 12 — Evaluating x + y

The PVM now needs to evaluate:

x + y

Conceptually:

Find the object referenced by x.
Find the object referenced by y.
Perform integer addition.
Create a new integer object for the result (30).

Notice:

Python doesn't "modify" either integer.

We'll later learn why integers are immutable.

### Step 13 — print()

The interpreter encounters:

print(...)

It does not draw text itself.

Instead it eventually asks the operating system:

"Please write these characters to standard output."

That request is called a system call.

The operating system communicates with the terminal.

The terminal displays:

30

### Step 14 — Program Finishes

Execution reaches the end of the file.

The interpreter returns control to the operating system.

### Step 15 — Cleanup

The operating system destroys the process.

Its memory is reclaimed.

RAM becomes available for other programs.

The original files remain safely on the SSD.

Complete Timeline
    SSD
    │
    ├── python.exe
    ├── app.py
    │
    ▼

    Operating System

        ▼

    Create Process

        ▼

    Allocate RAM

        ▼

    CPU executes CPython

        ▼

    CPython reads app.py

        ▼

    Parse

        ▼

    Compile to Bytecode

        ▼

    PVM executes Bytecode

        ▼

    Objects created

        ▼

    System Call

        ▼

    Terminal Output

        ▼

    Process Ends

        ▼

    RAM Released

Read this several times.

## AI Connection

Suppose you write:

prediction = model(image)

The exact same pipeline happens.

The only difference is that inside the model call, Python invokes highly optimized native code that performs millions or billions of numerical operations.

The architecture remains the same.

Common Misconceptions
"Variables store values."

We'll soon learn that's not how Python works.

More accurately:

Names refer to objects.

"The CPU executes Python."

No.

The CPU executes the machine instructions of CPython.

"The interpreter is hardware."

No.

The interpreter is a software program.

## Mental Model

Think of the Python interpreter as the conductor of an orchestra.

The conductor doesn't produce the music.

Instead, the conductor coordinates many players:

Parser
Bytecode compiler
Python Virtual Machine
Memory manager
Garbage collector
Operating system
CPU

Each component has its own responsibility.


## Key Insight

Running a Python program is a collaboration between the operating system, the CPython interpreter, the Python Virtual Machine, the CPU, and memory.

Each component has a distinct responsibility, and understanding their interactions removes the "magic" behind program execution.