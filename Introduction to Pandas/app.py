import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Viewer & Cleaner")
st.write("Upload a CSV file ")

# --- Sample Data ---
data = {
    "Name": ["Alice", "Bob", "Charlie", "", "123"],
    "Age": [25, 30, 35, 65, "jane"]
}
df = pd.DataFrame(data)

st.subheader("Original Data")
st.table(df)

#Print row at index 0 (to console)
print(df.loc[0])

# Data Cleaning 
#Replace empty strings ("") with NaN
df.replace("", pd.NA, inplace=True)

#Drop rows with missing values
clean_df = df.dropna()
print(clean_df.to_string())

#convert 'Age' to numeric, coercing invalid entries
clean_df["Age"] = pd.to_numeric(clean_df["Age"], errors="coerce")

#Drop rows where conversion failed (NaN)
clean_df = clean_df.dropna(subset=["Age"])
print(clean_df.to_string())

clean_df["Age"] = pd.to_numeric(clean_df["Age"], errors="coerce")

# Drop rows where conversion failed (NaN)
clean_df = clean_df.dropna(subset=["Age"])

st.subheader("Cleaned Data")
st.table(clean_df)
plot_df = clean_df 
st.subheader("1) Age distribution (histogram)")
fig1, ax1 = plt.subplots()
ax1.hist(plot_df["Age"].dropna(), bins=5)
ax1.set_xlabel("Age")
ax1.set_ylabel("Count")
ax1.set_title("Histogram of Age (numeric coercion)")
st.pyplot(fig1)

# Crete a scatter plot of Age vs Name

st.subheader("2) Age vs Name (scatter plot)")
fig2 ,ax2 = plt.subplots()
ax2.scatter(plot_df["Name"], plot_df["Age"])
ax2.set_xlabel("Name")
ax2.set_ylabel("Age")
ax2.set_title("Scatter Plot of Age vs Name")
plt.xticks(rotation=45)
st.pyplot(fig2)