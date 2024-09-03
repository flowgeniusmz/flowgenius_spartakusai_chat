import streamlit as st

class SessionState:
    def __init__(self):
        self.initial_state = dict(st.secrets.sessionstate)
        self._initialize_state()
        #self.initial_state['messages'] = [{"role": "assistant", "content": "Are you here to buy insurance?"}]

    def _initialize_state(self):
        for key, value in self.initial_state.items():
            if key not in st.session_state:
                st.session_state[key] = value

    @classmethod
    def get(cls):
        if "session_state_instance" not in st.session_state:
            st.session_state.session_state_instance = cls()
        return st.session_state.session_state_instance
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            st.session_state[key] = value

    def get_value(self, key):
        return st.session_state.get(key, None)
    
    @staticmethod
    def _read_file_content(filepath):
        try:
            with open(filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found."

    def set_file_content(self, key, filepath):
        content = self._read_file_content(filepath)
        st.session_state[key] = content
    

