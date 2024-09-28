import random

def random_passphrase(words, word_count):
    return ' '.join(random.choices(words, k=word_count))

word_list = ['Hund', 'Katze', 'Maus', 'Auto', 'Baum', 'Haus']
print(random_passphrase(word_list, 4))  # Zufällige Passphrase mit 4 Wörtern
