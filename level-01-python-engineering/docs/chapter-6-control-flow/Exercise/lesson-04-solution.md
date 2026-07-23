
Exercises
Exercise 1 — Mental Model

In your own words:

Why isn't match simply another name for if?
What kind of problems is match especially good at solving?
What does case _: represent?
Exercise 2 — Predict the Output

Without running the code, determine the output and explain why.

command = "predict"

match command:
    case "train":
        print("Training")
    case "predict":
        print("Predicting")
    case _:
        print("Unknown")
status = 500

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Other Error")
Exercise 3 — Write Code

Write a program that checks a payment status using match.

Possible statuses:

"PENDING" → "Waiting for processing"
"PROCESSING" → "Transfer in progress"
"COMPLETED" → "Transfer successful"
"FAILED" → "Retry required"
Any other value → "Unknown status"
Exercise 4 — AI Engineering Thinking

Suppose you're building an LLM API that supports these request types:

"chat"
"embedding"
"image"
"speech"

Write a match statement that dispatches each request to a different print statement.

Then answer:

Why is match cleaner than a long if/elif chain in this situation?
As the API grows from 4 request types to 40, what maintainability advantages does match provide?