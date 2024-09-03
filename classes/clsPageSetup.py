import streamlit as st
from streamlit_extras.stylable_container import stylable_container as sc
import base64

class PageSetup:
    @staticmethod
    def get_page_styling():
        with open("assets/styling/style.css" ) as css:
            st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    @staticmethod
    def display_background_image():
        # Set the Streamlit image for branding as the background with transparency
        background_image = 'assets/images/main.png'
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.90)), url({background_image});
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        
    @staticmethod
    def display_background_image2():
        # Set the Streamlit image for branding as the background with transparency
        background_image = st.image('assets/images/main.png')
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.9)), url('{background_image}');
                background-size: cover;
                background-attachment: fixed; /* Ensures the background is fixed during scroll */
            }}
            </style>
            """,
            unsafe_allow_html=True
        )


