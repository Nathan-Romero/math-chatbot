import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os

genai.configure(api_key="Enter your key here")

# configure the model to dictate chatbot output
generation_config = {
    "temperature": 0.05,
    "top_p": 1,
    "top_k": 64,
    "max_output_tokens": 250,
    "response_mime_type": "text/plain",
    }

# access the model
model = genai.GenerativeModel(
    model_name="tunedModels/mathchatbot-m4ggorut00v8",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

# chat history
chat_session = model.start_chat(
    history=[]
    )

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

