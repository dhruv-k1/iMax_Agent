# Model loading and inference (LLM, TTS, STT)
from transformers import pipeline 
from core.constants import DEFAULT_TTS_VOICE, DEFAULT_LLM_MODEL, GEMINI_API_KEY
import os
import pyttsx3
import re 

import google.generativeai as genai #Example of a gemini library

class TextToSpeech:
    def __init__(self, voice=DEFAULT_TTS_VOICE):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  
        voices = self.engine.getProperty('voices')
        # Find a suitable voice (this might need OS-specific adjustments)
        for v in voices:
          # print(v.id, v.name, v.languages) # Un comment to check voices
            if voice in v.name.lower():  # Crude voice selection
                self.engine.setProperty('voice', v.id)
                break

    def speak(self, text):
        """Speaks the given text using TTS."""
        # Extract the agent's dialogue (text after "Agent:")
        match = re.search(r"(?i)Agent:([\s\S]*)", text)  # Case-insensitive and handles potential whitespace #Update the search
        if match:
            agent_dialogue = match.group(1).strip()
            # print("AGENTDIAL", agent_dialogue) #THIS WAS ADDED FOR DEBUGGING
            try:
                self.engine.say(agent_dialogue)
                self.engine.runAndWait()
            except Exception as e:
                print(f"TTS Error: {e}") #Print this for debugging
                return False
            return True
        else:
            print("No agent dialogue found in text.") # This will provide some indication that it didn't run.
            return False

class LLM: #Load model based on scenario now
    def __init__(self, model_name=DEFAULT_LLM_MODEL): #Removed scenario
         genai.configure(api_key=GEMINI_API_KEY) # This is a placeholder - configure Gemini access

         self.model = genai.GenerativeModel(model_name) #Load the model

    def generate_response(self, prompt, max_length=50): #This part is the problem, difficult to generate sentences
         """Generates a response using the Gemini model."""
         try:
             response = self.model.generate_content(prompt) #Call Gemini API
             return response.text #Get repsonse
         except Exception as e:
             print(f"LLM Error: {e}")
             return "Mujhe samajh nahi aaya."  # Default response