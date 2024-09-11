from itertools import permutations

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]

print(all_permutations("abc"))



n = len("Florian")
print(n) # 7
print("Florian"[n - 2]) # a

