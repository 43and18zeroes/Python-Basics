telefonbuch = {
    "Junus" : "0123456789"
}

print(telefonbuch.get("Junus")) # 0123456789

print(telefonbuch["Junus"]) # 0123456789

print(telefonbuch["Florian"]) # KeyError

print(telefonbuch.get("Florian")) # None (kein Error)