import streamlit as st
from openai import OpenAI, AsyncOpenAI
from tavily import TavilyClient, AsyncTavilyClient
from pydantic import BaseModel
from googlemaps import places, Client
from googlesearch import search
import requests

## CLASSES
#### Class used in openai completion structured output
class BusinessInfo(BaseModel):
    business_name: str
    business_address: str
    business_phone: str
    business_owners: str
    business_website: str
    business_formation_date: str
    business_email: str

#### Business Research used to perform  research
class BusinessResearch:
    def __init__(self):
        self.init_all()
        self.run_tools()
        self.oai_business_info()
        self.set_values()
    
    def init_all(self):
        self._init_clients()
        self._init_values()
        self._init_queries()

    def _init_values(self):
        self.business_name = st.session_state.business_name
    
    def _init_queries(self):
        self.query1 = f"What is the date of formation, ownership details / owners, business address, and website url for the business {self.business_name}?"
    
    def _init_clients(self):
        self.oaiClient = OpenAI(api_key=st.secrets.openai.api_key)
        self.oaiClienta = AsyncOpenAI(api_key=st.secrets.openai.api_key)
        self.tavClient = TavilyClient(api_key=st.secrets.tavily.api_key)
        self.tavClienta = AsyncOpenAI(api_key=st.secrets.tavily.api_key)
        self.gooClient = Client(key=st.secrets.google.maps_api_key)
    
    def run_tools(self):
        self._tool_internet_research()
        self._tool_internet_search()
        self._tool_places_search()
        self.compiled_tool_results = "\n\n".join([self.internet_research_results_string, self.internet_search_results_string, self.places_search_results_string])

    def _tool_internet_search(self):
        self.internet_search_results = search(term=self.query1, advanced=True, num_results=10)
        self.internet_search_results_list = list(self.internet_search_results)
        self.internet_search_results_string = f"Answer: {self.internet_search_results_list}"
        print(self.internet_search_results_string)

    def _tool_internet_research(self):
        self.internet_research_results = self.tavClient.search(query=self.query1, search_depth="advanced", max_results=5, include_answer=True, include_raw_content=True)
        self.internet_research_results_string = f"Answer: {self.internet_research_results.get('answer', '')}\nRaw Content: {self.internet_research_results.get('raw_content', '')}"
        print(self.internet_research_results_string)

    def _tool_places_search(self):
        self.places_search_results = places.places(client=self.gooClient, query=self.business_name, region="US")
        self.places_search_results_string = f"Answer: {self.places_search_results}"
        #places.place()
        print(self.places_search_results_string)

    def oai_business_info(self):
        self._oai_set_model()
        self._oai_set_messages()
        self._oai_get_completion()

    def _oai_get_completion(self):
        self.completion_response = self.oaiClient.beta.chat.completions.parse(messages=self.messages, model=self.model, response_format=BusinessInfo)
        self.completion_message = self.completion_response.choices[0].message
        self.completion_message_parsed = self.completion_message.parsed  # Corrected variable name
        print(self.completion_message_parsed)

    def _oai_set_messages(self):
        self.system_message = {"role": "system", "content": "You are an expert at structured data extraction. You will be given unstructured text from a research paper and should convert it into the given structure."}
        self.user_message = {"role": "user", "content": f"{self.compiled_tool_results}"}
        self.messages = [self.system_message, self.user_message]
    
    def _oai_set_model(self):
        self.model = "gpt-4o-2024-08-06"

    def set_values(self):
        self._set_values_individual()
        self._set_values_session()

    def _set_values_individual(self):
        self.business_phone = self.completion_message_parsed.business_phone
        self.business_address = self.completion_message_parsed.business_address
        self.business_owners = self.completion_message_parsed.business_owners
        self.business_website = self.completion_message_parsed.business_website
        self.business_formation_date = self.completion_message_parsed.business_formation_date
        self.business_email = self.completion_message_parsed.business_email
        self.business_research = self.completion_message_parsed
    
    def _set_values_session(self):
        st.session_state.business_phone = self.completion_message_parsed.business_phone
        st.session_state.business_address = self.completion_message_parsed.business_address
        st.session_state.business_owners = self.completion_message_parsed.business_owners
        st.session_state.business_website = self.completion_message_parsed.business_website
        st.session_state.formation_date = self.completion_message_parsed.business_formation_date
        st.session_state.business_email = self.completion_message_parsed.business_email
        st.session_state.business_research = self.completion_message_parsed








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
        self.username = st.session_state.username
        self.password = st.session_state.password
        self.payload = {"username": self.username, "password": self.password}

    def send_request(self):
        self.response = requests.post(url=self.url, json=self.payload)
        self.response_text = self.response.text
        #self.response_json = self.response.json()
        #print(self.response_json)



