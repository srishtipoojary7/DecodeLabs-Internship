# ARTIFICIAL INTELLIGENCE – PROJECT 2
## DATA CLASSIFICATION USING AI

### 1. Title
**Data Classification Using Artificial Intelligence – Iris Flower Classification Using K-Nearest Neighbors**

### 2. Abstract
This project demonstrates a basic supervised machine-learning classification pipeline. The Iris dataset is loaded, divided into training and testing subsets, standardized, and used to train a K-Nearest Neighbors (KNN) classifier. The trained model predicts the class of unseen test samples. Model performance is evaluated using accuracy, confusion matrix and F1-score. The implementation uses Python and scikit-learn.

### 3. Objective
The objectives are:
- Load and understand a small dataset.
- Prepare numerical features for machine learning.
- Split the dataset into training and testing sets.
- Apply a simple classification algorithm.
- Train and test the model.
- Validate the output using evaluation metrics.

### 4. Dataset
The Iris dataset contains measurements of iris flowers. Each sample has four numerical features:
1. Sepal length
2. Sepal width
3. Petal length
4. Petal width

The target has three classes:
- Setosa
- Versicolor
- Virginica

There are 150 samples in total, with 50 samples in each class.

### 5. Methodology
The complete pipeline is:

**Input dataset → 80/20 train-test split → feature scaling → KNN training → prediction → evaluation**

#### 5.1 Train-test split
80% of the data is used for training and 20% for testing. Stratification is used so that the class distribution is maintained in both subsets.

#### 5.2 Feature scaling
KNN is distance-based. Therefore, the four numerical features are standardized using StandardScaler. The scaler is fitted only on the training data and then applied to both training and testing data.

#### 5.3 Algorithm: K-Nearest Neighbors
KNN classifies a new sample by looking at the K closest training samples. The majority class among those neighbors becomes the prediction.

The main model uses **K = 5**.

#### 5.4 Training
The model is created using:
`KNeighborsClassifier(n_neighbors=5)`

It is then trained using:
`model.fit(X_train_scaled, y_train)`

#### 5.5 Prediction
Predictions are generated using:
`model.predict(X_test_scaled)`

### 6. Evaluation
The project evaluates the classifier using:
- **Accuracy:** proportion of correctly classified test samples.
- **Confusion matrix:** shows correct and incorrect predictions for each class.
- **F1-score:** combines precision and recall and is useful for assessing class-wise performance.

### 7. Implementation
The implementation is provided in `project2_iris_knn.py`. It automatically:
1. Loads Iris.
2. Prints dataset information.
3. Splits the dataset 80/20.
4. Standardizes features.
5. Trains KNN with K=5.
6. Predicts test samples.
7. Prints accuracy, F1-score, classification report and confusion matrix.
8. Saves a confusion-matrix image.
9. Predicts a sample flower.

### 8. Expected Result
Because the Iris dataset is small and well separated, KNN should achieve high test accuracy. The exact accuracy depends on the train-test split and preprocessing. The included program prints the exact result obtained when it is executed rather than hard-coding a result.

### 9. Advantages
- Simple and easy to understand.
- No complicated training equation is required.
- Works well on small datasets.
- Easy to implement with scikit-learn.
- Useful as an introduction to supervised learning.

### 10. Limitations
- Prediction can become slower as the training dataset grows.
- KNN is sensitive to feature scale, so standardization is important.
- The choice of K affects performance.
- It can be affected by irrelevant or noisy features.

### 11. Conclusion
This project demonstrates the fundamental supervised-learning workflow required for a basic classification system. The Iris dataset is prepared, split into training and testing data, standardized, and classified using KNN. The resulting predictions are validated with accuracy, confusion matrix and F1-score. The project provides a practical foundation for understanding how an AI model learns from labelled data and predicts classes for unseen inputs.

### 12. Future Scope
The same pipeline can be extended by:
- Comparing KNN with Logistic Regression, Decision Tree and SVM.
- Using cross-validation for more reliable K selection.
- Applying the model to a larger real-world dataset.
- Building a simple graphical interface for user input.
- Saving and loading the trained model.

### 13. Viva Questions and Answers

**Q1. What type of learning is used?**  
Supervised learning, because the training data contains known class labels.

**Q2. Which algorithm is used?**  
K-Nearest Neighbors (KNN).

**Q3. Why is scaling used?**  
KNN uses distances. Scaling prevents features with larger numerical ranges from dominating the distance calculation.

**Q4. What is K?**  
K is the number of nearest training samples considered when deciding the class of a new sample.

**Q5. Why use K=5?**  
It is the main K value specified for this implementation and provides a reasonable neighborhood size for the small Iris dataset.

**Q6. What is the purpose of the test set?**  
It evaluates how well the trained model performs on data it did not use during training.

**Q7. What is a confusion matrix?**  
A table showing correct and incorrect predictions for each class.

**Q8. What is F1-score?**  
F1-score is the harmonic mean of precision and recall.

**Q9. What are the Iris classes?**  
Setosa, Versicolor and Virginica.

**Q10. Is KNN a supervised algorithm?**  
Yes. It uses labelled training examples.
