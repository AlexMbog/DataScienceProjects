import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student_exam_scores.csv')

st.set_page_config(page_title="Student Data Analysis", page_icon=":bar_chart:", layout="wide")

st.title("Student Exam Data Dashboard")
st.markdown("Analyze relationships between study habits and performance.")

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info("Upload a file through config", icon="ℹ️")
    st.stop()

df = pd.read_csv(uploaded_file)

numeric_df = df.select_dtypes(include=['number'])
corr = numeric_df.corr()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Heatmap")
    st.pyplot(fig)

with col2:
    st.subheader("Histogram for Distribution")
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    if numeric_columns:
        selected_column = st.selectbox("Select a numeric column", numeric_columns)
        fig, ax = plt.subplots()
        ax.hist(df[selected_column].dropna(), bins=10, color='skyblue', edgecolor='black')
        ax.set_title(f"Distribution of {selected_column}")
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Count")
        st.pyplot(fig)
    else:
        st.info("No numeric columns available for histogram.")

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Scatter Plot")
    x_col = st.selectbox("Select X-axis:", df.select_dtypes(include='number').columns, key="xaxis")
    y_col = st.selectbox("Select Y-axis:", df.select_dtypes(include='number').columns, key="yaxis")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
    ax.set_title(f"{y_col} vs {x_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

with col4:
    st.subheader("Summary Statistics")
    st.dataframe(df.describe())
