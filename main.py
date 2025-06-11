#!/usr/bin/env python3
"""
NexusAI - AI-Powered Chat & Image Platform
Authors: Amul Thantharate, Avanti Nandanwar
License: MIT
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Import modules
from chat_module import display_chat_interface
from image_analysis_module import display_image_analysis_interface
from image_generation_module import display_image_generation_interface
from tts_module import display_tts_interface
from stt_module import display_stt_interface
from document_chat_module import display_document_chat_interface

# Load environment variables
load_dotenv()

# Configuration
st.set_page_config(
    page_title="NexusAI Dashboard", 
    layout="wide",
    page_icon="🤖"
)

# Custom CSS for simple animations
st.markdown("""
<style>
    /* Button styling */
    .stButton button {
        width: 100%;
        border-radius: 5px;
        height: 2.5em;
        margin-bottom: 5px;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Simple page transition */
    .main .block-container {
        animation: fadeIn 0.3s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session states
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Function to change page
def change_page(page):
    st.session_state.page = page

# Main application
def main():
    # Sidebar navigation
    with st.sidebar:
        # Logo and title
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown("# 🤖")
        with col2:
            st.markdown("# NexusAI")
        
        st.markdown("---")
        
        # Navigation with styled buttons
        st.markdown("### 📋 Navigation")
        
        # Apply different styles based on current page
        current_page = st.session_state.page
        
        # Home button
        button_type = "primary" if current_page == "Home" else "secondary"
        if st.button("🏠 Home", key="home_btn", use_container_width=True, type=button_type):
            change_page("Home")
            
        # API Setup button
        button_type = "primary" if current_page == "API Setup" else "secondary"
        if st.button("🔑 API Setup", key="api_btn", use_container_width=True, type=button_type):
            change_page("API Setup")
            
        st.markdown("#### AI Services")
        
        # Chat button
        button_type = "primary" if current_page == "Chat" else "secondary"
        if st.button("💬 Chat", key="chat_btn", use_container_width=True, type=button_type):
            change_page("Chat")
            
        # Image Analysis button
        button_type = "primary" if current_page == "Image Analysis" else "secondary"
        if st.button("🖼️ Image Analysis", key="img_analysis_btn", use_container_width=True, type=button_type):
            change_page("Image Analysis")
            
        # Image Generation button
        button_type = "primary" if current_page == "Image Generation" else "secondary"
        if st.button("🎨 Image Generation", key="img_gen_btn", use_container_width=True, type=button_type):
            change_page("Image Generation")
            
        # Text-to-Speech button
        button_type = "primary" if current_page == "Text-to-Speech" else "secondary"
        if st.button("🗣️ Text-to-Speech", key="tts_btn", use_container_width=True, type=button_type):
            change_page("Text-to-Speech")
            
        # Speech-to-Text button
        button_type = "primary" if current_page == "Speech-to-Text" else "secondary"
        if st.button("🎤 Speech-to-Text", key="stt_btn", use_container_width=True, type=button_type):
            change_page("Speech-to-Text")
            
        # Document Chat button
        button_type = "primary" if current_page == "Document Chat" else "secondary"
        if st.button("📚 Document Chat", key="doc_chat_btn", use_container_width=True, type=button_type):
            change_page("Document Chat")
            
        st.markdown("---")
        
        # Thank You button
        button_type = "primary" if current_page == "Thank You" else "secondary"
        if st.button("🙏 Thank You", key="thanks_btn", use_container_width=True, type=button_type):
            change_page("Thank You")
        
        # Footer with author info
        st.markdown("---")
        st.markdown("### 👨‍💻 Created By")
        
        # Author info with social links
        st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="https://github.com/identicons/Amul-Thantharate.png" width="40" style="border-radius: 50%; margin-right: 10px;">
            <span style="font-weight: bold;">Amul Thantharate</span>
        </div>

        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="https://github.com/identicons/Avanti-ui.png" width="40" style="border-radius: 50%; margin-right: 10px;">
            <span style="font-weight: bold;">Avanti Nandanwar</span>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Amul-Thantharate)", unsafe_allow_html=True)
        with col2:
            st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amul-thantharate)", unsafe_allow_html=True)
        with col3:
            st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Avanti-ui)", unsafe_allow_html=True)
        with col4:
            st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/avanti-nandanwar-812b79266)", unsafe_allow_html=True)
            
        # Version info
        st.markdown("---")
        st.markdown("<div style='text-align: center; color: #888888;'>v2.0.0</div>", unsafe_allow_html=True)
    
    # Main content based on selected page
    if st.session_state.page == "Home":
        display_home_page()
    elif st.session_state.page == "API Setup":
        display_api_setup()
    elif st.session_state.page == "Chat":
        display_chat_interface()
    elif st.session_state.page == "Image Analysis":
        display_image_analysis_interface()
    elif st.session_state.page == "Image Generation":
        display_image_generation_interface()
    elif st.session_state.page == "Text-to-Speech":
        display_tts_interface()
    elif st.session_state.page == "Speech-to-Text":
        display_stt_interface()
    elif st.session_state.page == "Document Chat":
        display_document_chat_interface()
    elif st.session_state.page == "Thank You":
        display_thank_you()

