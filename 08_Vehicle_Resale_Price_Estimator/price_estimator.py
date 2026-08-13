import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split

# Load dataset
url = "https://raw.githubusercontent.com/ShuklaPrashant21/Used-Car-Price-Prediction/master/car%20data.csv"
data = pd.read_csv(url)

# Feature engineering: calculate vehicle age
data["Car_age"] = 2026 - data["Year"]

# Drop high-cardinality identifier feature
data = data.drop(columns=["Car_Name"])

# One-hot encode categorical features
ohe_encoded = pd.get_dummies(
    data[["Fuel_Type", "Seller_Type", "Transmission"]], drop_first=True
)

# Define feature matrix X and target variable y
X = pd.concat(
    [data[["Car_age", "Kms_Driven", "Present_Price"]], ohe_encoded], axis=1
)
y = data["Selling_Price"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 1. Linear Regression Model

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

prediction_linear = model_lr.predict(X_test)
mse_lr = mean_squared_error(y_test, prediction_linear)
r2_lr = r2_score(y_test, prediction_linear)

print("Linear Regression Results:")
print(f"Mean Squared Error: {mse_lr:.2f}")
print(f"R2 Score:           {r2_lr:.2f}\n")

# 2. Random Forest Regressor Model
model_rf = RandomForestRegressor(n_estimators=100, max_depth=4, random_state=42)
model_rf.fit(X_train, y_train)

prediction_rf = model_rf.predict(X_test)
mse_rf = mean_squared_error(y_test, prediction_rf)
r2_rf = r2_score(y_test, prediction_rf)

print("Random Forest Regressor Results:")
print(f"Mean Squared Error: {mse_rf:.2f}")
print(f"R2 Score:           {r2_rf:.2f}\n")

# 3. Model Validation (5-Fold Cross Validation)
cv_scores = cross_val_score(model_rf, X, y, cv=5)

print("Random Forest Cross-Validation:")
print(f"Mean CV Score:       {cv_scores.mean():.2f}")
print(f"Standard Deviation:  {cv_scores.std():.2f}\n")

# 4. Feature Importance Analysis
feature_importance_df = (
    pd.DataFrame(
        {"Feature": X.columns, "Importance": model_rf.feature_importances_}
    )
    .sort_values(by="Importance", ascending=False)
    .reset_index(drop=True)
)

# Format importance scores as percentages for clean terminal output
feature_importance_df["Importance"] = feature_importance_df["Importance"].map(
    "{:.2%}".format
)

print("Feature Importance Ranking:")
print(feature_importance_df.to_string(index=False))