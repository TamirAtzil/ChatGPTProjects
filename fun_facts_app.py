import openai
import streamlit as st

def get_fun_fact(topic):
<<<<<<< HEAD
    openai.api_key = "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"

    prompt_text = f"Give me a fun fact about {topic}."
=======
    openai.api_key = "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"

    prompt_text = f"Tell me a fun fact about {topic}."
>>>>>>> ea4b659c40d95ede1259481798aab25f65081084

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=prompt_text,
      max_tokens=150
    )

<<<<<<< HEAD
    fun_fact = response.choices[0].text.strip()

    return fun_fact

# Streamlit UI
st.set_page_config(page_title="Farsi-style Fun Facts Generator", layout="centered")
=======
    fact = response.choices[0].text.strip()

    return fact

# Streamlit UI
st.set_page_config(page_title="Fun Fact Generator", layout="centered")
>>>>>>> ea4b659c40d95ede1259481798aab25f65081084

st.markdown("""
    <style>
        .reportview-container {
            background-color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

<<<<<<< HEAD
st.title("Fun Facts Generator 🍎")
st.markdown("""
For those moments when you are lost in life, and you need some Farsi wisdom to make things better
=======
st.title("Fun Fact Generator 🌟")
st.markdown("""
Dive into a world of interesting tidbits on any topic you fancy. Knowledge, after all, is fun!
>>>>>>> ea4b659c40d95ede1259481798aab25f65081084
""")

topic = st.text_input("🔍 Enter a topic for the fun fact:")

if topic:
<<<<<<< HEAD
    with st.spinner("Generating a fun fact for you..."):
        fun_fact = get_fun_fact(topic)
    st.success(fun_fact)
=======
    with st.spinner("Generating an interesting fact..."):
        fact = get_fun_fact(topic)
    st.success(fact)
>>>>>>> ea4b659c40d95ede1259481798aab25f65081084

st.markdown("""
---
**Every day is a school day!** 📘
""")
