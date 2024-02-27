import os, sys
from datetime import datetime as dt
import pandas as pd
import streamlit as st
# from dotenv import load_dotenv

sys.path.append(os.getcwd())
from utils.file_operations import (
    convert_to_json,
    convert_to_csv
)

# load_dotenv()

st.title("File Operations - ⚡")
st.write("Only support xlsx, csv and json file")
st.divider()

uploaded_file = st.file_uploader("Upload a file, which you want to convert")

if uploaded_file:
    uploaded_file_metadata = {}
    uploaded_file_metadata["uploaded_file_name"] = uploaded_file.name
    uploaded_file_metadata["uploaded_file_dt"] = str(dt.today())
    uploaded_file_metadata["uploaded_file_extension"] = uploaded_file.name.split('.')[-1]
    
    with st.expander("Metadata of Uploaded File -"):
        st.table(pd.DataFrame([uploaded_file_metadata]))
    
    if uploaded_file_metadata["uploaded_file_extension"] == "xlsx":
        df = pd.read_excel(uploaded_file, header=0)
        
        with st.expander("Top 5 Rows of Uploaded File -"):
            st.dataframe(df.head(5))
        
        with st.expander("Convert The Uploaded File To Other Formats -"):
            if st.button(label=':green[Convert To JSON]'):
                output_json = convert_to_json(df.loc[0:2, :])
                st.write(output_json)
            
            if st.button(label=':green[Convert To CSV]'):
                output_csv = convert_to_csv(df.loc[0:2, :])
                st.write(output_csv)
        
        with st.expander("Download The Uploaded File To Other Formats -"):
            st.download_button(
                label="Download data as JSON",
                data=convert_to_json(df),
                file_name=f"{uploaded_file.name.split('.')[0]}.json",
                mime='text/json',
            )
         
            st.download_button(
                label="Download data as CSV",
                data=convert_to_csv(df),
                file_name=f"{uploaded_file.name.split('.')[0]}.csv",
                mime='text/csv',
            )
else:
    pass