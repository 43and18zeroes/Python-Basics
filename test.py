from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

print(are_anagrams("listen", "silent"))


print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

print("Florian".zfill(10)) # 000Florian

print("Florian".upper()) # FLORIAN

print("Florian".lower()) # florian

print("florian".capitalize()) # Florian

print("florian".isupper()) # False

print("florian".islower()) # True

print("1234".isnumeric()) # True

print("florian".isalpha()) # True

print("Florian;Pamela;Mia;Tokage".split(';')) # ['Florian', 'Pamela', 'Mia', 'Tokage']

print("Florian;Pamela;Mia;Tokage".split(';')) # ['Florian', 'Pamela', 'Mia', 'Tokage']

print("Florian\nPamela\nMia\nTokage") # Florian
# Pamela
# Mia
# Tokage

print("Florian\nPamela\nMia\nTokage".splitlines()) # ['Florian', 'Pamela', 'Mia', 'Tokage']

print("Florian\nPamela\nMia\nTokage".split("\n")) # ['Florian', 'Pamela', 'Mia', 'Tokage']

print("   Florian   ".strip()) # Florian (like trim() in JS)

print("   Florian   D   ".replace(" ", "")) # FlorianD

print("   Florian   D   ".replace("o", ".")) #    Fl.rian   D

print("Florian D".replace("Florian", "Pamela")) # Pamela D

print("Florian".replace("ia", "uo")) # Floruon

print("Wasserfall".count("s")) # 2

print("Wasserfall".index("a")) # 1

