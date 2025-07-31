import streamlit as st
import subprocess


def ask_llama(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'llama2'],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()

def get_greeting(name, occasion, tone, language):
    prompt = (
        f"Write a {tone.lower()} greeting message for a person named {name} "
        f"for the occasion of {occasion}. Please write the message in {language} only."
    )
    return ask_llama(prompt)

st.set_page_config(page_title="Greeting Generator", page_icon="🎉")
st.title("🎉 Custom Greeting Generator (LLaMA 2 + Ollama)")

name = st.text_input("Enter Name")
occasion = st.text_input("Enter Occasion")

tone = st.selectbox(
    "Choose Tone",
    ["Friendly", "Formal", "Funny", "Emotional", "Motivational"]
)


language = st.selectbox(
    "Choose Language",
    ["English", "Tamil", "Hindi", "French", "Spanish"]
)

if st.button("Generate Greeting"):
    if name and occasion:
        with st.spinner("⏳ Generating your greeting..."):
            greeting = get_greeting(name, occasion, tone, language)
        st.success("💌 Here’s your greeting:")
        st.write(greeting)
    else:
        st.warning("Please enter both name and occasion.")
