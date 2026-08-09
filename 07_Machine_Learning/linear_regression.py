import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# TASK 1: Student Marks Prediction based on Study Hours

# 1. Dataset Initialization
study_data = {
    "Study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 50, 55, 65, 70, 78, 85, 90, 95],
}
df_study = pd.DataFrame(study_data)

# 2. Feature and Target Selection (X must be 2D DataFrame, y must be 1D Series)
X_study = df_study[["Study_hours"]]
y_study = df_study["Marks"]

# 3. Train-Test Split (80% Training, 20% Testing)
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_study, y_study, test_size=0.2, random_state=42
)

# 4. Model Training
study_model = LinearRegression()
study_model.fit(X_train_s, y_train_s)

# 5. Model Evaluation
study_predictions = study_model.predict(X_test_s)
mse_s = mean_squared_error(y_test_s, study_predictions)
r2_s = r2_score(y_test_s, study_predictions)

print("Task 1: Student Marks Prediction\n")
print("Predicted Marks:", study_predictions)
print("Actual Marks:   ", y_test_s.values)
print(f"Slope (m):       {study_model.coef_[0]:.2f}")
print(f"Intercept (c):   {study_model.intercept_:.2f}")
print(f"MSE:             {mse_s:.2f}")
print(f"R² Score:        {r2_s:.2f}")

# 6. Predict for New Input
new_student = pd.DataFrame({"Study_hours": [7.5]})
pred_marks = study_model.predict(new_student)
print(
    f"Predicted marks for 7.5 study hours: {pred_marks[0]:.2f}\n"
)

# TASK 2: Salary Prediction based on Years of Experience

# 1. Dataset Initialization
salary_data = {
    "Experience_years": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [
        30000,
        35000,
        40000,
        48000,
        55000,
        60000,
        68000,
        75000,
        82000,
        90000,
    ],
}
df_salary = pd.DataFrame(salary_data)

# 2. Feature and Target Selection
X_salary = df_salary[["Experience_years"]]
y_salary = df_salary["Salary"]

# 3. Train-Test Split
X_train_sal, X_test_sal, y_train_sal, y_test_sal = train_test_split(
    X_salary, y_salary, test_size=0.2, random_state=42
)

# 4. Model Training
salary_model = LinearRegression()
salary_model.fit(X_train_sal, y_train_sal)

# 5. Model Evaluation
salary_predictions = salary_model.predict(X_test_sal)
mse_sal = mean_squared_error(y_test_sal, salary_predictions)
rmse_sal = np.sqrt(mse_sal)  # Root Mean Squared Error for scale context
r2_sal = r2_score(y_test_sal, salary_predictions)

print("\n Task 2: Salary Prediction \n")
print("Predicted Salary:", salary_predictions)
print("Actual Salary:   ", y_test_sal.values)
print(f"MSE:              {mse_sal:.2f}")
print(f"RMSE:             {rmse_sal:.2f} (Error in actual currency units)")
print(f"R² Score:         {r2_sal:.2f}")

# 6. Predict for New Input
new_employee = pd.DataFrame({"Experience_years": [12]})
pred_salary = salary_model.predict(new_employee)
print(f"Predicted salary for 12 years experience: ${pred_salary[0]:,.2f}")