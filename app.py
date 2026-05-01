import streamlit as st
import utils
import os

st.set_page_config(
    page_title="AI Sales Co-Pilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background-color: #f8f9fa;
    }
    .main-header {
        text-align: center;
        color: #1e3a8a;
        margin-bottom: 2rem;
    }
    .card {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
    }
    .output-box {
        background-color: #e0f2fe;
        border-left: 5px solid #0ea5e9;
        padding: 1rem;
        border-radius: 5px;
        color: #0f172a;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Configuration")
    api_key_input = st.text_input("Gemini API Key", type="password", help="Enter your Google Gemini API Key here.")
    if api_key_input:
        os.environ["GEMINI_API_KEY"] = api_key_input
        utils.API_KEY = api_key_input
        import google.generativeai as genai
        genai.configure(api_key=api_key_input)
        st.success("API Key configured!")
    elif not utils.API_KEY:
        st.warning("Please configure your Gemini API Key to use the app.")
        
    st.markdown("---")
    st.markdown("Built for **Google PromptWars x Ascent Challenge**")

st.markdown("<h1 class='main-header'>🚀 AI-Powered Sales Co-Pilot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 3rem;'>Transform generic outreach into personalized, human, and thoughtful engagements.</p>", unsafe_allow_html=True)

# Define Tabs
tab1, tab2, tab3 = st.tabs(["🔍 Module A: Research Engine", "✍️ Module B: Message Optimizer", "📈 Module C: Response Analyzer"])

# ==========================================
# MODULE A: Prospect Research Engine
# ==========================================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🔍 Prospect Research Engine (Pre-Pitch)")
    st.markdown("Extract personalized talking points and themes from a prospect's website, LinkedIn profile, or provided text.")
    
    input_type = st.radio("Input Type:", ["URL (Website/LinkedIn)", "Raw Text"])
    
    if input_type == "URL (Website/LinkedIn)":
        target_url = st.text_input("Enter URL:")
        if st.button("Generate Insights", key="btn_mod_a_url"):
            if not target_url:
                st.error("Please enter a URL.")
            else:
                with st.spinner("Scraping and analyzing..."):
                    insights = utils.generate_module_a_insights(target_url, is_url=True)
                    st.session_state['module_a_insights'] = insights
                    st.markdown("<div class='output-box'>", unsafe_allow_html=True)
                    st.markdown("#### 🎯 Personalized Talking Points")
                    st.write(insights)
                    st.markdown("</div>", unsafe_allow_html=True)
    else:
        target_text = st.text_area("Paste Information Here:", height=200)
        if st.button("Generate Insights", key="btn_mod_a_text"):
            if not target_text:
                st.error("Please paste some text.")
            else:
                with st.spinner("Analyzing text..."):
                    insights = utils.generate_module_a_insights(target_text, is_url=False)
                    st.session_state['module_a_insights'] = insights
                    st.markdown("<div class='output-box'>", unsafe_allow_html=True)
                    st.markdown("#### 🎯 Personalized Talking Points")
                    st.write(insights)
                    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# MODULE B: Message Optimizer
# ==========================================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("✍️ The Message Optimizer (The Pitch)")
    st.markdown("Rewrite a generic sales pitch by integrating personalized insights to create a human-like, non-pushy message.")
    
    generic_pitch = st.text_area("Generic Sales Pitch:", height=150, placeholder="Hi [Name], I'm reaching out because we help companies like yours increase revenue by 20%...")
    
    # Pre-fill insights if generated in Module A
    default_insights = st.session_state.get('module_a_insights', '')
    prospect_insights = st.text_area("Prospect Insights (Auto-filled from Module A):", value=default_insights, height=150)
    
    target_tone = st.select_slider(
        "Select Tone:",
        options=["Direct & Professional", "Friendly & Professional", "Casual & Conversational", "Bold & Visionary"]
    )
    
    if st.button("Optimize Message", key="btn_mod_b"):
        if not generic_pitch or not prospect_insights:
            st.error("Please provide both the generic pitch and prospect insights.")
        else:
            with st.spinner("Rewriting pitch..."):
                optimized_message = utils.optimize_module_b_message(generic_pitch, prospect_insights, target_tone)
                st.markdown("<div class='output-box'>", unsafe_allow_html=True)
                st.markdown("#### ✨ Optimized Pitch")
                st.write(optimized_message)
                st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# MODULE C: Response Analyzer & Strategist
# ==========================================
with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📈 Response Analyzer & Strategist (Post-Pitch)")
    st.markdown("Analyze a reply from the prospect to determine sentiment, buying signals, and the optimal next move.")
    
    prospect_reply = st.text_area("Prospect's Reply:", height=200, placeholder="Thanks for reaching out, but we don't have the budget for this right now.")
    
    if st.button("Analyze & Draft Follow-Up", key="btn_mod_c"):
        if not prospect_reply:
            st.error("Please paste the prospect's reply.")
        else:
            with st.spinner("Analyzing response and strategizing next move..."):
                analysis_result = utils.analyze_module_c_response(prospect_reply)
                st.markdown("<div class='output-box'>", unsafe_allow_html=True)
                st.markdown("#### 🧠 Strategic Analysis & Drafted Reply")
                st.write(analysis_result)
                st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
