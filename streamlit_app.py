import streamlit as st 
import pandas as pd
import random as rd


players = ['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6']
st.session_state.numPlayers = 3

def teamInc():
    st.session_state.numPlayers += 1

st.write('Spillere')
for p in players[:st.session_state.numPlayers]:
    st.checkbox(p)

st.write('Reserver')
for p in players[st.session_state.numPlayers:]:
    st.checkbox(p)

st.button('Bytt', on_click=teamInc)
