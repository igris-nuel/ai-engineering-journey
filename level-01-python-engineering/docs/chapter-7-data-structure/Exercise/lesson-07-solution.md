# Exercises
## Exercise 1 — Mental Model

In your own words:

Why are sets unordered?
Why can't you use indexing with a set?
Why do sets automatically remove duplicates?
Why are sets usually much faster than lists for membership testing?

## Exercise 2 — Professional Code

Given

    emails = [
        "alice@test.com",
        "bob@test.com",
        "alice@test.com",
        "carol@test.com",
    ]

Write code to:

Remove duplicate email addresses.
Add "dave@test.com".
Remove "bob@test.com" safely (without raising an error if it doesn't exist).
Print every unique email.

## Exercise 3 — Set Operations

Given

    frontend = {
        "Alice",
        "Bob",
        "Charlie",
    }

    backend = {
        "Charlie",
        "David",
        "Alice",
    }

Write code to compute:

Everyone on either team.

Engineers on both teams.

Engineers only on the frontend team.

Engineers on exactly one team.

## Exercise 4 — AI Engineering

A recommendation system has processed 10 million user IDs.

Every new request needs to answer:

"Has this user been seen before?"

Without running code, explain:

Why is a set a much better choice than a list?

What would happen to performance if a list were used instead?

Why is uniqueness important in this scenario?

Name two other AI or data engineering problems where a set is the ideal data structure.