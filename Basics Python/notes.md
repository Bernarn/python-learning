🧩 1. Variables

Used to store data in memory for later use.

Example:

name = "Bernard"
age = 22
height = 1.78


You can change (reassign) variables at any time.

Variable names should be descriptive and lowercase (e.g., total_cost, not TC).

🔁 2. Loops

Loops help you repeat actions without writing the same code multiple times.

➤ For Loop

Used when you know how many times to repeat:

for i in range(5):
    print("Hello")

➤ While Loop

Used when you repeat until a condition changes:

count = 0
while count < 5:
    print(count)
    count += 1

⚖️ 3. Conditional Statements (if, elif, else)

Used to make decisions in code.

age = 18
if age >= 18:
    print("You are an adult.")
elif age > 13:
    print("You are a teenager.")
else:
    print("You are a child.")


Conditions use comparison operators: ==, !=, <, >, <=, >=.

Logical operators combine conditions: and, or, not.

🧠 4. Functions

Functions are reusable blocks of code that perform specific tasks.

def greet(name):
    print(f"Hello, {name}!")

greet("Bernard")


def defines a function.

Functions can take parameters (inputs) and return outputs:

def add(a, b):
    return a + b

📦 5. Lists

Lists hold multiple items in one variable.

movies = ["Avatar", "Titanic", "Inception"]
print(movies[0])  # first item


You can add items: movies.append("Avengers")

Loop through items:

for movie in movies:
    print(movie)


Analyze lists:

len(movies)   # number of items
sum(numbers)  # total
max(numbers)  # largest value

💡 Key Takeaways

Variables store data.

Loops repeat tasks.

Conditionals make decisions.

Functions organize reusable logic.

Lists manage multiple data items and support analysis.