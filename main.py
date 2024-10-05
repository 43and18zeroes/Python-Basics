def produkt(array1, array2):
    """Berechnet das elementweise Produkt zweier Arrays gleicher Länge."""
    if len(array1) != len(array2):
        raise ValueError("Arrays müssen dieselbe Länge haben")
    return [x*y for x, y in zip(array1, array2)]