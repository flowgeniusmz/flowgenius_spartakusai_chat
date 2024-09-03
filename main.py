import streamlit as st
from classes import clsSessionState as ss, clsBusinessResearch as br, clsEmails as em, clsAccount as ac
from typing import Literal
import time

## PAGE SETUP
st.set_page_config(page_title="SpartakusAI", page_icon="assets/images/icon.png", layout="wide", initial_sidebar_state="collapsed")
title = st.markdown('<span style="font-weight: bold; font-size: 2em; color:#309BA2;">SpartakusAI </span> <span style="font-weight: bold; color:#FCA311; font-size:1.3em;">Inital Chat</span>', unsafe_allow_html=True)
st.divider()

## SESSION STATE
ss.SessionState.get()

## CALLBACK
def append_to_messages(question: str, response: str):
    asst_message = {"role": "assistant", "content": question}
    user_message = {"role": "user", "content": response}
    st.session_state.messages.append(asst_message)
    st.session_state.messages.append(user_message)

def next_step():
    st.session_state.step += 1

def store_value(key):
    st.session_state[key] = st.session_state["_"+key]
    st.session_state.response = st.session_state["_"+key]

def callback(question: str, response: str, key: str):
    append_to_messages(question=question, response=response)
    store_value(key)
    next_step()


## QUESTIONS
#questions = ["Are you here to buy insurance?", "Great - what type of insurance are you looking for?", "What is the reason you are purchasing insurance?", "What date do you need the insurance to be effective?", "What is the name of your business?", "Please wait while we research your business", "Please confirm the following information", "Great! Please provide an email address and password to create your account.", "All your information has been submitted! Someone will be in touch with you shortly."]

def question1():
    question = "Are you here to buy insurance?"
    options = ["Yes", "No"]
    ss_key = "buy_insurance"
    wid_key = "_buy_insurance"
    with st.chat_message("assistant"):
        st.markdown(question)
        widget = st.radio(label="Buy Insurance", options=options, label_visibility="hidden", index=None, horizontal=True, key=wid_key)
        if widget:
            submitbtn = st.button(label="Next", key="submit1", on_click=callback, args=[question, widget, ss_key])
                # st.session_state.buy_insurance = widget
                # st.session_state.response = widget
                # append_to_messages(question=question, response=widget)
                # next_step()

def question2():
    question = "What type of insurance are you looking for?"
    options=["General Liability", "Contents", "Contents and Building", "Building Only"]
    ss_key = "insurance_type"
    wid_key = "_insurance_type"
    with st.chat_message("assistant"):
        st.markdown(question)
        widget = st.multiselect(label="Insurance Type", options=options, label_visibility="hidden",  placeholder="Choose one or more options", key=wid_key)
        if widget:
            submitbtn = st.button(label="Next", key="submit2", on_click=callback, args=[question, ', '.join(widget), ss_key])



def question3():
    question = "What is the reason for purchasing insurance?"
    options = ["Purchase building", "New purchase", "Expiration of policy", "Starting new business", "Other"]
    ss_key = "insurance_reason"
    wid_key = "_insurance_reason" 
    with st.chat_message("assistant"):
        st.markdown(question)
        widget = st.multiselect(label="Insurance Reason", options=options, label_visibility="hidden",  placeholder="Choose one or more options", key=wid_key)
        if widget:
            submitbtn = st.button(label="Next", key="submit3", on_click=callback, args=[question, ', '.join(widget), ss_key])

def question4():
    question = "What date do you need the insurance to be effective?"
    options = ["ASAP", "Specific Date"]
    ss_key = "effective_date"
    wid_key = "_effective_date"
    with st.chat_message("assistant"):
        st.markdown(question)
        widget = st.selectbox(label="Effective Date", options=options, label_visibility="hidden", index=None, key=wid_key, placeholder="Select one of the options")
        if widget == "ASAP":
            submitbtn = st.button(label="Next", key="submit4", on_click=callback, args=[question, widget, ss_key])
        elif widget == "Specific Date":
            widget2 = st.date_input(label="Effective Date", key="_effective_date2", label_visibility="hidden", value=None, format="MM/DD/YYYY")
            if widget2 is not None:
                submitbtn2 = st.button(label="Next", key="submit4a", on_click=callback, args=[question, widget2, ss_key])
    

