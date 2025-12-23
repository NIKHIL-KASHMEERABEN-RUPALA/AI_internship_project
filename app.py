import streamlit as st
import requests

# Define the endpoint for Rasa API
RASA_URL = 'http://localhost:5005/webhooks/rest/webhook'

# Streamlit page setup
st.title("AI Career Counsellor")
st.write("Tell me about your interests, and I'll help you choose a career path!")

# Input field for user message
user_input = st.text_input("Your Message:")

if user_input:
    # Send the message to the Rasa server
    response = requests.post(RASA_URL, json={"sender": "user", "message": user_input})
    
    # Display the chatbot response
    for message in response.json():
        st.write(message['text'])
