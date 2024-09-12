from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

print(are_anagrams("listen", "silent"))


result = 2 ** 2.0
print(result)