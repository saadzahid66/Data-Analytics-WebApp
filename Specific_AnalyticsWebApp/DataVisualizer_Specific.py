import streamlit as st
import pandas as pd
import plotly_express as px




# --- WEB PAGE SETTINGS ---

# Page Layout Settings
st.set_page_config( page_title='Data Visualizer' , page_icon=':bar_chart:', layout='wide' )
st.title("Data Visualizer")
st.markdown("---")

# File Upload & Display Section
file_upload_header =st.header(":bar_chart: File Name 'merged_sorted_formatted.csv'")

df = pd.read_csv(r'.docs\merged_sorted_formatted.csv')
st.dataframe(df)