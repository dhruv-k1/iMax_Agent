import time
from agent.agent import Agent
from core.utils import logger, load_data
import os
from core.constants import DEFAULT_LLM_MODEL
import speech_recognition as sr

def main():
    """Main function to run the AI agent."""

    scenario = input("Enter scenario (erp_demo, interview, payment_followup): ").strip().lower()
    if scenario not in ["erp_demo", "interview", "payment_followup"]:
        print("Invalid scenario.")
        return

    customer_name = input("Enter customer name: ").strip()
    invoice_number = None
    job_title = None

    if scenario == "payment_followup":
        invoice_number = input("Enter invoice number: ").strip()
    elif scenario == "interview":
        job_title = input("Enter job title: ").strip()

    agent = Agent(scenario, customer_name, job_title) 

    try:
        prompt = agent.start_conversation(customer_name, invoice_number, job_title)
        print("Agent:" + prompt) #Initial prompt
        agent.speak(prompt) 

        while agent.is_running: #Keep the conversation running

            # Obtain audio from the microphone
            r = sr.Recognizer()
            with sr.Microphone(device_index=1) as source:  
                print("Awaiting your response...")
                r.adjust_for_ambient_noise(source) #Listen to ambient noise.

                
                try:
                    audio = r.listen(source, phrase_time_limit=None, timeout=5) #Pause 5 second before timeout # Added default
                except sr.WaitTimeoutError:
                    print("No audio received. Continuing...")
                    continue 
                except Exception as e:
                    print(f"Audio Exception occurred, defaulting {e}")
                    continue

            # Recognize speech using Google Speech Recognition
            try:
                user_input = r.recognize_google(audio)
                print("Google Speech Recognition thinks you said " + user_input)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                user_input = "" #Default input
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                user_input = "" #Default Input

            if user_input.lower() in ["ok bye", "bye", "alright bye", "thank you bye"]: #Check for exiting
                agent.end_conversation()
                print("Call ended.")
                break # Break out of the loop. Make sure all the variables are set up correctly

            response = agent.get_agent_response(prompt, user_input) 
            print(f"Agent: {response}")
            agent.speak(response) 

            #Update the prompt (this simple version just keeps appending the user input and agent responses)
            prompt += user_input + "\nAgent: " + response

            time.sleep(1) # Add a small delay
        print("Conversation ended.") #Print this if it exits after max.

    except Exception as e:
        logger.exception("An error occurred during the conversation.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()