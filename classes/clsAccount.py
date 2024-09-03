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


# supaClient = create_client(supabase_key=st.secrets.supabase_spartakus.api_key_admin, supabase_url=st.secrets.supabase_spartakus.url)

# def flatten_list(nested_list):
#     """Flatten a list of lists into a single list."""
#     return [item for sublist in nested_list for item in sublist]

# def add_data(username, password, business_name, business_email, business_phone, business_address, business_website, formation_date, insurance_types, insurance_reasons, buy_insurance, business_owners, business_research, effective_date):
#     # Flatten the lists if they are nested
#     insurance_types = flatten_list(insurance_types) if any(isinstance(i, list) for i in insurance_types) else insurance_types
#     insurance_reasons = flatten_list(insurance_reasons) if any(isinstance(i, list) for i in insurance_reasons) else insurance_reasons

#     data = {
#         "username": username,
#         "password": password,
#         "business_name": business_name,
#         "business_email": business_email,
#         "business_phone": business_phone,
#         "business_address": business_address,
#         "business_website": business_website,
#         "business_owners": business_owners,
#         "formation_date": formation_date,
#         "effective_date": effective_date,
#         "business_research": business_research,
#         "buy_insurance": buy_insurance,
#         "insurance_types": ', '.join(insurance_types),  # Convert list to comma-separated string
#         "insurance_reasons": ', '.join(insurance_reasons)  # Convert list to comma-separated string
#     }
#     response = supaClient.table("users2").insert(data).execute()
#     response_data = response.data
#     print(response_data)
#     return response_data

# # Sample data
# username = "test_user"
# password = "securepassword"
# business_name = "Test Business"
# business_email = "test@example.com"
# business_phone = "123-456-7890"
# business_address = "123 Test Street"
# business_website = "https://testbusiness.com"
# formation_date = "2024-01-01"
# insurance_types = ["General Liability"]  # Ensure this is a flat list
# insurance_reasons = ["New purchase"]  # Ensure this is a flat list
# buy_insurance = "Yes"
# business_owners = "John Doe"
# business_research = "Some research data"
# effective_date = "2024-02-01"

# # Add data
# add = add_data(username=username, password=password, business_address=business_address, business_owners=business_owners, business_name=business_name, business_email=business_email, business_phone=business_phone, business_website=business_website, formation_date=formation_date, effective_date=effective_date, insurance_reasons=insurance_reasons, insurance_types=insurance_types, buy_insurance=buy_insurance, business_research=business_research)

# print(add)
