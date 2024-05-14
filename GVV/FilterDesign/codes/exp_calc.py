from sympy import symbols, simplify

# Define symbolic variable s
s = symbols('s')

# Constants
omega0_val = 0.3973
B_val = 0.09113

# Define s_L in terms of s, omega0, and B
s_L = (s**2 + omega0_val**2) / (B_val * s)

# Given roots
s1 = -0.3913 - 0.4156j
s2 = -0.3913 + 0.4156j
s3 = -0.1621 + 1.0033j
s8 = -0.1621 - 1.0033j


# Define the given polynomial expression
polynomial_expr = 0.3125 / ((s_L - s1) * (s_L - s2) * (s_L - s3) * (s_L - s8))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
