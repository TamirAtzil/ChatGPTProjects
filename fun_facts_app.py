import openai
import streamlit as st

def get_fun_fact(topic):
    openai.api_key = "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"

    prompt_text = f"Give me a fun fact about {topic}."

    response = openai.Completion.create(
      model="text-davinci-002",  
      prompt=prompt_text,
      max_tokens=150
    )

    fun_fact = response.choices[0].text.strip()

    return fun_fact

# Streamlit UI
st.set_page_config(page_title="Farsi-style Fun Facts Generator", layout="centered")

st.markdown("""
    <style>
        .reportview-container {
            background-color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Fun Facts Generator 🍎")
st.markdown("""
For those moments when you are lost in life, and you need some Farsi wisdom to make things better
""")

topic = st.text_input("🔍 Enter a topic for the fun fact:")

if topic:
    with st.spinner("Generating a fun fact for you..."):
        fun_fact = get_fun_fact(topic)
    st.success(fun_fact)

st.markdown("""
---
**Enjoy the fun, share the joy!** 🎉
""")
