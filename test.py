def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    max_len = 0
    ending_index = m
    table = [[0] * (n + 1) for i in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_len:
                    max_len = table[i][j]
                    ending_index = i
    
    return str1[ending_index - max_len: ending_index]

print(longest_common_substring("substringfinder", "stringfindertest"))

name = "Florian"
print(name[:]) # Florian
