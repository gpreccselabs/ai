
from sympy import symbols, Eq, solve

# Define the symbols/variables
x, y = symbols('x y')

# Get user input for x_val and y_val
x_val = float(input("Enter the value for x+y=z1: "))
y_val = float(input("Enter the value for x-y=z2: "))

# Define equations using user input values
eq1 = Eq(x + y, x_val)
eq2 = Eq(x - y, y_val)

# Solve the system of equations
solution = solve((eq1, eq2), (x, y))

# Print the solution
print("Solution:")
print(f"x = {solution[x]}, y = {solution[y]}")
