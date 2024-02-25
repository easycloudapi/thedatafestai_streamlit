import os, sys
from datetime import datetime as dt
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

sys.path.append(os.getcwd())
from utils.file_operations import (
    convert_to_json,
    convert_to_csv
)

load_dotenv()

st.header("File Operations -")
st.divider()

uploaded_file = st.file_uploader("Upload a file, which you want to convert")
uploaded_filename = uploaded_file.name
uploaded_file_dt = str(dt.today())
uploaded_file_extension = uploaded_file.name.split('.')[-1]
if uploaded_file:
    st.markdown(
        f"""
        file - **{uploaded_filename}** uploaded successfully at `{uploaded_file_dt}`, 
        file extension is {uploaded_file_extension}
        """
    )
    
    if uploaded_file_extension == "xlsx":
        df = pd.read_excel(uploaded_file, header=0)
        st.write(df.sample(5))
    
        if st.button('ConvertToJson'):
            output_json = convert_to_json(df)
            st.write(output_json)
            
        if st.button('ConvertToCSV'):
            output_csv = convert_to_csv(df)
            st.write(output_csv)