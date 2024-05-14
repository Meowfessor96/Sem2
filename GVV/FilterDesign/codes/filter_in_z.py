import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 2.155e-5 * s**4 / (s**8 + 0.1008 * s**7 + 0.644 * s**6 + 0.0484 * s**5 + 0.1534 * s**4 + 0.00763 * s**3 + 0.016 * s**2 + 0.0004 * s + 0.0006)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)

