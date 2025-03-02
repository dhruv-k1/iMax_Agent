# --- agent.py ---
# Core logic for the AI agent (dialogue management, tool integration)

from llm.models import LLM, TextToSpeech
from prompts.prompts import get_erp_demo_prompt, get_interview_prompt, get_payment_followup_prompt
from core.utils import logger
from knowledge_base.kb_gen import generate_dynamic_knowledge_base

class Agent:
    def __init__(self, scenario, customer_name = None, job_title = None):
        self.scenario = scenario
        self.llm = LLM()  # No longer needs scenario
        self.tts = TextToSpeech()
        self.conversation_history = []
        self.customer_name = customer_name
        self.job_title = job_title
        self.knowledge = self._load_knowledge()
        self.prompt_function = self._select_prompt_function()
        self.is_running = True

    def _load_knowledge(self):
        #Infer agent gender from customer_name and create dynamic knowlegde base
        if self.scenario == "interview":
             return generate_dynamic_knowledge_base(self.scenario, customer_name=self.customer_name, job_title=self.job_title, company_name = "iMax")
        else:
            return generate_dynamic_knowledge_base(self.scenario, customer_name=self.customer_name, company_name = "iMax")

    def _select_prompt_function(self):
        if self.scenario == "erp_demo":
            return get_erp_demo_prompt
        elif self.scenario == "interview":
            return get_interview_prompt
        elif self.scenario == "payment_followup":
            return get_payment_followup_prompt
        else:
            logger.error("Invalid scenario selected.")
            raise ValueError("Invalid scenario")

    def start_conversation(self, customer_name, invoice_number=None, job_title=None):
        """Starts a new conversation."""
        self.conversation_history = []  # Clear previous history

        # Generate initial prompt
        if self.scenario == "erp_demo":
            prompt = self.prompt_function(customer_name, self.knowledge.get("product_name", "ERP System"), self.knowledge)
        elif self.scenario == "interview":
            prompt = self.prompt_function(customer_name, self.knowledge["job_title"], self.knowledge)  #Pass the attribute not the parameter
        elif self.scenario == "payment_followup":
            prompt = self.prompt_function(customer_name, invoice_number, self.knowledge)
        else:
            raise ValueError("Invalid scenario")
        return prompt

    def get_agent_response(self, prompt, user_input):
        """Generates an agent response using the LLM."""
        # Update conversation history
        self.conversation_history.append({"speaker": "Customer", "text": user_input})
        combined_prompt = prompt + user_input + "\nAgent: "  # Create combined prompt

        response = self.llm.generate_response(combined_prompt) #Call LLM

        self.conversation_history.append({"speaker": "Agent", "text": response})
        return response # Only return the generated response

    def speak(self, text):
        """Speaks the given text using TTS."""
        return self.tts.speak(text)

    def end_conversation(self):
        """Ends the current conversation."""
        self.is_running = False
        logger.info("Conversation ended.")