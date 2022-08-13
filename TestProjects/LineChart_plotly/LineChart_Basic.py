import pandas as pd
import plotly.express as px
import streamlit as st

from datetime import date
from plotly import graph_objs as go



# --- Functions --- 

# File Uploading Section
def upload_data():
    df = pd.read_csv( r".docs\merged_sorted_formatted.csv" )

    return df

def load_selected_function(selected_function):
    df_selected_function = df_uploaded.query("Function == @selected_function")

    return df_selected_function

# Data Plotting
def plot_raw_data():
    fig_raw = go.Figure()
    fig_raw.add_trace(go.Scatter(x=df_uploaded['time_stamp']), y=df_uploaded['Time'], name='time(s)' )
    fig_raw.layout.update(title_text="Raw Data Plotter", xaxis_rangeslider_visible=True)

    st.plotly_chart(fig_raw)

def plot_selected_data():
    fig_selected = go.Figure()
    fig_selected.add_trace(go.Scatter(x=df_uploaded['time_stamp'], y=df_uploaded['Time'], name='time(s)'))
    fig_selected.layout.update(title_text="Raw Data Plotter", xaxis_rangeslider_visible=True)

    st.plotly_chart(fig_selected)



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

# Plot Graph For Sorted Dataframe
st.header("Plot Data Frame ")
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Plot Raw Data")
    # plot_raw_data() Note: This wont work, find another fix

with right_column:
    st.subheader("Plot Raw Data: July,2022")
    plot_selected_data()