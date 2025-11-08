import json
import os

DATA_DIR = "data"
TONERS_FILE = os.path.join(DATA_DIR, "toners.json")
SUBSTRATES_FILE = os.path.join(DATA_DIR, "substrates.json")
TARGETS_FILE = os.path.join(DATA_DIR, "targets.json")

def ensure_data_dir():
    """Ensures the data directory exists."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_data(file_path):
    """Loads data from a JSON file."""
    ensure_data_dir()
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_data(file_path, data):
    """Saves data to a JSON file."""
    ensure_data_dir()
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage:
# toner_inventory = load_data(TONERS_FILE)
# save_data(TONERS_FILE, toner_inventory)