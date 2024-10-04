def word_count(filename):
    with open(filename, 'r') as f:
        words = f.read().split()
    return len(words)

filename = 'my_text.txt'
count = word_count(filename)
print("Die Datei", filename, "enthält", count, "Wörter.")