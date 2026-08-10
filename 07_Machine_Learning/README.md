# Machine Learning

Practice exercises covering supervised learning from core theory (supervised vs. unsupervised, train/test splits, overfitting) through building and evaluating regression, classification, and ensemble models.

## What's Inside

### `linear_regression.py`
- Predicting continuous numerical values (e.g., student marks from study hours, salary from experience)
- Train/test splitting with `train_test_split`
- Training a model with `LinearRegression().fit()`
- Evaluating performance with Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score
- Making predictions on new, unseen data

### `logistic_regression.py`
- Binary classification on the Titanic dataset — predicting passenger survival
- Data preprocessing: handling missing values with median imputation and encoding categorical features (`Sex`) into numeric form
- Training a `LogisticRegression` classifier
- Evaluating with Accuracy, Precision, Recall, and F1 Score — and understanding why accuracy alone can be misleading
- Reading a Confusion Matrix (True/False Positives and Negatives)

### `decision_tree.py`
- Non-linear binary classification using `DecisionTreeClassifier` on the Titanic dataset
- Controlling tree growth with `max_depth` to prevent overfitting
- Comparing classification metrics against Logistic Regression

### `random_forest.py`
- Ensemble learning using `RandomForestClassifier` with multiple decision trees (`n_estimators=100`)
- Evaluating ensemble performance on unseen test data
- Extracting and analyzing **Feature Importances** to identify which features (`Sex`, `Pclass`, `Age`) contributed most to predictions

## Key Concepts Covered

- **Supervised Learning**: Regression (predicting continuous numbers) vs. Classification (predicting categorical labels)
- **Ensemble Methods**: Bagging concept and aggregating decision trees with Random Forest
- **Train/Test Split**: Evaluating models on unseen data to measure true generalization
- **Overfitting & Tree Pruning**: Preventing decision trees from memorizing noise using `max_depth`
- **Feature Importance**: Understanding feature contribution in tree-based models
- **Model Evaluation**: Choosing the right metric — MSE/RMSE/R² for regression, and Precision/Recall/F1/Confusion Matrix for classification

## Tech Stack

- Python
- Pandas
- NumPy
- scikit-learn
