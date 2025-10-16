import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Correlation Table Viewer")

# --- Sample Data ---
data = {
    "Age": [25, 30, 35, 40, 45],
    "Score": [80, 85, 88, 90, 95],
    "Experience": [1, 3, 5, 7, 9]
}

df = pd.DataFrame(data)
st.subheader("Original Data")
st.table(df)

#Compute Correlation
corr_table = df.corr(numeric_only=True)

st.subheader("Correlation Table")
st.table(corr_table.style.format("{:.2f}"))  # show 2 decimal places
