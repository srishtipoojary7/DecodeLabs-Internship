# Artificial Intelligence Project 2 – Data Classification Using AI

## Objective
Build a basic supervised-learning classification model using a small dataset.

## Dataset
The project uses the standard **Iris dataset** available directly through scikit-learn. It contains:
- 150 samples
- 4 numerical features
- 3 flower classes: setosa, versicolor, virginica

## Required pipeline
1. Load and understand the dataset.
2. Split the data into training and testing sets using an 80/20 split.
3. Standardize the features using StandardScaler.
4. Train a K-Nearest Neighbors (KNN) classifier.
5. Use K=5 as the main model.
6. Predict the test data.
7. Evaluate using accuracy, confusion matrix and F1-score.
8. Test one new flower measurement.

## How to run on Windows PowerShell

```powershell
cd "PATH_TO_THIS_FOLDER"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python project2_iris_knn.py
```

If PowerShell blocks activation, run the Python file directly after installing packages:

```powershell
python project2_iris_knn.py
```

## Optional K tuning
Run:

```powershell
python tune_k.py
```

This compares K values from 1 to 15. The main project keeps K=5 to match the prescribed workflow.

## Files
- `project2_iris_knn.py` – complete project implementation
- `tune_k.py` – optional K-value comparison
- `requirements.txt` – required Python libraries
- `README.md` – setup and explanation
- `Project_2_Report.md` – submission-ready report content
- `confusion_matrix.png` – generated after running the main program
