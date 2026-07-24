# Exercises
## Exercise 1 — Mental Model

In your own words:

What does the else block of a loop actually mean?
Why doesn't break allow the else block to execute?
Why does continue still allow the else block to execute?

## Exercise 2 — Predict the Output

Without running the code, determine the output and explain why.

A
    for x in [1, 2, 3]:
        print(x)
    else:
        print("Finished")
B
    for x in [1, 2, 3]:

        if x == 2:
            break

        print(x)

    else:
        print("Finished")
C
    count = 1

    while count < 4:
        print(count)
        count += 1
    else:
        print("Done")
D
    count = 1

    while count < 4:

        if count == 2:
            break

        print(count)
        count += 1

    else:
        print("Done")

Explain why the behavior differs from Exercise C.

## Exercise 3 — Write Code
Program 1 — Search

Create a list:

    students = ["Grace", "John", "Mary", "David"]

Search for "Mary".

If found, print:
Found Mary

and stop searching with break.

If the loop finishes without finding "Mary", print:
Student not found

using the loop's else.

Program 2 — Retry Login

Write a loop that attempts a login 3 times.

Assume a function:

login_successful(attempt)

returns True only on the third attempt.

Use:

    break when login succeeds.
    Loop else to print:
    Login failed

only if all attempts fail.

## Exercise 4 — AI Engineering Thinking

You're writing an AI inference service that searches through a list of model servers to find one that is available.

Conceptually explain:

    Why for/else is a natural fit for this problem.
    What break represents in this context.
    What the loop's else represents.
    Why this design is cleaner than maintaining a separate server_found boolean flag.