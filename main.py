def sicheres_teilen(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division durch Null"

print(sicheres_teilen(10, 0))