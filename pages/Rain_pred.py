import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


st.title("Rain Prediction")

st.sidebar.header('Upload your CSV file')
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    def load_data(file):
        data = pd.read_csv(file)
        return data

    data = load_data(uploaded_file)

    st.subheader('Weather Data')
    st.write(data)

    def preprocess_data(data):
        X = data.drop('Rain', axis=1)
        y = data['Rain']
        return X, y

    X, y = preprocess_data(data)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    st.subheader('Model Accuracy')
    st.write(f"{accuracy * 100:.2f}%")

    st.sidebar.header('Input Features for Prediction')

    def user_input_features():
        features = {}
        for column in X.columns:
            features[column] = st.sidebar.number_input(f'Input {column}', float(X[column].min()), float(X[column].max()), float(X[column].mean()))
        return pd.DataFrame(features, index=[0])

    input_df = user_input_features()

    prediction = model.predict(input_df)

    st.subheader('Prediction')
    st.write("Rain" if prediction[0] == 1 else "No Rain")

else:
    st.info('Please upload a CSV file to start.')
