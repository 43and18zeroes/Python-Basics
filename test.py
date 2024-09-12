from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

print(are_anagrams("listen", "silent"))


print(dir(str))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


passwort1 = "abc123"
passwort2 = "Pass Wort"
passwort3 = "u1tr4g3h31m "

print(passwort1.upper()) # ABC123
print(passwort2.lower()) # pass wort
print(passwort3.islower()) # True
print(passwort2.isupper()) # False
print(passwort1.zfill(8)) # 00abc123
print(passwort2.strip()) # Pass Wort
print(len(passwort3)) # 12
print(passwort1.isalpha()) # False
print(passwort1[3:].isnumeric()) # True
print("a;b;c;d;e".split(';')) # [a, b, c, d, e]
print("01.23.45.67.89".split(';')) # Error
print(passwort2.replace("Pass",'.')) # . Wort
print(passwort3.count('3')) # 2
print(passwort2.count('s')) # 2
print(passwort3.find(2+2)) # 4
print(passwort1.index("4")) # -1