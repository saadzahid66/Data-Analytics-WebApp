from re import template
from unittest.mock import patch
import pandas as pd
import plotly.express as px
import streamlit as st

from datetime import date
from plotly import graph_objs as go


# --- Global Variables

# File
dataset_path = ".docs\merged_sorted_formatted.csv"

# --- Functions --- 

# File Uploading Section
def upload_data():
    df = pd.read_csv( dataset_path )
    df.Name = dataset_path[6:-4]

    return df

def load_selected_function(selected_function):
    df_selected_function = df_uploaded.query("Function == @selected_function")

    return df_selected_function



# --- Page Settings ---
st.set_page_config( page_title="Bar Chart Plotter", page_icon=":chart_with_upwards_trend:", layout="wide" )
st.title("Bar Chart Plotter")



# --- Main Screen ---

# Display Data Frame
header_Display = st.header("Display Data Frame ")
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

header_Display.header(f"File Uploaded: '{df_uploaded.Name}' ")

# Plot Graph For Sorted Dataframe
st.header("Plot Data Frame ")

st.subheader("Performance Metrics")

total_time = int( df_uploaded['Time'].sum() )
min_time = float( df_uploaded['Time'].min() )
max_time = float( df_uploaded['Time'].max() )
avg_time = float( total_time / len(df_uploaded) - 1 )

st.caption(f"Total Time: {total_time}")
st.caption(f"Total Time: {min_time}")
st.caption(f"Total Time: {max_time}")
st.caption(f"Total Time: {avg_time}")


st.subheader("Max Time (Horizontal)")
    
df_grouped_function_time = df_uploaded.groupby( by=['Function'] ).max()[ ['Time'] ].sort_values( by=['Function'] )

fig_grouped_function_time = px.bar( df_grouped_function_time, x='Time', y= df_grouped_function_time.index, orientation='h', color_discrete_sequence=["#0083B8"] * len(df_grouped_function_time) , template='plotly_white' )
fig_grouped_function_time.layout.update(title_text="Max Time Taken By Functions", xaxis_rangeslider_visible=True)

st.plotly_chart(fig_grouped_function_time)
