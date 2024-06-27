import streamlit as st 
import pandas as pd
import random as rd

if 'team' not in st.session_state:
    st.session_state.team = ['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6']


if 'numPlayers' not in st.session_state:
    st.session_state.numPlayers = 4

if 'scorer' not in st.session_state:
    st.session_state.scorer = ['Spiller']

def teamInc():
    st.session_state.numPlayers += 1

def teamDec():
    st.session_state.numPlayers -= 1

def addScorer(player):
    st.session_state.scorer.append(player)

def swapPlayer(p1, p2):
    st.session_state.team[1] = 'test'
    st.write(p1,p2)
    

st.write('Spillere')

for p in st.session_state.team[:st.session_state.numPlayers]:
    myP= {'player':p}
    st.checkbox(p, on_change=addScorer, kwargs=myP)

st.write('Reserver')

for p in st.session_state.team[st.session_state.numPlayers:]:
    st.checkbox(p)

swap = {'p1': 'Player 4', 'p2': 'Player 2'}
st.button('Bytt', on_click=swapPlayer,kwargs=swap)

st.button('Spiller Pluss', on_click=teamInc)
st.button('Spiller Minus', on_click=teamDec)

st.divider()

st.write('Målscorer')
for item in st.session_state.scorer:
    st.write(item)
    
