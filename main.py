import streamlit as st

st.text("Welcome, Prasad! Your first Streamlit app awaits.")

# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

# 1. Import necessary libraries
import pandas as pd

# 2. Load the dataset
data_path = r"C:\Users\91917\Desktop\ML_Projects\01.Backup\DS_ML_Code\ML_Projects\02. Doc\scikit-learn-data (1).csv"
heart_disease = pd.read_csv(data_path)

# 3. Display the loaded dataset
print("Heart Disease Dataset Loaded Successfully!")
print(f"Dataset Shape: {heart_disease.shape}")
print("\nFirst 5 Rows of the Dataset:\n")
print(heart_disease.head())

