class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Alter muss positiv sein")
        self._age = value

person = Person(30)
print(person.age)  # Ausgabe: 30