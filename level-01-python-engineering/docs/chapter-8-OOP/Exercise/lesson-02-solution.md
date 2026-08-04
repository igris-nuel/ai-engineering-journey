Exercises
Exercise 1

Without running the code:

class User:
    pass

u1 = User()
u2 = User()

Explain:

What objects exist after execution?
Which names point to which objects?
Which object created u1?
Are u1 and u2 the same object?
Exercise 2

Explain why this is valid:

Alias = User

obj = Alias()

using your understanding of names and objects.

Exercise 3

A teammate says:

"The class is copied every time you create an object."

Critique that statement.

Explain what actually happens in memory when:

User()

is executed.

Exercise 4 (AI Engineering)

Consider:

model = nn.Linear(768, 512)

Explain:

What is the class?
What is the instance?
Why can you create multiple Linear objects?
Why should each object have independent state (such as weights and biases)?