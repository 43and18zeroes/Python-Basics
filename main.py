def transponieren(matrix):
    """Transponiert eine Matrix (2D-Array)."""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]