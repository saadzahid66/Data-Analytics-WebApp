import requests as req
import streamlit_lottie as st_lottie
import streamlit as st
import pandas as pd
import plotly_express as px

from datetime import date
from plotly import graph_objs as go
from PIL import Image as img



# --- Helpful Variables ---

# Pre-written List of Functions

information_text = "This web application designed to present & visualize performance metrics of specific CSV data set ('merged_sorted.csv') present in the Git repo. To view the data in full-screen please click the button on top-right of each widget. The columns, rows & values were not formatted or truncated to keep authenticity. However, the data-set was altered to retain only useful information & decrease load times. Your feedback is much awaited. Thankyou for giving the opprotunity to do something new."

options_functions = (   "main.py (API)  main", "main.py (API)  save_to_db", "main.py (API)  collection_exists", "main.py (API)  db_get_newest_entry", "main.py (API)  read_from_db", "main.py (API)  recommendation", "main.py (API)  ai_cosin_sim", "main.py (API)  read_from_db_by_date", "main.py (API)  db_get_articles_by_url",
                        "get_newest_articles_api.py get_keywords", "get_newest_articles_api.py save_to_db", "get_newest_articles_api.py db_check_not_empty", "get_newest_articles_api.py db_get_newest_entry", "get_newest_articles_api.py get", "get_newest_articles_api.py main", 
                        "get_ge_data.py ga_api", "get_ge_data.py save_to_db", "get_ge_data.py main",
                        "daily_sdct.py (categories and keywords)  save_to_db", "daily_sdct.py (categories and keywords)  read_from_db"  
                    )


# --- Utility Functions --- 

# File Uploading Section
def upload_data():
    file = st.file_uploader("Please upload csv file to continue...", type="csv")
    try:
        df = pd.read_csv( file )
        return df
    except Exception as e:
        st.text(f"")

# Filters & displays data according to selected function
def load_selected_function(selected_function):
    df_selected_function = df_uploaded.query("Function == @selected_function")

    return df_selected_function

# Calculates meta data for overall performance (Data unformatted to keep authenticity)
def calculate_metadata(df_any):
    total_time = int( df_any['Time'].sum() )
    min_time = float( df_any['Time'].min() )
    max_time = float( df_any['Time'].max() )
    avg_time = float( df_any['Time'].mean() )

    st.text(f"  Total Time:    {total_time} s")
    st.text(f"Average Time:    {avg_time} s")
    st.text(f"Maximum Time:    {max_time} s")
    st.text(f"Minimum Time:    {min_time} s")

# Plots min,max,mean,sum of each function in the entire uploaded data-set
def plot_uploaded_data(df_uploaded, op_choice):
    if op_choice==1: df_grouped_function_time = df_uploaded.groupby( by=['Function'] ).max()[ ['Time'] ].sort_values( by=['Function'] )
    elif op_choice==2: df_grouped_function_time = df_uploaded.groupby( by=['Function'] ).min()[ ['Time'] ].sort_values( by=['Function'] )
    elif op_choice==3: df_grouped_function_time = df_uploaded.groupby( by=['Function'] ).max()[ ['Time'] ].sort_values( by=['Function'] )
    elif op_choice==4: df_grouped_function_time = df_uploaded.groupby( by=['Function'] ).max()[ ['Time'] ].sort_values( by=['Function'] )

    fig_grouped_function_time = px.bar( df_grouped_function_time, x='Time', y= df_grouped_function_time.index, orientation='h', color_discrete_sequence=["#0083B8"] * len(df_grouped_function_time) , template='plotly_white' )
    fig_grouped_function_time.layout.update( xaxis_rangeslider_visible=True )

    st.plotly_chart(fig_grouped_function_time)

# Plots the data for the selected function from the select-box
def plot_selected_data(df_selected_function):
    fig_selected_function = go.Figure()
    fig_selected_function.add_trace( go.Scatter( x=df_selected_function['time_stamp'], y=df_selected_function['Time'], name='time(s)' ) )
    fig_selected_function.layout.update( xaxis_rangeslider_visible=True, xaxis=(dict(showgrid=False)), yaxis=(dict(showgrid=False)), plot_bgcolor="rgba(0,0,0,0)",   )

    st.plotly_chart(fig_selected_function, use_container_width=True )





# --- WEB PAGE SETTINGS & MAIN CODE ---

# Page Layout Settings
st.set_page_config( page_title='Data Visualizer' , page_icon=':bar_chart:', layout='wide' )
st.title(":bar_chart: Data Visualizer")
st.markdown(information_text)
st.markdown("---")
st.markdown("##")


# File Upload Section
with st.sidebar:
    streamlit_logo = img.open('D:\Work\Python\Data Analytics WebApp\.resources\streamlit-logo.png')
    st.image(streamlit_logo)
    st.markdown("##")

    st.header(":page_facing_up: Upload File")
    df_uploaded = upload_data()



# Data display & overall metrics display
if df_uploaded is not None:
    st.header(":bar_chart: Dataset Analysis")

    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader(":open_file_folder:File Opened 'merged_sorted.csv'")
        st.dataframe(df_uploaded)

    with right_column:
        st.subheader(":clipboard:Overall Performance Metrics")
        st.markdown("##")

        calculate_metadata(df_uploaded)


# Data plot of Maximum & Minimum time taken by each function
if df_uploaded is not None:
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader(":chart_with_upwards_trend:Maximum Time Of Each Function")
        plot_uploaded_data(df_uploaded, 1)

    with right_column:
        st.subheader(":chart_with_upwards_trend:Minimum Time Of Each Function")
        plot_uploaded_data(df_uploaded, 2)


# Data plot of Maximum & Minimum time taken by each function
if df_uploaded is not None:
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader(":chart_with_upwards_trend:Total Time Of Each Function")
        plot_uploaded_data(df_uploaded, 3)

    with right_column:
        st.subheader(":chart_with_upwards_trend:Mean Time Of Each Function")
        plot_uploaded_data(df_uploaded, 4)


    st.markdown("---")


# Display filter according to selected function
if df_uploaded is not None:
    st.header(":bar_chart: Filter Data By Function")

    state_selected_function = st.text("Please Select A Function From List To Analyze...")
    selected_function = st.selectbox( " ", options_functions )
    
    df_selected_function = load_selected_function(selected_function)


# Data display & overall metrics display
if df_uploaded is not None:
    left_column_selection, right_column_selection = st.columns(2)

    with left_column_selection:
        st.subheader(f":open_file_folder: Function '{selected_function}'")
        st.dataframe(df_selected_function)

    with right_column_selection:
        st.subheader(":clipboard:Overall Performance Metrics")
        st.markdown("##")

        calculate_metadata(df_selected_function)


    # Data plot of Function;s Time vs Timestamp
if df_uploaded is not None:
    st.subheader(":chart_with_upwards_trend:Time vs TimeStamp")
    plot_selected_data(df_selected_function)

    st.markdown("---")



