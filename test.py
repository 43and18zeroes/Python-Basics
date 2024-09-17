level = 0

def level_up():
    global level
    level += 5
    print(f"Dein Level ist: {level}") # 5
    
level_up()
print(level) # 5