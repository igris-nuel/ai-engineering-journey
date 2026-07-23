# Exercises
## Exercise 1 — Mental Model

In your own words:

What question does a while loop ask before every iteration?
Why is a while loop different from a for loop?
What causes a while loop to stop?

## Exercise 2 — Predict the Output

Without running the code, determine the output and explain why.

    count = 3

    while count > 0:
        print(count)
        count -= 1

    print("Finished")

    value = 0

    while value < 3:
        print(value)

Will this program terminate? Why or why not?

    x = 5

    while x > 2:
        print(x)
        x -= 2

    print(x)

## Exercise 3 — Write Code

Program 1

Write a countdown from 10 to 1 using a while loop.

Then print:

Launch!

Program 2

Simulate retrying a network connection.

Start with:

attempt = 1

While the attempt is less than or equal to 3, print:

Attempt 1
Attempt 2
Attempt 3

After the loop, print:

Connection failed

## Exercise 4 — AI Engineering Thinking

Suppose you're building a service that waits for a large language model to finish generating a response.

A junior engineer writes:

while status != "COMPLETED":
    pass

Evaluate this design.

Discuss:

Why it technically works.
Why it wastes CPU resources.
What a production AI system would usually do instead (for example, sleeping briefly between checks or using events/notifications).
Why efficient waiting matters when thousands of inference requests are running simultaneously.