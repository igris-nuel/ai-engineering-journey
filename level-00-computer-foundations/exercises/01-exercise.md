# Exercises

## Exercise 1

Explain in one paragraph:

What is a computer?
A computer is a programmable electronic machine that receives data as input, stores data and instructions, processes the data by executing instructions, and produces output. What makes a computer special is that it can perform many different tasks simply by changing the program it runs.

##  Exercise 2

Why is a smartphone still considered a computer?

A smartphone is a computer because it performs the same fundamental operations as any other computer. It receives input through the touchscreen, microphone, camera, and network, stores data in memory and storage, processes information using its CPU and GPU, and produces output through the screen, speakers, and other interfaces.

## Exercise 3

Give five examples of:

### Input 
mouse, keyboard, http request, camera
### Storage 
hard-disk, ssd, ram, register
### Processing 
sorting a list
calculating a sum
compressing an image
training a neural network
encrypting a file
Output -printer, monitor, 

Exercise 4

Why do you think binary is more reliable than decimal in electronics?

Binary is more reliable in electronics because physical circuits can easily distinguish between two states, such as low voltage and high voltage. Distinguishing between ten different voltage levels for decimal digits would be much harder and more prone to errors caused by electrical noise.


## Where Does Data Live?

Programs start on storage (SSD).


When executed:

SSD → RAM → CPU Registers → Computation → RAM

Variables primarily live in RAM and are temporarily loaded into CPU registers during computation.



## Program vs Running Program

A Python file on the SSD is just data.

When the file is executed:

1. The operating system creates a process.
2. The program is loaded into RAM.
3. Variables and program state are stored in RAM.
4. The CPU executes instructions.

If the computer loses power:

- RAM is cleared.
- The process disappears.
- Variables are lost.

The file on the SSD remains because storage is non-volatile.