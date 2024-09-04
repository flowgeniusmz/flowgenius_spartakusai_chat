import streamlit as st
import tools as t

class Questions:
    def __init__(self):
        self.step = st.session_state.step
        
    
    def get_question(self):
        if self.step == 1:
            self.question1()
        elif self.step == 2: 
            self.question2()
        elif self.step == 3: 
            self.question3()
        elif self.step == 4: 
            self.question4()
        elif self.step == 5: 
            self.question5()
        elif self.step == 6: 
            self.question6()
        elif self.step == 7: 
            self.question7()
        elif self.step == 8: 
            self.question8()
        elif self.step == 9: 
            self.question9()

    def callback(self, question: str, response: str, key: str):
        st.session_state.messages.append({"role": "assistant", "content": question})
        st.session_state.messages.append({"role": "user", "content": response})
        st.session_state[key] = st.session_state["_"+key]
        st.session_state.response = st.session_state["_"+key]
        st.session_state.step += 1

    def question1(self):
        question = "Are you here to buy insurance?"
        options = ["Yes", "No"]
        ss_key = "buy_insurance"
        wid_key = "_buy_insurance"
        with st.chat_message("assistant"):
            st.markdown(question)
            widget = st.radio(label="Buy Insurance", options=options, label_visibility="hidden", index=None, horizontal=True, key=wid_key)
            if widget:
                submitbtn = st.button(label="Next", key="submit1", on_click=self.callback, args=[question, widget, ss_key])

    def question2(self):
        question = "What type of insurance are you looking for?"
        options=["General Liability", "Contents", "Contents and Building", "Building Only"]
        ss_key = "insurance_type"
        wid_key = "_insurance_type"
        with st.chat_message("assistant"):
            st.markdown(question)
            widget = st.multiselect(label="Insurance Type", options=options, label_visibility="hidden",  placeholder="Choose one or more options", key=wid_key)
            if widget:
                submitbtn = st.button(label="Next", key="submit2", on_click=self.callback, args=[question, ', '.join(widget), ss_key])

    def question3(self):
        question = "What is the reason for purchasing insurance?"
        options = ["Purchase building", "New purchase", "Expiration of policy", "Starting new business", "Other"]
        ss_key = "insurance_reason"
        wid_key = "_insurance_reason" 
        with st.chat_message("assistant"):
            st.markdown(question)
            widget = st.multiselect(label="Insurance Reason", options=options, label_visibility="hidden",  placeholder="Choose one or more options", key=wid_key)
            if widget:
                submitbtn = st.button(label="Next", key="submit3", on_click=self.callback, args=[question, ', '.join(widget), ss_key])

    def question4(self):
        question = "What date do you need the insurance to be effective?"
        options = ["ASAP", "Specific Date"]
        ss_key = "effective_date"
        wid_key = "_effective_date"
        with st.chat_message("assistant"):
            st.markdown(question)
            widget = st.selectbox(label="Effective Date", options=options, label_visibility="hidden", index=None, key=wid_key, placeholder="Select one of the options")
            if widget == "ASAP":
                submitbtn = st.button(label="Next", key="submit4", on_click=self.callback, args=[question, widget, ss_key])
            elif widget == "Specific Date":
                widget2 = st.date_input(label="Effective Date", key="_effective_date2", label_visibility="hidden", value=None, format="MM/DD/YYYY")
                if widget2 is not None:
                    submitbtn2 = st.button(label="Next", key="submit4a", on_click=self.callback, args=[question, widget2, ss_key])

    def question5(self):
        question = "What is the name of your business"
        options = []
        ss_key = "business_name"
        wid_key = "_business_name"
        with st.chat_message("assistant"):
            st.markdown(question)
            if widget := st.chat_input(placeholder="Enter business name here", key=wid_key):
                #submitbtn = st.button(label="Next", key="submit6", on_click=callback, args=[question, widget, ss_key])
                self.callback(question=question, response=widget, key=ss_key)

    def question6(self):
        question = "Can you confirm the business information is correct?"
        options = []
        ss_key = "business_research"
        wid_key = "_business_research"
        with st.chat_message("assistant"):
            st.markdown("Please wait while I research your business.")
            with st.status(label="Researching...⏳", expanded=False, state="running") as status:
                st.toast(body="Researching...please wait...", icon="⏳")
                st.markdown("Performing research...")
                research = t.BusinessResearch()
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
                submitbtn = st.button(label="Next", key="submit6", on_click=self.callback, args=[question, widget, ss_key])

    def question7(self):
        question = "Can you provide an email for your account?"
        options = []
        ss_key = "username"
        wid_key = "_username"
        with st.chat_message("assistant"):
            st.markdown(question)
            widget = st.text_input(label="Username", key=wid_key, label_visibility="hidden", type="default", placeholder="Please provide a valid email address.")
            if widget:
                submitbtn = st.button(label="Next", key="submit7", on_click=self.callback, args=[question, widget, ss_key])   

    def question8(self):
        question = "Can you please create a password for your account?"
        options = []
        ss_key = "password"
        wid_key = "_password"
        with st.chat_message("assistant"):
            st.markdown(question)
            widget = st.text_input(label="Password", key=wid_key, label_visibility="hidden", type="password", placeholder="Please provide a password.")
            if widget:
                submitbtn = st.button(label="Next", key="submit8", on_click=self.callback, args=[question, widget, ss_key])
        
    def question9(self):
        question = "Success! Your information has been submitted. Someone will be in touch with you and you will recieve an email with a link to complete your application at a later time!"
        options = []
        ss_key = ""
        wid_key = ""
        with st.chat_message("assistant"):
            st.success(question)
        
    
  
  

## CONTROLLER

        