import cmath

def solve_quadratic(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2

# Example
solve_quadratic(1, -3, 2)  # Output: (2.0, 1.0)


print(2 < 3 and 3 == 5) # False

print(2 < 3 or 3 == 5) # True

print((2 < 3) ^ (3 != 5)) # False (weil XOR)

print(True or 2 < 3 and False) # True (< als erstes, dann and weil Python)

print(True and 2 < 3 and False) # False







