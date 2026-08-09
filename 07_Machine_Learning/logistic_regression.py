import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

# Titanic Survival Classification using Logistic Regression

# 1. Load Dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df_titanic = pd.read_csv(url)

# 2. Data Preprocessing & Feature Engineering
# Impute missing values in 'Age' using the median strategy
df_titanic["Age"] = df_titanic["Age"].fillna(df_titanic["Age"].median())

# Map binary categorical column 'Sex' to numeric representations (Male: 0, Female: 1)
df_titanic["Sex"] = df_titanic["Sex"].map({"male": 0, "female": 1})

# 3. Feature & Target Isolation
X_titanic = df_titanic[["Pclass", "Sex", "Age"]]
y_titanic = df_titanic["Survived"]

# 4. Train-Test Split (80% Training, 20% Testing)
X_train_t, X_test_t, y_train_t, y_test_t = train_test_split(
    X_titanic, y_titanic, test_size=0.2, random_state=42
)

# 5. Model Instantiation & Training
clf_model = LogisticRegression()
clf_model.fit(X_train_t, y_train_t)

# 6. Predictions & Classification Metrics Evaluation
y_pred_t = clf_model.predict(X_test_t)

acc = accuracy_score(y_test_t, y_pred_t)
prec = precision_score(y_test_t, y_pred_t)
rec = recall_score(y_test_t, y_pred_t)
f1 = f1_score(y_test_t, y_pred_t)
cm = confusion_matrix(y_test_t, y_pred_t)

print("\n Titanic Survival Classification Metrics \n")
print(f"Accuracy:  {acc:.4f}")
print(f"Precision: {prec:.4f}")
print(f"Recall:    {rec:.4f}")
print(f"F1 Score:  {f1:.4f}")
print("\nConfusion Matrix (TN, FP / FN, TP):")
print(cm)