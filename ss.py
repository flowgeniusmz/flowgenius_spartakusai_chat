import streamlit as st

def initialize_session_state():
    if "initialized" not in st.session_state:
        st.session_state.initialized = True
        st.session_state.step = 1
        st.session_state.buy_insurance = ""
        st.session_state.insurance_type = ""
        st.session_state.insurance_reason = ""
        st.session_state.effective_date = ""
        st.session_state.effective_date_type = ""
        st.session_state.business_name = ""
        st.session_state.formation_date = ""
        st.session_state.business_address = ""
        st.session_state.business_phone = ""
        st.session_state.business_email = ""
        st.session_state.business_owners = ""
        st.session_state.business_research = ""
        st.session_state.business_website = ""
        st.session_state.username = ""
        st.session_state.password = ""
        st.session_state.question = ""
        st.session_state.response = ""
        st.session_state.questions = ["Are you here to buy insurance?", "Great - what type of insurance are you looking for?", "What is the reason you are purchasing insurance?", "What date do you need the insurance to be effective?", "What is the name of your business?", "Please wait while we research your business", "Please confirm the following information", "Great! Please provide an email address and password to create your account.", "All your information has been submitted! Someone will be in touch with you shortly."]
        st.session_state.responses = []
        st.session_state.messages = []