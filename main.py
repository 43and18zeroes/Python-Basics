import random
import string

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

print(random_string(8))  # Zufällige Zeichenkette mit 8 Zeichen
