import joblib
import pandas as pd

# Load model files
model = joblib.load(r'C:\Users\suvar.LAPTOP-UHQNOLH5\Desktop\Project\models\churn_model.pkl')
expected_columns = joblib.load(r'C:\Users\suvar.LAPTOP-UHQNOLH5\Desktop\Project\models\expected_columns.pkl')

def predict_churn(data_dict):
    df = pd.DataFrame([data_dict])

    # Convert numeric columns if needed
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    categorical_cols = ['Contract', 'PaymentMethod', 'InternetService']
    available_cats = [col for col in categorical_cols if col in df.columns]

    df_encoded = pd.get_dummies(df, columns=available_cats, drop_first=True)

    # Add missing columns
    for col in expected_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[expected_columns]

    prob = model.predict_proba(df_encoded)[:, 1][0]

    if prob >= 0.55:
        return "Likely to Churn"
    else:
        return "Not Likely to Churn"