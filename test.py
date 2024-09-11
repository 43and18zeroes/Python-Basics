print(bool(0.1)) # True
print(bool(-0.1)) # True
print(bool("")) # False

print(int("1.5"))

print(int(float("1.5")))

int(42.5) # 42
float(-1) # -1.0
str(0.5) # "0.5"
bool(0.001) # True
str("False") # 'False'
int(False) # 0
float("10") # 10.0
bool('0') # False
int("False") # Fehlermeldung weil String zu Int
float("True") # Fehlermeldung weil String zu Float

print(
    """
    _____    __________________ .___.___  ___________            __   
    /  _  \  /   _____/\_   ___ \|   |   | \_   _____/___   _____/  |_ 
    /  /_\  \ \_____  \ /    \  \/|   |   |  |    __)/  _ \ /    \   __\
    /    |    \/        \\     \___|   |   |  |     \(  <_> )   |  \  |  
    \____|__  /_______  / \______  /___|___|  \___  / \____/|___|  /__|  
            \/        \/         \/               \/             \/      
    """
)