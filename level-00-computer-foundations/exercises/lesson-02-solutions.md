## Exercise 1

In your own words:

What is the difference between hardware and software?


## Exercise 2

Classify each:

hardware : CPU SSD Keyboard Monitor

software : Python Interpreter Chrome RAM Linux GPU VS Code



## Exercise 3

Explain what happens when you run:
python app.py
using this sequence:

SSD → RAM → CPU → Output

When I run `python app.py`, the operating system loads the Python interpreter and my Python file from the SSD into RAM. The CPU then begins executing instructions from the interpreter. Whenever the CPU needs data, it loads it into registers, performs computations, and stores the results back in memory. Finally, if the program prints something, the result is sent to an output device such as the terminal.


Exercise 4

Why can't a computer run software if it has no RAM?
A computer cannot run software without RAM because running programs and their data need a place to live while they are executing. The CPU cannot execute a program directly from long-term storage like an SSD, so the operating system loads the program into RAM first.

Exercise 5

Why can't a computer run software if it has no CPU?
A computer cannot run software without a CPU because the CPU is the component that fetches, decodes, and executes instructions. Without a CPU, instructions can be stored in memory, but nothing can actually perform the computations.