import streamlit as st 
import pandas as pd
import random as rd


players = ['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6']

if 'numPlayers' not in st.session_state:
    st.session_state.numPlayers = 4

if 'scorer' not in st.session_state:
    st.session_state.scorer = []

def teamInc():
    st.session_state.numPlayers += 1

def addScorer(p):
    st.session_state.scorer.append('Test')

st.write('Spillere')

for p in players[:st.session_state.numPlayers]:
    st.checkbox(p)

st.write('Reserver')
for p in players[st.session_state.numPlayers:]:
    st.checkbox(p)

st.button('Bytt', on_click=teamInc)
st.button('Målscorer', on_click=addScorer)
st.write('Bytt', st.session_state.numPlayers)

for s in st.session_state.scorer:
    st.write(s)
    
