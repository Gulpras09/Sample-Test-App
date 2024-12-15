import streamlit as st

st.text("Welcome, Prasad! Your first Streamlit app awaits.")

# Standard imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# 1. Get the data ready
import pandas as pd
heart_disease = pd.read_csv(r"C:\Users\91917\Desktop\ML_Projects\01.Backup\DS_ML_Code\ML_Projects\02. Doc\scikit-learn-data (1).csv")
heart_disease
