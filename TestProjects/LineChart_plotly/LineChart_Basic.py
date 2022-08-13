import pandas as pd
import plotly.express as px
import streamlit as st

from datetime import date
from plotly import graph_objs as go


# File Uploading Section
def upload_data():
    df = pd.read_csv( r".docs\merged_sorted_formatted.csv" )

    return df

def load_selected_function(selected_function):
    df_selected_function = df_uploaded.query("Function == @selected_function")

    return df_selected_function


# --- Page Settings ---
st.set_page_config( page_title="Line Chart Plotter", page_icon=":bar_chart:", layout="wide" )
st.title("Line Chart Plotter")


# --- Main Screen ---

# Display Data Frame
st.header("Display Data Frame ")
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Raw Data Set")

    df_uploaded = upload_data()
    st.dataframe(df_uploaded.tail())

with right_column:
    st.subheader("Selected Function Set")

    functions = ( "main.py (API)  save_to_db", "main.py (API)  collection_exists"  )
    selected_function = st.selectbox("Select Function", functions)
    df_selected_function = load_selected_function(selected_function)

    st.dataframe(df_selected_function.tail())