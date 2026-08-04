## Lesson 1 — Why OOP?

Before learning class, answer this:

## Why was OOP invented?

If functions were enough, why create classes?

The Problem with Procedural Programming

Imagine you're building PocketFlow procedurally.

def create_user():
    ...

def create_schedule():
    ...

def create_transfer():
    ...

def pause_schedule():
    ...

def cancel_schedule():
    ...

def update_schedule():
    ...

def execute_schedule():
    ...

def retry_transfer():
    ...

def fail_transfer():
    ...

def send_notification():
    ...

Looks fine.

Now fast forward one year.

payments.py
users.py
notifications.py
schedules.py
transfers.py
providers.py

400+ functions

Question:

Which functions belong together?

Python doesn't know.

Real Systems Have Relationships

In PocketFlow:

A schedule has:

amount
frequency
status
next_execution
authorization
recipient

And behaviors:

pause()
resume()
cancel()
execute()

Notice something.

The data and the behavior naturally belong together.

Procedural Style
schedule = {
    "amount": 50000,
    "status": "ACTIVE"
}

pause_schedule(schedule)
resume_schedule(schedule)
cancel_schedule(schedule)

The data lives here.

The behavior lives somewhere else.

OOP Style
schedule = Schedule(
    amount=50_000
)

schedule.pause()
schedule.resume()
schedule.cancel()

Now:

Schedule
├── Data
└── Behavior

They're grouped together.

Why This Matters

Suppose tomorrow you add:

status = "PAUSED"

Where should validation happen?

Procedural code:

Maybe here.

Maybe there.

Maybe forgotten entirely.

OOP:

schedule.pause()

The object owns the rules.

Real Example — Bank Account

Procedural:

deposit(account, amount)
withdraw(account, amount)
freeze(account)

OOP:

account.deposit(amount)
account.withdraw(amount)
account.freeze()

Which reads closer to English?

The second.

Another Example — PyTorch

When you train a model:

model.forward(x)
model.train()
model.eval()
model.parameters()
model.to(device)

Imagine if PyTorch were procedural:

forward(model, x)
train(model)
eval(model)
parameters(model)
move_to_device(model)

Technically possible.

Much harder to organize across thousands of classes.

Another Example — FastAPI

Instead of:

start_server(app)
add_route(app)
mount(app)

FastAPI uses:

app.add_api_route(...)
app.mount(...)
app.include_router(...)

The application object manages itself.

Another Example — SQLAlchemy

Instead of:

commit(session)
rollback(session)
execute(session)

You write:

session.commit()
session.rollback()
session.execute(...)

Again:

Behavior belongs to the object.

Another Example — File Objects

Python itself uses OOP.

file = open("data.txt")

Then:

file.read()

file.write(...)

file.close()

Not:

read(file)
write(file)
close(file)
The Core Idea

Objects combine:

State
+
Behavior

State:

balance

Behavior:

deposit()
withdraw()

Without behavior,

it's just data.

Without state,

it's just a function.

OOP is About Modeling

Think about your domain.

PocketFlow has:

User
Recipient
Schedule
Transfer
Authorization
Provider

Each one:

has data
performs actions

Those are natural objects.

When NOT to Use OOP

Not everything needs a class.

Bad:

class Math:

    def add(self, a, b):
        return a + b

Better:

def add(a, b):
    return a + b

No state.

No object.

No class needed.

Another bad example:

class StringUtils:

    @staticmethod
    def capitalize(text):
        ...

Usually better:

def capitalize(text):
    ...

Or use Python's built-in methods:

text.capitalize()

Classes are valuable when they manage state over time, not just group unrelated functions.

Senior Engineering Guideline

Ask yourself:

Does this thing have identity and state that changes over time?

If yes, a class is often appropriate.

Examples:

User ✅
PaymentSchedule ✅
BankAccount ✅
NeuralNetwork ✅

If not:

calculate_tax() ❌
parse_json() ❌
hash_password() ❌

A function is usually enough.

PocketFlow Example

Good objects:

Schedule
Transfer
Authorization
Recipient
Provider
WebhookEvent

Good functions:

generate_signature()
parse_csv()
format_currency()
calculate_next_run()

Notice the difference.

Objects represent entities.

Functions represent operations.

Interview Question

Why use OOP instead of procedural programming?

A good answer:

OOP groups related state and behavior into cohesive units, making large systems easier to organize, maintain, and extend. It models domain entities naturally and localizes business rules to the objects that own the data.



