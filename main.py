def compose(g, f):
    def h(x):
        return g(f(x))
    return h

def f(x): return x * 2
def g(x): return x + 3

composed_func = compose(g, f)
print(composed_func(5))  # Ausgabe: 13