import streamlit as st
import numpy as np
import os
from helper import draw_embed, create_spectrogram, read_audio, record, save_record
import requests
import json
st.set_page_config(layout="wide")
st.header("1. Record your own voice")

if st.button(f'Click to Record'):
    record_state = st.text("Recording...")
    filename = 'audio'
    duration = 5  # seconds
    fs = 48000
    myrecording = record(duration, fs)
    record_state.text(f"Saving sample as {filename}.mp3")

    path_myrecording = f"./samples/{filename}.mp3"

    save_record(path_myrecording, myrecording, fs)
    record_state.text(f"Done! Saved sample as {filename}.mp3")

col1, col2, col3= st.columns((2,2,1))

with col1:
    username = st.text_input("Choose a filename: ")
    # Add chart #1
    if st.button(f'Train'):
        result = st.text("Train....")
        url = 'http://localhost:8000/addData'
        print(username)
        files = {'file': open('./samples/audio.mp3','rb')}
        data = {'username':username}
        r = requests.post(url, files=files, data=data)
        print(r.json())
        result.text(f'{r['status']}')

with col2:
    # Add chart #4
    if st.button(f'Predict'):
        result = st.text("Predict....")
        url = 'http://localhost:8000/predict'
        files = {'file': open('./samples/audio.mp3','rb')}
        r = requests.post(url, files=files)
        print(r.json())
        result.text(f'{r['status']}, intent is {r['intent']}, username is {r['username']}')

with col3:
    if st.button(f'Check'):
        url = 'http://localhost:8000/check'
        r = requests.get(url)
        print(r.json())
        res = st.text(f'{r['status']}')




    

