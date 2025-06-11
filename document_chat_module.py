"""
Document Chat Module for NexusAI
This module provides document chat functionality using Google Gemini and ChromaDB.
"""

import streamlit as st
import os
import tempfile
from document_chat import DocumentChat

def initialize_document_chat():
    """Initialize the document chat with Google API"""
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        return None
        
    try:
        doc_chat = DocumentChat(api_key=google_api_key)
        return doc_chat
    except Exception as e:
        st.error(f"Failed to initialize Document Chat: {e}")
        return None

def display_document_chat_interface():
    """Display the document chat interface"""
    st.title("📚 Document Chat")
    
    # Initialize document chat
    if 'document_chat' not in st.session_state:
        st.session_state.document_chat = initialize_document_chat()
    
    # Check if document chat is initialized
    if not st.session_state.document_chat:
        st.error("Google API key not set. Please enter your Google API key in the API Setup page.")
        return
    
    # Document upload section
    st.subheader("Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload documents (PDF, TXT, CSV)", 
        type=["pdf", "txt", "csv"], 
        accept_multiple_files=True
    )
    
    if uploaded_files:
        for file in uploaded_files:
            if st.button(f"Process {file.name}", key=f"process_{file.name}"):
                with st.spinner(f"Processing {file.name}..."):
                    success = st.session_state.document_chat.load_document(file)
                    if success:
                        st.success(f"Successfully processed {file.name}")
                    else:
                        st.error(f"Failed to process {file.name}")
    
    # Document info section
    documents = st.session_state.document_chat.get_document_info()
    if documents:
        st.subheader("Loaded Documents")
        for i, doc in enumerate(documents):
            st.markdown(f"**{i+1}. {doc['name']}** ({doc['chunks']} chunks)")
        
        if st.button("Clear All Documents"):
            st.session_state.document_chat.clear_documents()
            st.success("All documents cleared")
            st.rerun()
    
    # Chat interface
    st.subheader("Chat with Documents")
    
    # Display chat history
    chat_history = st.session_state.document_chat.get_chat_history()
    for user_msg, ai_msg in chat_history:
        with st.chat_message("user"):
            st.markdown(user_msg)
        with st.chat_message("assistant"):
            st.markdown(ai_msg)
    
    # Chat input
    if documents:  # Only show chat input if documents are loaded
        user_question = st.chat_input("Ask a question about your documents...")
        if user_question:
            with st.chat_message("user"):
                st.markdown(user_question)
            
            with st.chat_message("assistant"):
                with st.spinner("Searching documents..."):
                    model_name = "gemini-2.0-flash"
                    response = st.session_state.document_chat.chat_with_documents(user_question, model_name)
                    st.markdown(response)
    else:
        st.info("Please upload and process documents before chatting.")
    
    # Clear chat history button
    if chat_history:
        if st.button("Clear Chat History"):
            st.session_state.document_chat.clear_chat_history()
            st.success("Chat history cleared")
            st.rerun()
