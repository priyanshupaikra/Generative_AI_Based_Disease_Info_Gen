from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()  # helps to load all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) #API key of Gemini

# Function to use Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

#Initialize our Streamlit app
# Dedails What My Generative AI Application Generate
st.set_page_config(page_title="AI-Powered Health Information")
st.header("Gemini Health Disease Information Generator")
st.write("This is Generative AI based automatically Disease Information generating System")
st.write("Where you get Information about:")
st.write("1. Symptoms of the Disease")
st.write("2. Steps to take Precautions")
st.write("3. Solution of the Disease Both Medical and Home")
st.write("4. Reaction of disease on body step by step if you not taken any step with examples")

input_text = st.text_input("Name of the Disease:")
submit = st.button("Ask AI")

if submit and input_text:
    # Construct the query with additional text with written disease name
    query1 = f"{input_text}. Give its 5 symptoms, steps to take precautions and solution both medical and home. Explain it's all step by step reaction in body with all stages. If possible give examples"
    response = get_gemini_response(query1)

    # Initialize session state for chat history if it doesn't exist
    if 'chats' not in st.session_state:
        st.session_state['chats'] = []

    # Add user query and response to session state chat history
    st.session_state['chats'].append(("You", input_text))
    st.subheader("About the Disease")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chats'].append(("Bot", chunk.text))