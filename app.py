import streamlit as st
import pandas as pd
import gspread
import json
from google.oauth2.service_account import Credentials

# --- GOOGLE SHEET SETUP ---
SHEET_ID = "1dlPKBqb6fNB5xp2l0uqXSW4WSmw-_hhSjJNx3CrGJnU"

# Connect to Google Sheet
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds_dict = **st.secrets.gcp_service_account"
#st.write(creds_dict)
if "data" not in st.session_state:
    creds = Credentials.from_service_account_info(creds_dict)
    #cred["private_key"] = cred["private_key"].replace("\\n", "\n")
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).sheet1
    
    # Load data
    data = pd.DataFrame(sheet.get_all_records())
    st.session_state.data=data

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
st.dataframe(st.session_state.data.sort_values(by="Points", ascending=False), use_container_width=True)

# Optional: search/filter
search = st.text_input("Search Player:")
if search:
    filtered = st.session_state.data[st.session_state.data["Name"].str.contains(search, case=False)]
    st.dataframe(filtered)

st.caption("Auto-updating from Google Sheets ✨")
