import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key is None:
    api_key = st.secrets["GROQ_API_KEY"]

MODEL = os.getenv("MODEL")

if MODEL is None:
    MODEL = st.secrets.get("MODEL", "llama-3.3-70b-versatile")

client = Groq(api_key=api_key)


def ask_llm(system_prompt, user_prompt):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content