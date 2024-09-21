class Meta(type):
    def __new__(mcs, name, bases, attrs):
        print(f"Erstelle Klasse: {name}")
        return super().__new__(mcs, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass