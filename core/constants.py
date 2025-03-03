import os
from dotenv import load_dotenv
load_dotenv()

# Centralized configuration and constants
GEMINI_API_KEY = os.getenv('MY_KEY')
HINGLISH_LANGUAGE_CODE = "hin-eng"  # Standard code for Hinglish
DEFAULT_TTS_VOICE = "male"  # Or "female" for default TTS voice
DEFAULT_STT_MODEL = "facebook/wav2vec2-base-960h" #Or other suitable free STT models
DEFAULT_LLM_MODEL = "gemini-2.0-flash" # This will be the base model

# Paths for storing data and models
DATA_PATH = "data/"
MODEL_PATH = "models/"
LOG_PATH = "logs/"

# Scenario-specific model paths
# ERP_DEMO_MODEL_PATH = os.path.join(MODEL_PATH, "erp_demo_finetuned")
# INTERVIEW_MODEL_PATH = os.path.join(MODEL_PATH, "interview_finetuned")
# PAYMENT_MODEL_PATH = os.path.join(MODEL_PATH, "payment_finetuned")
