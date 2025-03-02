# iMax_Agent
# Hinglish AI Cold Calling Agent

## Project Description

This project implements an AI agent capable of conducting personalized and human-like cold calls in Hinglish for three business objectives: Demo Scheduling for an ERP system, Candidate Interviewing for initial screening, and Payment/Order Follow-up. The agent is designed to understand context, personalize interactions, and exhibit conversational abilities in Hinglish.  It leverages the Google Gemini API for natural language understanding and generation, Google Speech Recognition for speech-to-text, and pyttsx3 for text-to-speech.

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Make sure a `requirements.txt` file is present in your repo.  It should include libraries like `google-generativeai`, `SpeechRecognition`, `pyttsx3`, etc.)

3.  **Set Gemini API Key:**
    *   Obtain an API key from the Google AI Studio: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
    *   Set the API key as an environment variable named `GOOGLE_API_KEY`. This can be done in several ways:
        *   **(Recommended) Using `.env` file:** Create a file named `.env` in the project root directory and add the following line:
            ```
            GOOGLE_API_KEY=YOUR_API_KEY
            ```
            You'll need to install the `python-dotenv` package (`pip install python-dotenv`) and load the environment variables in `main.py` at the beginning of the script.
            ```python
            from dotenv import load_dotenv
            import os

            load_dotenv()
            gemini_api_key = os.getenv("GOOGLE_API_KEY")
            ```
        *   **Directly in the terminal (for Linux/macOS):**
            ```bash
            export GOOGLE_API_KEY=YOUR_API_KEY
            ```
        *   **Directly in the terminal (for Windows):**
            ```powershell
            $env:GOOGLE_API_KEY="YOUR_API_KEY"
            ```
        *   **Hardcoding (Not recommended for security reasons):** Directly adding your API key to the Python script.

4.  **Run the Agent:**
    ```bash
    python main.py
    ```
    Follow the on-screen prompts to interact with the AI agent and select the desired cold calling scenario.

## Models and Datasets Used

*   **LLM:** Google Gemini API (Pro model used for conversational AI capabilities). No specific datasets were used to fine-tune the model due to time constraints. Prompts were carefully engineered to guide the LLM's responses.
*   **Speech-to-Text (STT):** Google Speech Recognition API (part of the `SpeechRecognition` library) - Leveraged for transcribing user speech in Hinglish.
*   **Text-to-Speech (TTS):** `pyttsx3` - Used for generating speech output.  While functional, this is an area for improvement as the Hinglish pronunciation and accent could be significantly better.

## Agent Architecture and Key Components

The agent architecture follows a basic structure involving STT, LLM interaction, and TTS:

1.  **Speech-to-Text (STT):** Captures the user's voice input and converts it to text.
2.  **LLM (Gemini API):** Receives the text input, processes it based on the current conversation state and pre-defined prompts, and generates a response.
3.  **Text-to-Speech (TTS):** Converts the LLM's text response into audible speech using `pyttsx3`.
4.  **Conversation State Management:**  Basic state management is implemented to track the conversation's progress.  This involves tracking the purpose of the call (demo scheduling, interview, payment follow-up) and key information gathered during the interaction.
5.  **Prompt Engineering:**  Specifically crafted prompts are used for each scenario to guide the LLM's responses and ensure they are relevant, personalized, and in natural Hinglish.

## Demonstration Video

[Link to LOOM (or similar platform) Demonstration Video](YOUR_LOOM_VIDEO_LINK_HERE)

## Completed, Partially Implemented, and Unfinished Features

**Completed:**

*   Basic setup and environment configuration.
*   Integration with Gemini API for LLM functionality.
*   Implementation of speech-to-text using Google Speech Recognition.
*   Implementation of text-to-speech using `pyttsx3`.
*   Core logic for the three cold-calling scenarios (demo scheduling, candidate interviewing, and payment/order follow-up).
*   Basic conversation state management.
*   Demonstration video creation.
*   Basic error handling.

**Partially Implemented:**

*   **Hinglish Handling:** While the agent can generate responses in Hinglish, the quality and naturalness of the Hinglish can be improved with better data and model fine-tuning. The current implementation primarily relies on prompt engineering.
*   **Conversation State Management:** The current implementation is rudimentary. A more robust system would be beneficial for tracking more complex conversations.
*   **API Integrations:** While the design considered potential API integrations (e.g., Calendar API), these were not implemented due to time constraints.
*   **Evaluation & Refinement:**  Initial testing was conducted, but more thorough evaluation and refinement are required to optimize the agent's performance.

**Unfinished:**

*   **LLM Fine-tuning:**  Due to the limited time and the difficulty of finding/creating suitable Hinglish datasets, the LLM was not fine-tuned.
*   **Advanced Error Handling:** The current error handling is basic and could be significantly improved to handle a wider range of potential issues.
*   **Enhanced TTS:**  A more sophisticated TTS solution with better Hinglish pronunciation and a more natural-sounding voice was not implemented. Services like Google Cloud Text-to-Speech or similar offerings specifically designed for Indian languages would improve the experience.

## Challenges Faced

*   **Data Scarcity for Fine-Tuning:**  A major challenge was the lack of readily available, high-quality datasets for fine-tuning the LLM specifically for Hinglish cold-calling scenarios. Creating such datasets within the given timeframe was not feasible.
*   **Suboptimal TTS Quality:** The `pyttsx3` library, while functional, provides a subpar experience for Hinglish text-to-speech. The pronunciation and accent are not ideal, and a more advanced TTS solution would be necessary for a truly natural and engaging conversation.
*   **Time Constraints:**  The 8-hour time limit significantly impacted the depth of implementation and refinement possible. Many planned features, such as API integrations and comprehensive error handling, were either partially implemented or not implemented at all.
