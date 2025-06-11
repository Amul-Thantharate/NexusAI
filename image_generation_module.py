"""
Image Generation Module for NexusAI
This module provides image generation functionality using OpenAI and Azure OpenAI DALL-E 3.
"""

import streamlit as st
import os
import time
import json
from openai import OpenAI
from openai import AzureOpenAI

def initialize_openai_client():
    """Initialize the OpenAI client for image generation"""
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        return None
        
    try:
        client = OpenAI(
            api_key=openai_api_key
        )
        return client
    except Exception as e:
        st.error(f"Failed to initialize OpenAI client: {e}")
        return None

def initialize_azure_openai_client():
    """Initialize the Azure OpenAI client for image generation"""
    azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_openai_api_version = os.getenv("OPENAI_API_VERSION", "2024-04-01-preview")
    
    if not azure_openai_api_key or not azure_openai_endpoint:
        return None
        
    try:
        client = AzureOpenAI(
            api_version=azure_openai_api_version,
            azure_endpoint=azure_openai_endpoint,
            api_key=azure_openai_api_key
        )
        return client
    except Exception as e:
        st.error(f"Failed to initialize Azure OpenAI client: {e}")
        return None

def generate_image(client, prompt, size, provider="openai"):
    """Generate image using selected provider"""
    if not client:
        return f"Error: {provider.capitalize()} API key not set. Please enter your API key in the API Setup page."

    try:
        if provider == "openai":
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size=size,
                style="vivid",
                quality="standard"
            )
            return response.data[0].url
        elif provider == "azure":
            deployment = os.getenv("DEPLOYMENT_NAME", "dall-e-3")
            response = client.images.generate(
                model=deployment,
                prompt=prompt,
                n=1,
                size=size,
                style="vivid",
                quality="standard"
            )
            # Extract URL from response
            image_url = json.loads(response.model_dump_json())['data'][0]['url']
            return image_url
    except Exception as e:
        return f"Error: {str(e)}"

def display_image_generation_interface():
    """Display the image generation interface"""
    st.title("🎨 Image Generation")
    
    # Initialize history
    if 'image_generation_history' not in st.session_state:
        st.session_state.image_generation_history = []
    
    # Initialize clients
    openai_client = initialize_openai_client()
    azure_openai_client = initialize_azure_openai_client()
    
    # Image generation options
    prompt = st.text_area("Image prompt:", height=100)
    
    col1, col2 = st.columns(2)
    with col1:
        provider = st.selectbox("Provider:", ["OpenAI DALL-E 3", "Azure OpenAI DALL-E 3"], index=0)
    with col2:
        size = st.selectbox("Image size:", ["1024x1024", "1792x1024", "1024x1792"], index=0)

    # Generate button
    if st.button("Generate Image"):
        if not prompt:
            st.warning("Please enter a prompt")
        else:
            with st.spinner("Generating image..."):
                # Convert provider selection to internal name
                provider_name = "openai" if provider == "OpenAI DALL-E 3" else "azure"
                
                # Select appropriate client
                client = openai_client if provider_name == "openai" else azure_openai_client
                
                image_result = generate_image(client, prompt, size, provider_name)
                
                if image_result.startswith("Error:"):
                    st.error(image_result)
                else:
                    # Both OpenAI and Azure OpenAI return URLs
                    st.image(image_result, caption=prompt, use_container_width=True)
                    st.markdown(f"[Download Image]({image_result})")
                    
                    # Save to history
                    st.session_state.image_generation_history.append({
                        'prompt': prompt,
                        'size': size,
                        'provider': provider,
                        'url': image_result,
                        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                    })

    # Display history
    if st.session_state.image_generation_history:
        st.markdown("---")
        st.subheader("Generation History")

        for idx, item in enumerate(reversed(st.session_state.image_generation_history)):
            with st.expander(f"Image {len(st.session_state.image_generation_history)-idx} - {item['timestamp']}"):
                st.markdown(f"**Prompt:** {item['prompt']}")
                st.markdown(f"**Provider:** {item.get('provider', 'OpenAI DALL-E 3')}")
                
                # Handle different URL types
                if isinstance(item['url'], str) and item['url'].startswith('http'):
                    st.image(item['url'], use_container_width=True)
                    st.markdown(f"[Download]({item['url']})")
                else:
                    st.error(f"Invalid image URL format: {item['url']}")

        # Clear history button
        if st.button("Clear Generation History"):
            st.session_state.image_generation_history = []
            st.rerun()
