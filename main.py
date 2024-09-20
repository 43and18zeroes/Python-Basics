try:
    datei = open("nicht_existierende_datei.txt", "r")
    inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden.")
except Exception as e:
    print("Ein unerwarteter Fehler ist aufgetreten:", e)
finally:
    datei.close()  # Wird immer ausgeführt, auch bei Fehlern