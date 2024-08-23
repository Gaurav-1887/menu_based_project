import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_data(uploaded_file):
    df = pd.read_excel(uploaded_file)
    return df

st.title('Flexible Linear Regression Model Trainer')

uploaded_file = st.file_uploader("Upload your data file (Excel format)", type=['xlsx'])

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write("Uploaded Data:")
    st.write(data)

    columns = data.columns.tolist()
    
    st.write("Select Features and Target Variable")
    feature_columns = st.multiselect("Select Feature Columns", columns)
    target_column = st.selectbox("Select Target Column", columns)

    if st.button('Train Model'):
        if not feature_columns or not target_column:
            st.error("Please select features and target variable")
        else:
            X = data[feature_columns]
            y = data[target_column]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = LinearRegression()
            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            rmse = mse ** 0.5
            r2 = r2_score(y_test, y_pred)

            st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
            st.write(f"R-squared (Model Accuracy): {r2:.2f}")

            st.write("Model Coefficients:")
            st.write(dict(zip(feature_columns, model.coef_)))

           
