from PIL import Image
import streamlit as st

# im = Image("")
st.set_page_config(
        page_title="TheDataFestAI",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )
st.header("Welcome To TheDataFestAI! 👋")
st.divider()


st.markdown(
    """
    ## Click below links -
    - [Convert File Types](Convert_File_Type)
    
    """
)

st.divider()
st.write("A Small Initiative By: Indranil Pal")
st.write("For any issues/concerns, please raise ticket here [click here]('https://github.com/easycloudapi/thedatafestai_streamlit/issues')")