def teilnehmer(**daten):
    vorname = daten.get("vorname")
    nachname = daten.get("nachname")
    alter = daten.get("alter", 18)
    print(f"{vorname} {nachname}; {alter}") # Florian Dalwigk, 28
    
teilnehmer(vorname="Florian", nachname="Dalwigk", alter=28)