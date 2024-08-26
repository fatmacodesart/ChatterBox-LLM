from dotenv import load_dotenv, find_dotenv
from transformers import pipeline
import streamlit as st

load_dotenv(find_dotenv())


def chat(messages):

    text_gen = pipeline(

        "text-generation", model="microsoft/DialoGPT-medium",
        device=0,
        temperature=0.7,
        top_k=50,
        top_p=0.9,
        pad_token_id=50256)
    text = text_gen(messages)
    return text


def main():
    st.set_page_config(page_title="Text Chat", page_icon="🤖")

    st.title("💬 DialoGPT ChatterBox")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []
        st.chat_message("assistant").write(
            "Hello! I'm Chatter-Box. How can I help you!")

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = chat([st.session_state.messages[-1]])
        msg = response[0]["generated_text"][1]["content"]
        st.session_state.messages.append(
            {"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)


if __name__ == "__main__":
    main()
