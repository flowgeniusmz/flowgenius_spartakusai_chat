import streamlit as st
from supabase import create_client, Client

class Account:
    def __init__(self):
        self.init_client()
        self.get_data()
        self.add_account()

    def init_client(self):
        self.client = create_client(supabase_key=st.secrets.supabase_spartakus.api_key_admin, supabase_url=st.secrets.supabase_spartakus.url)
    
    def get_data(self):
        self.data = {
            "username": st.session_state.username,
            "password": st.session_state.password,
            "business_name": st.session_state.business_name,
            "business_email": st.session_state.business_email,
            "business_phone": st.session_state.business_phone,
            "business_address": st.session_state.business_address,
            "business_website": st.session_state.business_website,
            "business_owners": st.session_state.business_owners,
            "formation_date": st.session_state.formation_date,
            "effective_date": st.session_state.effective_date,
            "business_research": st.session_state.business_research,
            "buy_insurance": st.session_state.buy_insurance,
            "insurance_types": ', '.join(st.session_state.insurance_type),  # Convert list to comma-separated string
            "insurance_reasons":', '.join(st.session_state.insurance_reason) # Convert list to comma-separated string
        }

    def add_account(self):
        self.response = self.client.table("users2").insert(self.data).execute()
        self.response_data = self.response.data
        print(self.response_data)

    def util_flatten_list(nested_list):
        """Flatten a list of lists into a single list."""
        return [item for sublist in nested_list for item in sublist]