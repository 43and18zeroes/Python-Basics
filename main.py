class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'MyClass':
            namespace['my_method'] = lambda self: print('Hello')
        return super().__new__(mcs, name, bases, namespace)

class MyClass(metaclass=Meta):
    pass