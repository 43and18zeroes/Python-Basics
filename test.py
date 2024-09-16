passwort_hashes = {
    "abc123" : "e4u57913dfkgjst8kj45h234jkh2",
    "1337" : "e4u57913dfkgjst8kj45h234jkh2",
    "love" : "e4u57913dfkgjst8kj45h234jkh2"
}

print(passwort_hashes.get("ultrageheim", "456432185498768546513245679874654")) # 456432185498768546513245679874654, Default Wert

passwort_hashes["abc123"] = "overwrite"
print(passwort_hashes) # {'abc123': 'overwrite', '1337': 'e4u57913dfkgjst8kj45h234jkh2', 'love': 'e4u57913dfkgjst8kj45h234jkh2'}

passwort_hashes["Eva"] = "1234" # {'abc123': 'overwrite', '1337': 'e4u57913dfkgjst8kj45h234jkh2', 'love': 'e4u57913dfkgjst8kj45h234jkh2', 'Eva': '1234'}
print(passwort_hashes)