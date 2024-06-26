import streamlit as st 
import pandas as pd
import random as rd


players = ['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6']


if 'numPlayers' not in st.session_state:
    st.session_state.numPlayers = 4

if 'scorer' not in st.session_state:
    st.session_state.scorer = ['test','test']

def teamInc():
    st.session_state.numPlayers += 1

def addScorer():
    st.session_state.scorer = ['test','Not test']

st.write('Spillere')

for p in players[:st.session_state.numPlayers]:
    st.checkbox(p, on_change=addScorer )

st.write('Reserver')
for p in players[st.session_state.numPlayers:]:
    st.checkbox(p)

st.button('Bytt', on_click=teamInc)



st.write('Målscorer')
for item in st.session_state.scorer:
    st.write(item)
    
