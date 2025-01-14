#How to define a funstion:
# 1. Use the keyword def.
# 2. Give your function a name.
# 3. Add parantheses ()--- you can include inputs (parameters) here.
# 4. End the line with a colon:. 
# 5. Indent the body of the function (this is the code that runs when the finction is called)

# Example:
def greet():
    print("Hello, world!")
greet()

def say_hello():
    print("Hi, there!")
say_hello()

# Step 2 Functions with Parameters
#Example
name = "Alice"

print(f"Hello, {name}!")  # Output: Hello, Alice!


def introduce(name):
    print(f"Nice to meet you, {name}!")
introduce("Leroy")

# 3 Step Example 
def introduce (first_name, last_name):
    print(f"Hello, {first_name} {last_name}! Welcome!")
introduce("Leroy", "Tillman")

greet(), introduce("Leroy", "Tillman") 