def calculate(**values):
    result = 0
    for value in values.values():
        result += value
    return result

result = calculate(a=10, b=20, c=30)
print(result)