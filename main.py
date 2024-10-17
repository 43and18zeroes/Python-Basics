def forward_kwargs(**kwargs):
    another_function(**kwargs)

def another_function(x, y, z):
    print(f"x={x}, y={y}, z={z}")

forward_kwargs(x=1, y=2, z=3)