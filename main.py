def count_words_in_file(filename):
  word_count = 0
  with open(filename, 'r') as file:
    for line in file:
      words = line.split()
      word_count += len(words)
  return word_count

# Beispiel-Datei
filename = "my_text_file.txt"
total_words = count_words_in_file(filename)
print("Anzahl der Wörter:", total_words)