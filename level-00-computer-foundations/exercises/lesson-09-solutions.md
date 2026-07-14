Exercises
Exercise 1

In your own words:

What is machine language?
Machine language is the lowest-level software language, consisting entirely of raw binary numbers (1s and 0s). It is the only language that a computer's physical CPU hardware can natively understand, interpret, and execute without any translation


Exercise 2

Why can't a CPU execute Python code directly?
The hardware lacks the physical circuits required to understand words, syntax, or text characters directly.
electronic switches only reacts to specific binary electrical signals

Exercise 3

What is an instruction?
Give two examples.

An instruction is a single, fundamental command given to a CPU to perform a primitive operation.

LOAD - Go to a specific memory location, copy the data found there, and place it into a CPU register
Example 2: ADD (Take two numbers currently inside the CPU registers, combine them mathematically, and store the result)

Exercise 4

Why do different CPUs have different instruction sets?
Different CPUs are engineered for entirely different goals, budgets, and physical constraints e.g speed

Exercise 5

Which statement is more accurate?

A.

The CPU executes Python.

B.

The CPU executes machine instructions generated while running Python.

Explain why.
B is more accurate, the cpu only understands machine code and not python. python is being translated into machine code by the python interpreter

Exercise 6 (Thinking)

Imagine you invent a brand-new CPU with a completely new instruction set.

What problem would software developers face?
Software developers would face a massive software compatibility crisis. Because the instruction set is completely new, every existing operating system (like Windows, macOS, or Linux) and every existing application or game would fail to run.

Exercise 7 (Challenge)

Suppose a CPU had only these instructions:

LOAD
STORE
ADD
JUMP

Do you think it would still be possible to build a web browser or train an AI model?

Why or why not?

Yes, it is entirely possible.Why: Even the most complex modern software is just a massive chain of incredibly simple logic.