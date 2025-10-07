import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# --- GOOGLE SHEET SETUP ---
SHEET_URL = "https://docs.google.com/spreadsheets/d/1dlPKBqb6fNB5xp2l0uqXSW4WSmw-_hhSjJNx3CrGJnU/edit#gid=0"

# Connect to Google Sheet
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("service_account.json", scopes=scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(SHEET_URL).sheet1

# Load data
data = pd.DataFrame(sheet.get_all_records())

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    body { background-color: #f7f7f9; color: #222; }
    .leaderboard-title {
        text-align: center;
        font-size: 40px;
        font-weight: 700;
        color: #ff4b4b;
        margin-bottom: 30px;
    }
    .stDataFrame { border-radius: 12px; overflow: hidden; }
    .css-1q8dd3e { background-color: #fff !important; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- UI ---
st.markdown("<div class='leaderboard-title'>🏆 Live Leaderboard</div>", unsafe_allow_html=True)

# Sorting & filtering
st.dataframe(data.sort_values(by="Points", ascending=False), use_container_width=True)

# Optional: search/filter
search = st.text_input("Search Player:")
if search:
    filtered = data[data["Name"].str.contains(search, case=False)]
    st.dataframe(filtered)

st.caption("Auto-updating from Google Sheets ✨")
