import streamlit as st
import json
import requests


class WelcomeEmail:
    def __init__(self):
        self.init_values()
        self.send_request()

    def init_values(self):
        self.url = st.secrets.requests.welcome_email
        self.content_type = "application/json"
        self.accept = "*/*"
        #self.username = st.session_state.username
        #self.password = st.session_state.password
        self.username = "michael.zozulia@almalasers.com"
        self.password = "EveryQuinn"
        self.payload = {"username": self.username, "password": self.password}

    def send_request(self):
        self.response = requests.post(url=self.url, json=self.payload)
        self.response_text = self.response.text
        #self.response_json = self.response.json()
        #print(self.response_json)