# Page functions
def display_home_page():
    st.title("🤖 Welcome to NexusAI")
    
    st.markdown("""
    ## AI-Powered Chat & Image Platform
    
    NexusAI is a comprehensive AI platform that combines multiple AI capabilities into a single, 
    user-friendly Streamlit dashboard. Built with Python and powered by Groq, OpenAI, Azure OpenAI, 
    and Google Gemini, NexusAI offers chat, image analysis, image generation, text-to-speech, 
    audio transcription, and document chat services.
    
    ### ✨ Features
    
    - 💬 **AI Chat**: Engage in conversations with advanced LLMs like Llama 3
    - 🖼️ **Image Analysis**: Upload and analyze images with multimodal AI models
    - 🎨 **Image Generation**: Create stunning images with OpenAI or Azure OpenAI DALL-E 3
    - 🗣️ **Text-to-Speech**: Convert text to natural-sounding speech
    - 🎤 **Audio Transcription**: Transcribe audio files with Whisper models
    - 📚 **Document Chat**: Chat with your documents using Google Gemini and ChromaDB
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 👨‍💻 About the Authors
    
    **Amul Thantharate** is an AI enthusiast passionate about creating innovative solutions.
    
    - [GitHub](https://github.com/Amul-Thantharate)
    - [LinkedIn](https://www.linkedin.com/in/amul-thantharate)
    
    **Avanti Nandanwar** is a dedicated AI developer contributing to this project.
    
    - [GitHub](https://github.com/Avanti-ui)
    - [LinkedIn](https://www.linkedin.com/in/avanti-nandanwar-812b79266)
    """)

def display_api_setup():
    st.title("🔑 API Key Configuration")
    
    # API Key information
    with st.expander("ℹ️ Where to get API Keys", expanded=True):
        st.markdown("""
        ### Groq API Key
        1. Visit [Groq's website](https://console.groq.com/signup) and create an account
        2. Navigate to the API section in your dashboard
        3. Generate a new API key
        4. Copy the key and paste it below
        
        ### OpenAI API Key
        1. Visit [OpenAI's website](https://platform.openai.com/) and create an account
        2. Navigate to the API section in your dashboard
        3. Generate a new API key
        4. Copy the key and paste it below
        
        ### Google Gemini API Key
        1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and create an account
        2. Create a new API key
        3. Copy the key and paste it below
        
        ### Azure OpenAI API Key
        1. Create an [Azure account](https://azure.microsoft.com/) if you don't have one
        2. Set up an Azure OpenAI resource
        3. Deploy a DALL-E 3 model
        4. Get your API key, endpoint, and deployment name
        5. Enter these details in the fields below
        """)
    
    # API Key input fields
    groq_api_key = st.text_input("Groq API Key", value=os.getenv("GROQ_API_KEY", ""), type="password")
    openai_api_key = st.text_input("OpenAI API Key", value=os.getenv("OPENAI_API_KEY", ""), type="password")
    google_api_key = st.text_input("Google API Key", value=os.getenv("GOOGLE_API_KEY", ""), type="password")
    
    # Azure OpenAI configuration
    st.subheader("Azure OpenAI Configuration")
    azure_openai_api_key = st.text_input("Azure OpenAI API Key", value=os.getenv("AZURE_OPENAI_API_KEY", ""), type="password")
    azure_openai_endpoint = st.text_input("Azure OpenAI Endpoint", value=os.getenv("AZURE_OPENAI_ENDPOINT", "https://image-ai-project.openai.azure.com/"))
    azure_openai_api_version = st.text_input("Azure OpenAI API Version", value=os.getenv("OPENAI_API_VERSION", "2024-04-01-preview"))
    azure_openai_deployment = st.text_input("Azure OpenAI Deployment Name", value=os.getenv("DEPLOYMENT_NAME", "dall-e-3"))
    
    # Save API keys button
    if st.button("Save API Keys"):
        # Update environment variables
        os.environ["GROQ_API_KEY"] = groq_api_key
        os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ["GOOGLE_API_KEY"] = google_api_key
        os.environ["AZURE_OPENAI_API_KEY"] = azure_openai_api_key
        os.environ["AZURE_OPENAI_ENDPOINT"] = azure_openai_endpoint
        os.environ["OPENAI_API_VERSION"] = azure_openai_api_version
        os.environ["DEPLOYMENT_NAME"] = azure_openai_deployment
        
        st.success("API keys saved successfully!")

def display_thank_you():
    st.title("🙏 Thank You for Using NexusAI")
    
    st.markdown("""
    ## We appreciate your support!
    
    NexusAI is continuously being improved to provide you with the best AI experience.
    
    ### 👨‍💻 About the Authors
    
    **Amul Thantharate** is an AI enthusiast passionate about creating innovative solutions.
    
    - [GitHub](https://github.com/Amul-Thantharate)
    - [LinkedIn](https://www.linkedin.com/in/amul-thantharate)
    
    **Avanti Nandanwar** is a dedicated AI developer contributing to this project.
    
    - [GitHub](https://github.com/Avanti-ui)
    - [LinkedIn](https://www.linkedin.com/in/avanti-nandanwar-812b79266)
    
    ### ⭐ Support the Project
    
    If you find this project useful, please consider giving it a star on GitHub!
    
    [Star on GitHub](https://github.com/Amul-Thantharate/NexusAI)
    """)

if __name__ == "__main__":
    main()
