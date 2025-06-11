"""
Text-to-Speech Module for NexusAI
This module provides text-to-speech functionality using Groq's TTS API.
"""

import streamlit as st
import os
import time
import tempfile
from openai import OpenAI

def initialize_tts_client():
    """Initialize the TTS client with Groq API"""
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        return None
        
    try:
        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )
        return client
    except Exception as e:
        st.error(f"Failed to initialize Groq client: {e}")
        return None

def generate_speech(client, text, voice, model, output_format):
    """Generate speech using Groq TTS API"""
    if not client:
        return "Error: Groq API key not set. Please enter your Groq API key in the API Setup page."

    try:
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=text,
            response_format=output_format
        )

        # Save to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{output_format}") as tmp_file:
            for chunk in response.iter_bytes():
                tmp_file.write(chunk)
            tmp_file.flush()
            return tmp_file.name
    except Exception as e:
        st.error(f"TTS generation failed: {str(e)}")
        return None

def display_tts_interface():
    """Display the text-to-speech interface"""
    st.title("🗣️ Text-to-Speech")
    
    # Initialize history
    if 'tts_history' not in st.session_state:
        st.session_state.tts_history = []
    
    # Initialize client
    client = initialize_tts_client()
    
    # TTS options
    text = st.text_area("Text to convert to speech:", height=150)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        voice = st.selectbox(
            "Voice:", 
            ["Aaliyah-PlayAI", "Dave-PlayAI", "Farah-PlayAI", "Mike-PlayAI",
             "Sarah-PlayAI", "Andrew-PlayAI", "Brian-PlayAI", "Olivia-PlayAI", "Jason-PlayAI"],
            index=0
        )
    with col2:
        model = st.selectbox("Model:", ["playai-tts"], index=0)
    with col3:
        output_format = st.selectbox("Output format:", ["wav", "mp3", "aac", "flac", "pcm"], index=0)

    # Generate button
    if st.button("Generate Speech"):
        if not text:
            st.warning("Please enter text")
        else:
            with st.spinner("Generating speech..."):
                audio_file = generate_speech(client, text, voice, model, output_format)

                if audio_file:
                    st.audio(audio_file, format=f"audio/{output_format}")
                    st.download_button(
                        label="Download Audio",
                        data=open(audio_file, "rb").read(),
                        file_name=f"speech.{output_format}",
                        mime=f"audio/{output_format}"
                    )

                    # Save to history
                    st.session_state.tts_history.append({
                        'text': text,
                        'voice': voice,
                        'model': model,
                        'format': output_format,
                        'audio_file': audio_file,
                        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                    })

    # Display history
    if st.session_state.tts_history:
        st.markdown("---")
        st.subheader("TTS History")

        for idx, item in enumerate(reversed(st.session_state.tts_history)):
            with st.expander(f"Speech {len(st.session_state.tts_history)-idx} - {item['timestamp']}"):
                st.markdown(f"**Text:** {item['text'][:100]}...")
                st.audio(item['audio_file'], format=f"audio/{item['format']}")
                st.download_button(
                    label=f"Download ({idx+1})",
                    data=open(item['audio_file'], "rb").read(),
                    file_name=f"speech_{idx+1}.{item['format']}",
                    mime=f"audio/{item['format']}",
                    key=f"download_{idx}"
                )

        # Clear history button
        if st.button("Clear TTS History"):
            st.session_state.tts_history = []
            st.rerun()
