# Pre-Requisite:

ID | Topic | URLs
--- | --- | ---
1   | Streamlit | https://docs.streamlit.io/
2   |           | 


# Build & Run The App Locally:

## Step 1 - Build The Working Env Locally:
```shell
git clone https://github.com/easycloudapi/thedatafestai_streamlit.git
cd thedatafestai_streamlit
python -m virtualenv .venv
.venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

## Step 2 - Run The Streamlit App:
```shell
streamlit run Home.py
```