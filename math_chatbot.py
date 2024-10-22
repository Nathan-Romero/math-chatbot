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

# Loop infinitely for user
while True:    
    
    # Exception handling to handle
    # exceptions at runtime
    try:
        
        # use the microphone as source for input
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            # listens for the user's input 
            audio2 = r.listen(source2)

            # use Google API to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            # print what the user said through their microphone
            print(MyText)

            # send the user's input to the Google API and the model, then grab its output
            response = chat_session.send_message(MyText)
            SpeakText(response.text)

    except sr.RequestError as e:
        print("Could not request results")

    except sr.UnknownValueError:
        print("An unknown error occurred")

# print the response from the math chatbot
print(response.text)