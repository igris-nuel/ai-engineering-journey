# Exercises
## Exercise 1

In your own words:

Why is RAM not completely empty after your computer finishes booting?
RAM is not empty because your Operating System (OS) must be constantly running in the background to keep the computer functional. During the boot process, the OS core files (the kernel), hardware drivers, background system services, and your graphical desktop interface are loaded directly into RAM so the CPU can execute them continuously

## Exercise 2

What is the role of the operating system in managing RAM?
The operating system acts as a strict traffic controller for RAM. It allocates specific, isolated blocks of memory to apps when they open, tracks exactly which bytes of memory are currently in use, and reclaims (wipes) that memory when an application closes so other programs can reuse it.

## Exercise 3

Explain the difference between:

Program
Process
Operating System

Try to relate all three in one explanation.

Think of a restaurant kitchen:The Program is a static recipe book sitting on a shelf (a dormant file on your SSD like python.exe).The Process is an active chef currently cooking that specific recipe in the kitchen (the program alive and running in RAM).The Operating System is the head chef/kitchen manager who owns the restaurant, hands out the ingredients (RAM), assigns the stoves (CPU), and ensures the chefs don't crash into each other or steal each other's tools

## Exercise 4

Suppose you open:

VS Code
Chrome
Spotify
Python

Why doesn't one application accidentally overwrite another application's memory?
Applications cannot overwrite each other because the OS uses a hardware-enforced security feature called Virtual Memory and Page Tables.
## Exercise 5

True or False?

"When a program is running, it executes directly from the SSD."

Explain.
False. A program cannot execute directly from an SSD. While the SSD holds the files permanently, its connection to the CPU is far too slow for real-time processing. The CPU can only execute instructions that have been copied into RAM (or cached in the CPU itself), which operates thousands of times faster than an SSD.
## Exercise 6 (Thinking)

Suppose you have two terminal windows, and both run:

python app.py

Why can both programs run at the same time even though they are executing the same source file?
They can run simultaneously because the OS creates two completely independent processes in RAM. Even though both processes read the exact same text instructions from the single app.py file on the SSD, the OS clones those instructions into two distinct, isolated memory sandboxes. Each process tracks its own variables, line numbers, and state independently
## Exercise 7 (Challenge)

Imagine there were no operating system, only a CPU, RAM, and an SSD.

Describe what would happen when you tried to run two different programs at the same time.

Think carefully about:

Who loads programs into RAM?
Who decides where each program lives?
Who prevents memory corruption?
Who gives CPU time to each program?


Loading Programs: There is no OS to read the files from the SSD. Program A would have to include its own custom hardware code just to talk to the SSD controller, find its own bytes, and dump them into RAM.

Deciding Memory Locations: There is no coordinator to hand out memory slots. If Program A decides to use memory address 1000, and Program B also decides to use address 1000, they will blindly write over each other. Program B will corrupt Program A's data, causing both to instantly crash.

Preventing Corruption: With no OS enforcing hardware memory boundaries, any program can read or write to any part of RAM. A bug in a tiny script could accidentally wipe out your entire system memory.

Allocating CPU Time: A CPU can only run one instruction at a time per core. Without an OS "scheduler" rapidly switching the CPU between Program A and Program B every few milliseconds, whichever program grabs the CPU first will hoard it forever. The second program will never run unless the first one voluntarily terminates or you pull the power plug.
