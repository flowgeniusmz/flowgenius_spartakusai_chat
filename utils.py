import streamlit as st


def page_setup():

    # Set Title
    gradient_text_html = """
    <style>
    .gradient-text {
        font-weight: bold;
        background: -webkit-linear-gradient(left, red, orange);
        background: linear-gradient(to right, red, orange);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 3em;
    }
    </style>
    <div class="gradient-text">SpartakusAI</div>
    """

    st.markdown(gradient_text_html, unsafe_allow_html=True)

def restart_chat():
    resetbtn = st.button("Start Over")
    if resetbtn:
        st.session_state.clear()
        st.rerun()