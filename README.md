# AI-Powered Sales Co-Pilot

Transform generic, robotic sales outreach into personalized, highly human, and thoughtful engagements. Built as an MVP for the **Google PromptWars x Ascent Challenge**.

This extremely lightweight application uses the **Google Gemini API** to analyze prospects, optimize outreach messages, and strategize follow-ups.

## Features (3 Modules)

1. **Prospect Research Engine (Pre-Pitch)**
   - Scrape and analyze a URL (or pasted text) to extract core themes, recent news, and personal interests.
   - Outputs highly personalized talking points.

2. **The Message Optimizer (The Pitch)**
   - Input a generic sales pitch and prospect insights.
   - Adjust the tone using a slider.
   - Outputs a deeply personal, human-sounding outreach message that converts.

3. **Response Analyzer & Follow-Up Strategist (Post-Pitch)**
   - Paste a prospect's reply.
   - The AI evaluates sentiment, intent, and buying signals.
   - Suggests the optimal next move, channel, and provides a drafted response.

## Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Install Dependencies
It's recommended (and required on macOS) to use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Environment Variables
You need a Google Gemini API Key. Get one from Google AI Studio.
Create a `.env` file in the root directory (or rename `.env.example` to `.env`) and add your key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

*Alternatively, you can input the API key directly in the Streamlit app sidebar.*

### 4. Run the Application
Ensure your virtual environment is activated, then run the Streamlit app locally:

```bash
source venv/bin/activate
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.
