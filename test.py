def string_compression(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))  # Add last character
    return ''.join(compressed)

print(string_compression("aaabbccddddeee"))



a = "Hallo"
b = " "
c = "Python"
d = "!"

print(d * 3) # !!!