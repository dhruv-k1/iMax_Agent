# Utility functions (e.g., logging, data loading)
import logging
import os
import json

from core.constants import LOG_PATH, DATA_PATH, MODEL_PATH

# Ensure directories exist
os.makedirs(LOG_PATH, exist_ok=True)
os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(MODEL_PATH, exist_ok=True) #For saving models

# Logging setup
logging.basicConfig(filename=os.path.join(LOG_PATH, 'agent.log'), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_data(filename):
    """Loads data from a JSON file."""
    try:
        with open(os.path.join(DATA_PATH, filename), 'r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f"Loaded data from {filename}")
        return data
    except FileNotFoundError:
        logger.error(f"Data file not found: {filename}")
        return None
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON in {filename}")
        return None


def save_data(filename, data):
    """Saves data to a JSON file."""
    try:
        with open(os.path.join(DATA_PATH, filename), 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"Saved data to {filename}")
    except Exception as e:
        logger.error(f"Error saving data to {filename}: {e}")
