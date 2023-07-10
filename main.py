import streamlit as st

from lib.service_setup import openai_setup
from lib.ui_components import render_logo_header, render_chat_example, render_analysis
from lib.model import GPTReviewer, Analyzer

from configs import ENTITIES_TO_EXTRACT, AZURE_OPENAI_GPT_DEPLOYMENT
from lib.statics import CHAT_EXAMPLE


def main():
    st.set_page_config(layout="wide")
    openai_setup()

    render_logo_header("Review text with the power of GPT")
    st.markdown(
        "##### Within this demo you can pass chat between user and bot regarding their flight to GPT to extract entities."
    )
    st.markdown("<br>", unsafe_allow_html=True)
    render_chat_example(CHAT_EXAMPLE)

    st.markdown("<br>", unsafe_allow_html=True)
    text_input = st.text_area("Enter text here", height=200)
    submit_button = st.button("Submit")

    # Show the results in the table.
    if submit_button:
        reviewer = GPTReviewer(ENTITIES_TO_EXTRACT, AZURE_OPENAI_GPT_DEPLOYMENT)

        df = reviewer.text_analysis(text_input)

        render_analysis(df, Analyzer(df))


if __name__ == "__main__":
    main()
