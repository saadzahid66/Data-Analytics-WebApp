import streamlit as st
import pandas as pd
import plotly_express as px



# --- Functions --- 

# File Uploading Section
def upload_data():
    df = pd.read_csv( r".docs\merged_sorted_formatted.csv" )

    return df

def load_selected_function(selected_function):
    df_selected_function = df_uploaded.query("Function == @selected_function")

    return df_selected_function


# --- WEB PAGE SETTINGS ---

# Page Layout Settings
st.set_page_config( page_title='Data Visualizer' , page_icon=':bar_chart:', layout='wide' )
st.title(":bar_chart: Data Visualizer")
st.subheader("Web application designed to present & visualize performance metrics of CSV formatted data sets.")
st.markdown("##")

# File Upload Section
st.header(":bar_chart: File Upload")

df_uploaded = upload_data()

# Data display & overall metrics display
left_column, right_column = st.columns(2)

with left_column:
    st.subheader(":open_file_folder:File Opened 'merged_sorted_formatted.csv'")
    st.dataframe(df_uploaded)

with right_column:
    st.subheader(":clipboard:Overall Performance Metrics")
    st.markdown("##")

    total_time = int( df_uploaded['Time'].sum() )
    min_time = float( df_uploaded['Time'].min() )
    max_time = float( df_uploaded['Time'].max() )
    avg_time = float( total_time / len(df_uploaded) )

    st.subheader(f"Total Time:  {total_time} s")
    st.subheader(f"Average Time:    {avg_time} s")
    st.subheader(f"Maximum Time:    {max_time} s")
    st.subheader(f"Minimum Time:    {min_time} s")


# Data Plot of overall metrics (i.e total , min, max, average)
