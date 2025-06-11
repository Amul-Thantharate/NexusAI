"""
Image Analysis Module for NexusAI
This module provides image analysis functionality using Groq's multimodal API.
"""

import streamlit as st
import os
import time
import base64
from openai import OpenAI

def initialize_image_client():
    """Initialize the client for image analysis with Groq API"""
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

def analyze_image(client, image_bytes, prompt, model):
    """Analyze image using Groq's multimodal API"""
    if not client:
        return "Error: Groq API key not set. Please enter your Groq API key in the API Setup page."

    try:
        base64_image = base64.b64encode(image_bytes).decode('utf-8')

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def display_image_analysis_interface():
    """Display the image analysis interface"""
    st.title("🖼️ Image Analysis")
    
    # Initialize history
    if 'image_analysis_history' not in st.session_state:
        st.session_state.image_analysis_history = []
    
    # Initialize client
    client = initialize_image_client()
    
    # Upload image
    uploaded_file = st.file_uploader("Upload an image for analysis:", type=["jpg", "jpeg", "png", "webp"])
    
    # Analysis options
    analysis_prompt = st.text_input("Analysis Prompt:", "What's in this image?")
    analysis_model = st.selectbox(
        "Model:", 
        ["meta-llama/llama-4-maverick-17b-128e-instruct", "meta-llama/llama-4-scout-17b-16e-instruct"], 
        index=0
    )

    # Analyze button
    if uploaded_file is not None and st.button("Analyze Image"):
        image_bytes = uploaded_file.getvalue()
        st.image(image_bytes, caption="Uploaded Image", use_container_width=True)

        with st.spinner("Analyzing image..."):
            analysis_result = analyze_image(
                client=client,
                image_bytes=image_bytes,
                prompt=analysis_prompt,
                model=analysis_model
            )

            st.markdown("### Analysis Result")
            st.markdown(analysis_result)

            # Save to history
            st.session_state.image_analysis_history.append({
                'image_bytes': image_bytes,
                'prompt': analysis_prompt,
                'model': analysis_model,
                'result': analysis_result,
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            })

    # Display history
    if st.session_state.image_analysis_history:
        st.markdown("---")
        st.subheader("Analysis History")

        for idx, item in enumerate(reversed(st.session_state.image_analysis_history)):
            with st.expander(f"Analysis {len(st.session_state.image_analysis_history)-idx} - {item['timestamp']}"):
                st.image(item['image_bytes'], use_container_width=True)
                st.markdown(f"**Prompt:** {item['prompt']}")
                st.markdown(f"**Model:** {item['model']}")
                st.markdown(f"**Result:** {item['result']}")

        # Clear history button
        if st.button("Clear Analysis History"):
            st.session_state.image_analysis_history = []
            st.rerun()
