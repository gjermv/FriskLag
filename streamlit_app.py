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
    st.session_state.team.remove(p1)
    st.session_state.team.append(p1)



st.write('Spillere')

c = 0
for p in st.session_state.team[:st.session_state.numPlayers]:
    myP= {'player':p}
    st.checkbox(p, key=p+str(c), on_change=addScorer, kwargs=myP)
    c += 1

print(st.session_state.p1, st.session_state.p2)
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
    
