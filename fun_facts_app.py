import openai
import streamlit as st

def get_fun_fact(topic):
    openai.api_key = "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"

    prompt_text = f"Tell me a fun fact about {topic}."

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt_text,
      max_tokens=150
    )

    fact = response.choices[0].text.strip()

    return fact

# Streamlit UI
st.set_page_config(page_title="Fun Fact Generator", layout="centered")

st.markdown("""
    <style>
        .reportview-container {
            background-color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Fun Fact Generator 🌟")
st.markdown("""
Dive into a world of interesting tidbits on any topic you fancy. Knowledge, after all, is fun!
""")

topic = st.text_input("🔍 Enter a topic for the fun fact:")

if topic:
    with st.spinner("Generating an interesting fact..."):
        fact = get_fun_fact(topic)
    st.success(fact)

st.markdown("""
---
**Every day is a school day!** 📘
""")
