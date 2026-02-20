import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import joblib

df = pd.read_csv("data/telecom_churn.csv")
X = df.drop(["CustomerID", "Churn"], axis=1)
X_encoded = pd.get_dummies(X, columns=['Contract','PaymentMethod','InternetService'])

expected_columns = X_encoded.columns.tolist()
y = df["Churn"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)


print("training columns: ", expected_columns)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "models/churn_model.pkl")
joblib.dump(expected_columns, "models/expected_columns.pkl")
