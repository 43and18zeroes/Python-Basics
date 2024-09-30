MyClass = type('MyClass', (object,), {'attr': 42})

obj = MyClass()
print(obj.attr)
