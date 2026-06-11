# Project 2: Data Classification Using AI

import numpy as np

#Iris data, hardcoded small sample)

data = np.array([
    [5.1, 3.5, 1.4, 0.2], [4.9, 3.0, 1.4, 0.2], [5.0, 3.6, 1.4, 0.2],  # setosa
    [4.7, 3.2, 1.3, 0.2], [5.4, 3.9, 1.7, 0.4], [4.6, 3.4, 1.4, 0.3],  # setosa
    [7.0, 3.2, 4.7, 1.4], [6.4, 3.2, 4.5, 1.5], [6.9, 3.1, 4.9, 1.5],  # versicolor
    [5.5, 2.3, 4.0, 1.3], [6.5, 2.8, 4.6, 1.5], [5.7, 2.8, 4.5, 1.3],  # versicolor
    [6.3, 3.3, 6.0, 2.5], [5.8, 2.7, 5.1, 1.9], [7.1, 3.0, 5.9, 2.1],  # virginica
    [6.3, 2.9, 5.6, 1.8], [6.5, 3.0, 5.8, 2.2], [7.6, 3.0, 6.6, 2.1],  # virginica
])

labels = np.array([0,0,0,0,0,0, 1,1,1,1,1,1, 2,2,2,2,2,2])
class_names = ["setosa", "versicolor", "virginica"]

print("Dataset size:", data.shape)
print("Classes:", class_names)

#training (80%) and testing (20%) manually
np.random.seed(42)
indices = np.random.permutation(len(data))
split = int(0.8 * len(data))

X_train, X_test = data[indices[:split]], data[indices[split:]]
y_train, y_test = labels[indices[:split]], labels[indices[split:]]

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

#KNN
def predict(X_train, y_train, X_test, k=3):
    predictions = []
    for test_point in X_test:
        # Calculate distance from this test point to every training point
        distances = np.sqrt(np.sum((X_train - test_point) ** 2, axis=1))
        # Pick the k nearest neighbours
        k_nearest = np.argsort(distances)[:k]
        # Vote on the most common class
        k_labels = y_train[k_nearest]
        predicted = np.bincount(k_labels).argmax()
        predictions.append(predicted)
    return np.array(predictions)


y_pred = predict(X_train, y_train, X_test, k=3)

#accuracy
accuracy = np.sum(y_pred == y_test) / len(y_test) * 100
print("Accuracy:", round(accuracy, 2), "%")

#predictions vs actual
print("\nPredicted vs Actual:")
for pred, actual in zip(y_pred, y_test):
    status = "✓" if pred == actual else "✗"
    print(f"  {status}  Predicted: {class_names[pred]:12} | Actual: {class_names[actual]}")