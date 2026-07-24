# Exercises
## Exercise 1 — Mental Model

In your own words:

What is the conceptual difference between break and continue?
Does break destroy the loop variable or simply stop future iterations?
Why does continue not end the loop?

## Exercise 2 — Predict the Output

Without running the code, determine the output and explain why.

A
    for x in range(6):
        if x == 3:
            break
        print(x)

    print("Done")
B
    for x in range(6):
        if x == 3:
            continue
        print(x)
C
    count = 0

    while True:
        count += 1

        if count == 4:
            break

        print(count)

What is printed?

## Exercise 3 — Write Code
Program 1 — Even Numbers

Write a program that prints the numbers 1 through 10, but skips all even numbers using continue.

Expected output:

1
3
5
7
9
Program 2 — Password Attempts

Create a list:

    passwords = ["1234", "password", "OpenAI2026", "admin"]

Loop through the list.

If the password equals "OpenAI2026":

Print:

Correct password found

Exit the loop using break.

Otherwise print:

Trying: <password>

## Exercise 4 — AI Engineering Thinking

You're training a model over millions of images.

Some images are unreadable, while one image is discovered to be seriously corrupted and indicates that the dataset itself may be damaged.

Conceptually explain:

Why continue is appropriate for unreadable images.

Why break might be appropriate for the corrupted image.

Why stopping early can save hours of GPU time.

How these two keywords help make AI pipelines both efficient and robust.