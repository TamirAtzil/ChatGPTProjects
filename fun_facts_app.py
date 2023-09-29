import openai
import streamlit as st

def get_dad_joke(topic):
    openai.api_key = "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"

    prompt_text = f"Tell me a dad joke about {topic}."

    response = openai.Completion.create(
      model="text-davinci-002",  
      prompt=prompt_text,
      max_tokens=150
    )

    joke = response.choices[0].text.strip()

    return joke

# Streamlit UI
st.set_page_config(page_title="Apple-style Dad Joke Generator", layout="centered")

st.markdown("""
    <style>
        .reportview-container {
            background-color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Dad Joke Generator 🍎")
st.markdown("""
For those moments when you need a joke with a specific theme, inspired by the sleek design of Apple.
""")

topic = st.text_input("🔍 Enter a topic for the dad joke:")

if topic:
    with st.spinner("Generating a sleek joke..."):
        joke = get_dad_joke(topic)
    st.success(joke)

st.markdown("""
---
**Enjoy the fun, share the joy!** 🎉
""")
