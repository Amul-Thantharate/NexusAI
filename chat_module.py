"""
Chat Module for NexusAI
This module provides chat functionality using Groq's LLM API.
"""

import streamlit as st
import os
import time
from openai import OpenAI

def initialize_chat_client():
    """Initialize the chat client with Groq API"""
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

def chat_completion(client, messages, model, temperature=0.7, max_tokens=1024, top_p=1.0):
    """Get chat completion from Groq"""
    if not client:
        return "Error: Groq API key not set. Please enter your Groq API key in the API Setup page."

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def display_chat_interface():
    """Display the chat interface"""
    st.title("💬 Chat with AI")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Initialize client
    client = initialize_chat_client()
    
    # Model selection and parameters
    col1, col2 = st.columns(2)
    with col1:
        model = st.selectbox(
            "Model:", 
            ["llama3-8b-8192", "llama3-70b-8192", "mixtral-8x7b-32768"],
            index=0
        )
    with col2:
        temperature = st.slider("Temperature:", 0.0, 1.0, 0.7, 0.1)
    
    # Display chat history
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(chat['message'])
        with st.chat_message("assistant"):
            st.markdown(chat['response'])

    # Clear chat history button
    if st.session_state.chat_history:
        if st.button("Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()
        st.markdown("---")

    # Chat input
    prompt = st.chat_input("Type your message here...")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                messages = [{"role": "user", "content": prompt}]
                response = chat_completion(
                    client=client,
                    messages=messages,
                    model=model,
                    temperature=temperature,
                    max_tokens=1024,
                    top_p=1.0
                )
                st.markdown(response)

                # Save to history
                st.session_state.chat_history.append({
                    'message': prompt,
                    'response': response,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                })
