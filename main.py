try:
    try:
        # Innerer try-Block
        x = 10 / 0
    except ZeroDivisionError:
        print("Division durch Null im inneren Block.")
except Exception as e:
    print("Äußerer Fehler:", e)