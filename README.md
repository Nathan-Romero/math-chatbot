# Math Chatbot

## Overview
This project is a voice-activated **Math Chatbot** that uses Google's Generative AI Model and the Speech Recognition library to process spoken math-related queries and respond to them in real time. The bot converts voice input to text, sends it to the chatbot model for processing, and then reads the response aloud using text-to-speech functionality.

## Key Features
- Converts math-related voice queries to text
- Processes text queries and generates responses using Google's Generative AI Model
- Reads responses aloud using text-to-speech functionality

## Requirements
Before running the code, ensure you have the following installed:

### Software Requirements
- **Google Cloud AI Studio**: Create a project and get access to the API.
- **Python 3.x**: Ensure you have Python installed on your system.

### Python Libraries
**google-generativeai**: To interface with Google's AI chatbot model.
**speechrecognition**: To capture and convert voice input to text.
**pyttsx3**: To convert text responses to speech for voice output.

Install these libraries using the following command:

```bash
pip install google-generativeai speechrecognition pyttsx3
```

### Other Requirements
- **Microphone Access**: Ensure you have a working microphone connected to your system.
- **Internet Connection**: Ensure you have a stable internet connection to access the Google AI model.

## Setup

### Google Cloud AI Studio:
1. Obtain your API key from Google Cloud AI Studio.
2. Replace the placeholder `Enter your key here` in the code with your API key:

```python
genai.configure(api_key="Enter your key here")
```

## Usage
- Ensure your microphone is working properly.
- Run the Python script, and the chatbot will begin listening for voice input.
- Speak your query aloud, and the chatbot will respond with a math-related answer.