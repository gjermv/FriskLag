import streamlit as st 
import pandas as pd

players = ['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6']


for p in players:
    st.checkbox(p)

