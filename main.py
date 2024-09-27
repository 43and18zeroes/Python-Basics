from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Laden des Iris-Datensatzes
iris = load_iris()
X = iris.data
y = iris.target

# Aufteilung in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Erstellen und Trainieren eines KNN-Modells
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Vorhersage für neue Daten
new_data = [[3, 5, 4, 2]]
predicted = knn.predict(new_data)
print(predicted)