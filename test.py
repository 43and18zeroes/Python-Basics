def harmonic_mean(numbers):
    return len(numbers) / sum(1 / num for num in numbers)

# Example
harmonic_mean([1, 2, 4])  # Output: 1.7142857142857142



print(True and False and True or False) # False

print(not False or not True) # True (erst die nots, dann das or)

print(True and (False or not False)) # True

print(not (not False ^ True or not False)) # False, erst die nots, dann XOR, dann or, dann Klammer

print(True and False ^ True and False) # False









