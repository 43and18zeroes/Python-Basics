def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example
gcd(48, 18)  # Output: 6
