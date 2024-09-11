def count_vowels_consonants(s):
    vowels = "aeiou"
    s = s.lower()
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

print(count_vowels_consonants("Hello World"))



a = "Buchhaltung"
b = "Python ist toll!"

print(a[5]) # a
print(b[-1]) # !
print(a[:4]) # Buch
print(b[11:16]) # toll!
print(a[-100:100]) # Buchhaltung
print(a[-5]) # l
print(a[-12]) # Fehler
print(a[4:8]) # halt