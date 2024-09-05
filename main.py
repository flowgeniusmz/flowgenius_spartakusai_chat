import streamlit as st
import utils as u
# import sessionstate as ss
import tools as t
import app as a
import database as d
import ss


# Set page config
st.set_page_config(page_title="SpartakusAI", page_icon="assets/images/icon.png", layout="wide", initial_sidebar_state="collapsed")

# Set Title
u.page_setup()

# Set Session State
ss.initialize_session_state()


hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Set Containers
main_container = st.container(height=600, border=False)
with main_container:
    chat_placeholder = st.empty()
    widget_container = st.container(border=False)

if st.session_state.step == 1:
    with widget_container:
        a.Questions().get_question()
elif st.session_state.step == 9:
    st.success("Success! Your information has been submitted. Someone will be in touch with you and you will recieve an email with a link to complete your application at a later time!")
    t.WelcomeEmail()
    d.Account()
    u.restart_chat()
else:
    chat_container = chat_placeholder.container( height=300,border=False)
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message['role']):
                st.markdown(message['content'])
    with widget_container:
        a.Questions().get_question()


