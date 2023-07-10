import streamlit as st
from streamlit_extras.colored_header import colored_header
from PIL import Image


def render_logo_header(header_title):
    col1, col2 = st.columns([0.05, 0.95])
    col1.image(Image.open("lib/logos/porini_logo.png"), use_column_width="always")
    with col2:
        colored_header(label=header_title, description=" ", color_name="blue-100")


def render_chat_example(example):
    st.markdown("##### Example of the chat:")
    st.markdown("<br>".join(example.split("\n")), unsafe_allow_html=True)


def render_analysis(df, analyzer):
    st.markdown(f"<p style='text-align: center;'>Table of Extracted Entities</p>", unsafe_allow_html=True)
    st.columns([0.2, 0.6, 0.2])[1].write(df)
    st.markdown(f"<p style='text-align: center;'>Visualizations of Entity Analysis</p>", unsafe_allow_html=True)

    analyzer.process_data()

    with st.columns([0.05, 0.9, 0.05])[1]:
        _, col2, _ = st.columns([0.15, 0.7, 0.15])
        col2.pyplot(analyzer.word_cloud())

        col1, col2, col3 = st.columns([0.33, 0.33, 0.33])
        col1.pyplot(analyzer.flights_by_departure())
        col2.pyplot(analyzer.flights_by_destination())
        col3.pyplot(analyzer.popular_cities())

        col1, col2 = st.columns([0.5, 0.5])
        col1.pyplot(analyzer.animals_types())
        col2.pyplot(analyzer.pie_with_animals())

        _, col2, _ = st.columns([0.15, 0.7, 0.15])
        col2.pyplot(analyzer.plot_2_figures())
