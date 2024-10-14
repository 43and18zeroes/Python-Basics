import random
import string
länge = 10
zeichen = string.ascii_letters + string.digits
passwort = ''.join(random.choice(zeichen) for _ in range(länge))
print(passwort)