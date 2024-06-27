import streamlit as st 
import pandas as pd
import random as rd

if 'team' not in st.session_state:
    st.session_state.team = ['Player 1','Player 2','Player 3','Player 4','Player 5','Player 6']

for p in st.session_state.team: 
    if p not in st.session_state:
        st.session_state[p] = ''

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
    for px in st.session_state.team:
        if st.session_state[px]:
            st.session_state.team.remove(px)
            st.session_state.team.append(px)
            break


st.write('Utespillere:')

for p in st.session_state.team[:st.session_state.numPlayers]:
    myP= {'player':p}
    st.session_state[p] = st.checkbox(p, on_change=addScorer, kwargs=myP)
   

st.write('Innbyttere')

for p in st.session_state.team[st.session_state.numPlayers:]:
    st.checkbox(p)

swap = {'p1': 'Player 4', 'p2': 'Player 2'}
st.button('Bytt', on_click=swapPlayer,kwargs=swap)

st.button('Spiller Pluss', on_click=teamInc)
st.button('Spiller Minus', on_click=teamDec)

st.divider()

st.write('Målscorer')

    
