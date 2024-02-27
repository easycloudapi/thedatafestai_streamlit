import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer, init_streamlit_comm
import streamlit as st


st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
init_streamlit_comm()

st.title("Data EDA (Exploratory Data Analysis) 🕵")

# col1, col2 = st.columns(2, gap="small")
# with col1:
#     file_type_val = st.radio("Choose any file type -", ("csv", "json", "xlsx"))
# with col2:
#     uploaded_file = st.file_uploader(f"upload {''} file")
    
# if uploaded_file:
#     df = pd.read_csv(uploaded_file, header=0)
#     st.write(f"file_type - {file_type_val}")

@st.cache_resource
def get_pyg_df_renderer():
    df = pd.read_csv("https://corgis-edu.github.io/corgis/datasets/csv/cars/cars.csv", header=0)

    st.header("Metadata - ")

    with st.expander("Dataframe - Sample Data"):
        st.table(df.sample(10))

    with st.expander("Dataframe - Size"):
        st.text(f"dataframe has rows: {df.shape[0]} and cols: {df.shape[1]}")
    
    with st.expander("Dataframe - Columns"):
        st.write(df.columns)
    
    with st.expander("Dataframe - Column Types"):
        st.write(df.dtypes)
    
    # if df is not None:
    #     html_output = pyg.walk(df, env='Streamlit')
    #     st.write(html_output, unsafe_allow_html=True)
        
    return StreamlitRenderer(df, spec=".streamlit\gw_config.json", debug=False)
    # return StreamlitRenderer(df, debug=False)

renderer = get_pyg_df_renderer()
renderer.render_explore()