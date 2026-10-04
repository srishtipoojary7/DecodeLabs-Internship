"""
Artificial Intelligence - Project 2
Data Classification Using AI
Dataset: Iris
Algorithm: K-Nearest Neighbors (KNN)
Pipeline: 80/20 train-test split -> StandardScaler -> KNN -> evaluation
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    f1_score,
)

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("Dataset: Iris")
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])
print("Classes:", list(iris.target_names))
print("Class counts:", {name: int((y == i).sum()) for i, name in enumerate(iris.target_names)})

# 2. Split into training and testing data (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 3. Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Create and train the KNN classifier with K=5
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# 5. Predict the test set
y_pred = model.predict(X_test_scaled)

# 6. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")
cm = confusion_matrix(y_test, y_pred)

print("\n--- MODEL RESULTS ---")
print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
print(f"Weighted F1-score: {f1:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
print("Confusion Matrix:")
print(cm)

# 7. Validate on one new sample
new_flower = [[5.1, 3.5, 1.4, 0.2]]
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)[0]
print("\nNew sample prediction:", iris.target_names[prediction])

# 8. Display and save confusion matrix
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)
disp.plot()
plt.title("KNN Confusion Matrix - Iris Dataset")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=200)
plt.show()
