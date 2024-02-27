# Pre-Requisite:

ID  | Topic | URLs
--- | ---   | ---
1   | Streamlit             | https://docs.streamlit.io/
2   | Streamlit - Dashboard | https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/
3   | Streamlit - Emoji     | 1. https://share.streamlit.io/streamlit/emoji-shortcodes</br>2. https://emojidb.org/streamlit-emojis
4   | Snowflake Python API  | https://docs.snowflake.com/en/developer-guide/snowflake-python-api/snowflake-python-overview
5   | langchain - demo      | https://lablab.ai/t/anthropics-claude-and-langchain-tutorial-bulding-personal-assistant-app


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
# or
streamlit run Home.py --server.port 8080
```

## Step 3 - GitHub Setup For Pull/Push The Code:
```shell
git config --global user.email "emailaddress@gmail.com"
git config --global user.name "username"
# generate personal access token (https://github.com/settings/tokens)
git remote set-url origin https://<repo_account>:<MYTOKEN>@github.com/easycloudapi/thedatafestai_streamlit.git

git pull origin <branch_name>
git status
git add .
git commit -m "initial commit"
git push -u origin <branch_name>
```