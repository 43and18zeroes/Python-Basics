def harmonic_mean(numbers):
    return len(numbers) / sum(1 / num for num in numbers)

# Example
harmonic_mean([1, 2, 4])  # Output: 1.7142857142857142


print(2 < 3 and 3 == 5) # False

print(2 < 3 or 3 == 5) # True

print((2 < 3) ^ (3 != 5)) # False (weil XOR)

print(True or 2 < 3 and False) # True (< als erstes, dann and weil Python)

print(True and 2 < 3 and False) # False

print(not (2 < 3)) # False

print(1 ^ False) # 1

print(2 - 2 ^ False) # 0

