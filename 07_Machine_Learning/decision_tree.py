import pandas as pd
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the Titanic dataset from the repository
data = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

# Impute missing values in the Age column using the median value
data["Age"] = data["Age"].fillna(data["Age"].median())

# Encode the categorical Sex feature into numerical format (male: 0, female: 1)
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

# Define the features matrix (X) and target vector (y)
X = data[["Pclass", "Sex", "Age"]]
y = data["Survived"]

# Split data into 80% training set and 20% testing set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize Decision Tree model with max_depth=4 to prevent overfitting
model = DecisionTreeClassifier(max_depth=4, random_state=42)

# Train the Decision Tree classifier on the training data
model.fit(X_train, y_train)

# Predict survival status on the unseen test set
prediction = model.predict(X_test)
print("Predicted values: ", prediction)
print("Actual values: ", y_test.values)

# Calculate and print model accuracy score
accuracy = accuracy_score(y_test, prediction)
print(f"Accuracy score: {accuracy:.2f}")

# Calculate and print model precision score
precision = precision_score(y_test, prediction)
print(f"Precision score: {precision:.2f}")