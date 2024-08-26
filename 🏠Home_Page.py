from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
import streamlit as st

load_dotenv(find_dotenv())


def main():
    st.set_page_config(page_title="Text Chat", page_icon="🤖")
    st.header("HF Chatter-Box")
    st.title("💬 Chatbot")

    st.markdown(
        """
        This is a demo of a simple chatbot using the DialoGPT model from Hugging Face.
        
        **👈 Select a model from the sidebar** to see some examples
        
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - More information about [DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium)
        
    """
    )


if __name__ == "__main__":
    main()
