"""Optional K tuning for the Iris KNN model."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.20, random_state=42, stratify=iris.target
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("K\tAccuracy")
best_k, best_acc = None, -1

for k in range(1, 16):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"{k}\t{acc:.4f}")
    if acc > best_acc:
        best_k, best_acc = k, acc

print(f"\nBest K on this fixed split: {best_k}")
print(f"Accuracy: {best_acc:.4f}")
