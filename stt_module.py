"""
Speech-to-Text Module for NexusAI
This module provides speech-to-text functionality using Groq's Whisper API.
"""

import streamlit as st
import os
import time
import tempfile
from groq import Groq

def initialize_whisper_client():
    """Initialize the Whisper client with Groq API"""
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        return None
        
    try:
        client = Groq(api_key=groq_api_key)
        return client
    except Exception as e:
        st.error(f"Failed to initialize Whisper client: {e}")
        return None

def transcribe_audio(client, audio_file, model="whisper-large-v3-turbo", language="en", temperature=0.0):
    """Transcribe audio using Groq's Whisper model"""
    if not client:
        return "Error: Groq API key not set. Please enter your Groq API key in the API Setup page."

    try:
        with open(audio_file, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=file,
                model=model,
                language=language,
                temperature=temperature,
                response_format="verbose_json",
                timestamp_granularities=["word", "segment"]
            )
            return transcription
    except Exception as e:
        st.error(f"Transcription failed: {str(e)}")
        return None

def display_stt_interface():
    """Display the speech-to-text interface"""
    st.title("🎤 Speech-to-Text")
    
    # Initialize history
    if 'transcription_history' not in st.session_state:
        st.session_state.transcription_history = []
    
    # Initialize client
    client = initialize_whisper_client()
    
    # Audio upload
    uploaded_audio = st.file_uploader("Upload audio file:", type=["wav", "mp3", "m4a", "ogg"])
    
    if uploaded_audio is not None:
        # Save uploaded audio to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_audio:
            tmp_audio.write(uploaded_audio.getvalue())
            tmp_audio.flush()
            audio_file = tmp_audio.name

            # Display audio player
            st.audio(uploaded_audio)

            # Transcription options
            col1, col2, col3 = st.columns(3)

            with col1:
                model = st.selectbox("Model:", ["whisper-large-v3-turbo", "whisper-large-v3"], index=0)
            with col2:
                language = st.selectbox(
                    "Language:", 
                    ["en", "es", "fr", "de", "it", "pt", "nl", "ru", "zh", "ja", "ko"], 
                    index=0
                )
            with col3:
                temperature = st.slider("Temperature:", 0.0, 1.0, 0.0, 0.1)

            # Transcribe button
            if st.button("Transcribe"):
                with st.spinner("Transcribing audio..."):
                    transcription = transcribe_audio(client, audio_file, model, language, temperature)

                    if transcription:
                        # Display transcription
                        st.markdown("### Transcription Result")
                        st.markdown(transcription.text)

                        # Save to history
                        st.session_state.transcription_history.append({
                            'audio_file': audio_file,
                            'transcription': transcription.text,
                            'language': language,
                            'model': model,
                            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                        })

                        # Display timestamps if available
                        if hasattr(transcription, 'segments'):
                            st.markdown("### Word Timestamps")
                            for segment in transcription.segments:
                                try:
                                    text = segment.get('text')
                                    start = segment.get('start')
                                    end = segment.get('end')

                                    if text is None or start is None or end is None:
                                        continue  # Skip to the next segment

                                    st.markdown(f"{text} ({start:.2f}s - {end:.2f}s)")

                                except Exception as e:
                                    st.error(f"Error processing segment: {e}")
                                    break
                    else:
                        st.error("Transcription failed. Check the logs for details.")

    # Display history
    if st.session_state.transcription_history:
        st.markdown("---")
        st.subheader("Transcription History")

        for idx, item in enumerate(reversed(st.session_state.transcription_history)):
            with st.expander(f"Transcription {len(st.session_state.transcription_history)-idx} - {item['timestamp']}"):
                st.audio(item['audio_file'], format="audio/wav")
                st.markdown(f"**Transcription:** {item['transcription']}")
                st.markdown(f"**Language:** {item['language']}")
                st.markdown(f"**Model:** {item['model']}")

                # Download options
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        label="Download Audio",
                        data=open(item['audio_file'], "rb").read(),
                        file_name=f"audio_{idx+1}.wav",
                        mime="audio/wav"
                    )
                with col2:
                    st.download_button(
                        label="Download Transcription",
                        data=item['transcription'].encode('utf-8'),
                        file_name=f"transcription_{idx+1}.txt",
                        mime="text/plain"
                    )

        # Clear history button
        if st.button("Clear Transcription History"):
            st.session_state.transcription_history = []
            st.rerun()
