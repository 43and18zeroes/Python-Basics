import random

def shuffle_list(items):
    random.shuffle(items)
    return items

fruits = ['Apfel', 'Banane', 'Kirsche']
print(shuffle_list(fruits))  # Zufällig gemischte Liste
