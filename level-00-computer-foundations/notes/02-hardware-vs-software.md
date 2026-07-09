# Hardware

The physical parts of a computer that you can touch.

Examples:
CPU
RAM
SSD
GPU
Keyboard
Monitor
Software

The instructions that tell hardware what to do.

Examples:

Operating System
Browser
Python
VS Code
Games
AI Models
Think Like an Engineer

This file:

print("Hello")

is software.

When it runs, it causes physical events:

electrons move,
voltages change,
memory cells change state,
the CPU executes instructions.

Software is ultimately controlling hardware.

## Anatomy of a Computer

A simplified computer looks like this:

                                    +---------------------+
                                    |      CPU            |
                                    +---------------------+
                                            |
                                            |
                                    +---------------------+
                                    |       RAM           |
                                    +---------------------+
                                            |
                                            |
                                    +---------------------+
                                    |      Storage        |
                                    |    SSD / HDD        |
                                    +---------------------+
                                            |
                                            |
                                    +---------------------+
                                    | Input / Output      |
                                    +---------------------+

Everything revolves around these components.

1. CPU

(Central Processing Unit)

The CPU is the "brain" of the computer.

Its job:

                    Fetch instruction
                           ↓
                    Decode instruction
                           ↓
                    Execute instruction

Millions or billions of times every second.

Examples:

x = 5
y = 7
z = x + y

The CPU performs the addition.

2. RAM

(Random Access Memory)

RAM is the computer's working memory.

It stores:

running programs
variables
open browser tabs
temporary data

RAM is:

Fast
Volatile
Temporary

3. Storage

Examples:

SSD
HDD

Storage is:

Slower
Persistent
Non-volatile

It keeps data even after power is removed.

4. Input Devices

Examples:

keyboard
mouse
microphone
camera
network requests

They bring information into the computer.

5. Output Devices

Examples:

monitor
printer
speakers
network responses

They present results.

The Most Important Mental Model So Far

                    SSD
                    ↓
                    RAM
                    ↓
                    CPU Registers
                    ↓
                    CPU Computation
                    ↓
                    RAM
                    ↓
                    Output

You will use this model throughout your AI career.

Example: Running Python

You write:

print("Hello")

The flow is:

                Python file on SSD
                     ↓
                Loaded into RAM
                     ↓
                CPU executes instructions
                     ↓
                Output on screen

This simple model explains an enormous amount of computing.

Why This Matters for AI

Suppose we train a neural network:

model.train()

The process becomes:

                Dataset on SSD
                      ↓
                Loaded into RAM
                      ↓
                Moved to GPU memory
                      ↓
                GPU computations
                      ↓
                Results returned

Understanding where data lives and moves is crucial for AI engineering.



## Key Insight

Hardware provides the capability to compute.

Software provides the instructions that determine what the computer does.

The same hardware can perform completely different tasks by running different software.