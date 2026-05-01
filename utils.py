import os
import json
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Load Prompts
try:
    with open("prompts.json", "r") as f:
        PROMPTS = json.load(f)
except Exception as e:
    PROMPTS = {}

def get_gemini_model(model_name="gemini-1.5-pro"):
    """Returns a configured Gemini model instance."""
    # Using gemini-1.5-pro or gemini-1.5-flash for the tasks
    return genai.GenerativeModel(model_name)

def fetch_url_content(url):
    """Fetches and extracts text from a given URL."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()
            
        # Get text
        text = soup.get_text(separator=' ', strip=True)
        return text
    except Exception as e:
        return f"Error fetching URL: {str(e)}"

def generate_module_a_insights(input_text, is_url=False):
    """Generates insights for Module A (Pre-Pitch)."""
    if not API_KEY:
        return "Error: Gemini API Key not configured."
    
    content = fetch_url_content(input_text) if is_url else input_text
    
    if content.startswith("Error fetching URL:"):
        return content
        
    model = get_gemini_model()
    prompt = f"{PROMPTS.get('module_a_research', '')}\n\nHere is the information about the prospect:\n{content}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"

def optimize_module_b_message(generic_pitch, insights, tone="Direct & Professional"):
    """Optimizes the sales pitch for Module B."""
    if not API_KEY:
        return "Error: Gemini API Key not configured."
        
    model = get_gemini_model()
    prompt = f"{PROMPTS.get('module_b_optimizer', '')}\n\n"
    prompt += f"Target Tone: {tone}\n\n"
    prompt += f"Prospect Insights:\n{insights}\n\n"
    prompt += f"Generic Pitch to rewrite:\n{generic_pitch}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"

def analyze_module_c_response(prospect_reply):
    """Analyzes prospect response and suggests next moves for Module C."""
    if not API_KEY:
        return "Error: Gemini API Key not configured."
        
    model = get_gemini_model()
    prompt = f"{PROMPTS.get('module_c_analyzer', '')}\n\nProspect's Reply:\n{prospect_reply}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"
