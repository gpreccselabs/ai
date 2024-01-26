
from sympy import symbols, Eq, solve
x, y = symbols('x y')
x_val = float(input("Enter the value for x+y=z1: "))
y_val = float(input("Enter the value for x-y=z2: "))
eq1 = Eq(x + y, x_val)
eq2 = Eq(x - y, y_val)
solution = solve((eq1, eq2), (x, y))
print("Solution:")
print(f"x = {solution[x]}, y = {solution[y]}")
