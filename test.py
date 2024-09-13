def harmonic_mean(numbers):
    return len(numbers) / sum(1 / num for num in numbers)

# Example
harmonic_mean([1, 2, 4])  # Output: 1.7142857142857142




print(2 < 3 and not 2 > 5) # True

print(not True ^ False or 3 == 2 + 1) # True

print(not not not 2 % 5 == 7 % 5) # False, 2 % 5 = 2

print(True and False ^ True and False) # False

print(True ^ False ^ 0 ^ 1 ^ (2 > 3)) # 0
