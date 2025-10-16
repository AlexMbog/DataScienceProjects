"""
In an environment with streamlit, plotly and duckdb installed,
Run with `streamlit run streamlit_app.py`
"""
import random
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

#######################################
# PAGE SETUP
#######################################

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Sales Streamlit Dashboard")
st.markdown("_Prototype v0.4.1_")

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info(" Upload a file through config", icon="ℹ️")
    st.stop()

#######################################
# DATA LOADING
#######################################

#######################################
# DATA LOADING
#######################################

@st.cache_data
def load_data(uploaded_file):
    if uploaded_file is None:
        return None

    file_name = uploaded_file.name.lower()

    try:
        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif file_name.endswith((".xls", ".xlsx")):
            df = pd.read_excel(uploaded_file, engine="openpyxl")
        else:
            st.error("Unsupported file type. Please upload a .csv or .xlsx file.")
            return None
        return df

    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None


df = load_data(uploaded_file)
if df is None:
    st.stop()
