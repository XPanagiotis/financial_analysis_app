import streamlit as st
from openai import OpenAI
import yfinance as yf

client = OpenAI(api_key=st.secrets["OPEN_API_KEY"])
print(client)