def question5():
    question = "What is the name of your business"
    options = []
    ss_key = "business_name"
    wid_key = "_business_name"
    with st.chat_message("assistant"):
        st.markdown(question)
        if widget := st.chat_input(placeholder="Enter business name here", key=wid_key):
            #submitbtn = st.button(label="Next", key="submit6", on_click=callback, args=[question, widget, ss_key])
            callback(question=question, response=widget, key=ss_key)

    

def question6():
    question = "Can you confirm the business information is correct?"
    options = []
    ss_key = "business_research"
    wid_key = "_business_research"
    with st.chat_message("assistant"):
        st.markdown("Please wait while I research your business.")
        with st.status(label="Researching...⏳", expanded=False, state="running") as status:
            st.toast(body="Researching...please wait...", icon="⏳")
            st.markdown("Performing research...")
            research = br.BusinessResearch()
            status.update(label="Research completed! ✅", state="complete", expanded=False)
        # research = "Research"
        if research:
            st.markdown(question)
            formation_date = st.text_input(label="Formation Date", key="_formation_date", value=st.session_state.formation_date)
            business_address = st.text_input(label="Business Address", key="_business_address", value=st.session_state.business_address)
            business_owners = st.text_input(label="Business Owners", key="_business_owners", value=st.session_state.business_owners)
            business_email = st.text_input(label="Business Email", key="_business_email", value=st.session_state.business_email)
            business_phone = st.text_input(label="Business Phone", key="_business_phone", value=st.session_state.business_phone)
            business_website = st.text_input(label="Business Website", key="_business_website", value=st.session_state.business_website)
            widget = {"business_email": business_email, "business_phone": business_phone,"business_address": business_address,"business_website": business_website,"business_owners": business_owners,"formation_date": formation_date}
            submitbtn = st.button(label="Next", key="submit6", on_click=callback, args=[question, widget, ss_key])

    

def question7():
    question = "Can you provide an email for your account?"
    options = []
    ss_key = "username"
    wid_key = "_username"
    with st.chat_message("assistant"):
        st.markdown(question)
        widget = st.text_input(label="Username", key=wid_key, label_visibility="hidden", type="default", placeholder="Please provide a valid email address.")
        if widget:
            submitbtn = st.button(label="Next", key="submit7", on_click=callback, args=[question, widget, ss_key])
       
    

def question8():
    question = "Can you please create a password for your account?"
    options = []
    ss_key = "password"
    wid_key = "_password"
    with st.chat_message("assistant"):
        st.markdown(question)
        widget = st.text_input(label="Password", key=wid_key, label_visibility="hidden", type="password", placeholder="Please provide a password.")
        if widget:
            submitbtn = st.button(label="Next", key="submit8", on_click=callback, args=[question, widget, ss_key])
       
    

def question9():
    question = "Success! Your information has been submitted. Someone will be in touch with you and you will recieve an email with a link to complete your application at a later time!"
    options = []
    ss_key = ""
    wid_key = ""
    with st.chat_message("assistant"):
        st.success(question)
        em.WelcomeEmail()
    
  
  

## CONTROLLER
def get_question(step: int):
    if step == 1:
        question1()
    elif step == 2: 
        question2()
    elif step == 3: 
        question3()
    elif step == 4: 
        question4()
    elif step == 5: 
        question5()
    elif step == 6: 
        question6()
    elif step == 7: 
        question7()
    elif step == 8: 
        question8()
    elif step == 9: 
        ac.Account()
        question9()

## DISPLAY SETUP
chat_container = st.empty()
if st.session_state.step >= 2 and st.session_state.step <= 8:
    chat = chat_container.container(height=400, border=True)
    with chat:
        for message in st.session_state.messages:
            with st.chat_message(message['role']):
                st.markdown(message['content'])

widget_container = st.container(border=True)

## DISPLAY - CHAT
# with chat_container:
#     for message in st.session_state.messages:
#         with st.chat_message(message['role']):
#             st.markdown(message['content'])

## DISPLAY - PROMPT
with widget_container:
    get_question(step=st.session_state.step)
