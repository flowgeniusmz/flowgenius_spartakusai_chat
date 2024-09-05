import streamlit as st
from htbuilder import div, p, styles

def get_footer():
    style = """
    <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp { bottom: 60px; }
        /* Hide Streamlit's "Built with Streamlit" footer */
        .viewerBadge_container__1QSob {visibility: hidden;}
        .embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
    </style>
    """

    style_div = styles(
        position="fixed",
        right=0,
        bottom=0,
        margin="0 15px 0 0",
        text_align="center",
        opacity=0.5,
    )

    body = p()
    foot = div(
        style=style_div
    )(
        body
    )

    st.markdown(style, unsafe_allow_html=True)
    st.markdown(str(foot), unsafe_allow_html=True)
