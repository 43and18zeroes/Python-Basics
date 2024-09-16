passwort_hashes = {
    "abc123" : "e4u57913dfkgjst8kj45h234jkh2",
    "1337" : "e4u57913dfkgjst8kj45h234jkh2",
    "love" : "e4u57913dfkgjst8kj45h234jkh2"
}

print(passwort_hashes.get("ultrageheim", "456432185498768546513245679874654")) # 456432185498768546513245679874654, Default Wert

passwort_hashes["abc123"] = "overwrite"
print(passwort_hashes) # {'abc123': 'overwrite', '1337': 'e4u57913dfkgjst8kj45h234jkh2', 'love': 'e4u57913dfkgjst8kj45h234jkh2'}

passwort_hashes["Eva"] = "1234"
print(passwort_hashes) # {'abc123': 'overwrite', '1337': 'e4u57913dfkgjst8kj45h234jkh2', 'love': 'e4u57913dfkgjst8kj45h234jkh2', 'Eva': '1234'}

passwort_hashes.update({"1337" : "4321"})
print(passwort_hashes) # {'abc123': 'overwrite', '1337': '4321', 'love': 'e4u57913dfkgjst8kj45h234jkh2', 'Eva': '1234'}

del passwort_hashes["love"]
print(passwort_hashes) # {'abc123': 'overwrite', '1337': '4321', 'Eva': '1234'}

del passwort_hashes["Max"] # nichts passiert, es wird kein Fehler geworfen

kopie = passwort_hashes.copy()
print(kopie) # {'abc123': 'overwrite', '1337': '4321', 'Eva': '1234'}

print(passwort_hashes.keys()) # dict_keys(['abc123', '1337', 'Eva'])

print(type(passwort_hashes.keys())) # <class 'dict_keys'>

print(type(list(passwort_hashes.keys()))) # <class 'list'>

print(passwort_hashes.values()) # dict_values(['overwrite', '4321', '1234'])

print(type(passwort_hashes.values())) # <class 'dict_values'>

print(type(list(passwort_hashes.values()))) # <class 'list'>



