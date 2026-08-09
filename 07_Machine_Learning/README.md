# Machine Learning 

Practice exercises covering supervised learning from core theory (supervised vs. unsupervised, train/test splits, overfitting) through building and evaluating regression and classification models.

## What's Inside

### `linear_regression.py`
- Predicting a continuous value (e.g., salary from years of experience)
- Train/test splitting with `train_test_split`
- Training a model with `LinearRegression().fit()`
- Evaluating performance with Mean Squared Error (MSE) and R² Score
- Making predictions on new, unseen data

### `logistic_regression.py`
- Binary classification on the Titanic dataset — predicting passenger survival
- Encoding categorical features (`Sex`) into numeric form with `.map()`
- Training a `LogisticRegression` classifier on real, messy data
- Evaluating with Accuracy, Precision, Recall, and F1 Score — and understanding
  why accuracy alone can be misleading
- Reading a Confusion Matrix (true/false positives and negatives)

## Key Concepts Covered

- **Supervised learning**: Regression (predicting numbers) vs. Classification (predicting categories)
- **Train/test split**: why evaluating a model on unseen data is essential
- **Overfitting**: recognizing when a model has memorized training data rather than learned a general pattern
- **Model evaluation**: choosing the right metric for the problem — MSE/R² for regression, Precision/Recall/F1 for classification

## Tech Stack

- Python
- Pandas
- scikit-learn
