import streamlit as st

st.set_page_config(
    page_title="GPU Recommender",
    page_icon="🎮",
    layout="wide"
)

st.title("GPU Recommender")
st.write("Welcome to the GPU Recommender app!")

st.markdown("""
## Features:
- **Main Page**: Welcome and overview
- **Gpu Recommender**: Find the best GPU for your needs

Use the sidebar to navigate between pages.
""")

st.info("👈 Select a page from the sidebar to get started!")