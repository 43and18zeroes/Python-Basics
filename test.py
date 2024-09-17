def teilnehmer(**daten):
    vorname = daten.get("vorname")
    nachname = daten.get("nachname")
    print(f"{vorname} {nachname}") # Florian Dalwigk
    
teilnehmer(vorname="Florian", nachname="Dalwigk")