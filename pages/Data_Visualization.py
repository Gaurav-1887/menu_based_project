import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

def infer_plot_type(data):
    if data.shape[1] == 1:
        return "Histogram"
    elif data.shape[1] == 2 and pd.api.types.is_numeric_dtype(data.iloc[:, 1]):
        return "Bar Chart"
    elif data.shape[1] == 2 and pd.api.types.is_object_dtype(data.iloc[:, 1]):
        return "Pie Chart"
    elif data.shape[1] > 2:
        return "Line Chart"
    else:
        return "Line Chart"

def preprocess_data(data):
    label_encoders = {}
    for column in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    return data, label_encoders

def generate_plot(data, plot_type):
    st.subheader(f"Generated Plot: {plot_type}")

    if plot_type == "Line Chart":
        st.line_chart(data)
    elif plot_type == "Bar Chart":
        st.bar_chart(data)
    elif plot_type == "Histogram":
        plt.figure(figsize=(10, 6))
        data.hist(bins=10, alpha=0.7, grid=False)
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Histogram')
        st.pyplot(plt)
    elif plot_type == "Pie Chart":
        plt.figure(figsize=(10, 6))
        if data.shape[1] > 1:
            data = data.set_index(data.columns[0])
            data = data[data.columns[0]]
        plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Pie Chart')
        st.pyplot(plt)
    else:
        st.error("Unsupported plot type selected.")

def main():
    st.title("Interactive Plot Generator")
    st.write("Upload an Excel file and let the app automatically generate the appropriate plot.")

    uploaded_file = st.file_uploader("Upload an Excel file", type=['xlsx'])

    if uploaded_file is not None:
        data = pd.read_excel(uploaded_file)
        st.subheader("Uploaded Data")
        st.dataframe(data)

        plot_type = infer_plot_type(data)
        data, label_encoders = preprocess_data(data)

        generate_plot(data, plot_type)

if __name__ == "__main__":
    main()
