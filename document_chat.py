"""
Document Chat Module for NexusAI
This module provides functionality to chat with documents using ChromaDB and Google Gemini embeddings.
"""

import os
import tempfile
from typing import List, Dict, Any, Optional
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DocumentChat:
    """Class for handling document chat functionality"""
    
    def __init__(self, api_key=None):
        """Initialize the DocumentChat class"""
        self.embeddings = None
        self.vector_store = None
        self.chat_history = []
        self.documents = []
        self.db_path = os.path.join(tempfile.gettempdir(), "chroma_db")
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        
        # Configure Google Gemini API
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.initialize_embeddings()
        
    def initialize_embeddings(self) -> None:
        """Initialize the embedding model"""
        if not self.api_key:
            st.error("Google API Key not found. Please set the GOOGLE_API_KEY environment variable.")
            return
            
        try:
            self.embeddings = GoogleGenerativeAIEmbeddings(
                model="models/embedding-001",
                google_api_key=self.api_key
            )
        except Exception as e:
            st.error(f"Failed to initialize embeddings: {str(e)}")
    
    def load_document(self, file) -> bool:
        """
        Load a document and create embeddings
        
        Args:
            file: The uploaded file object
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.embeddings:
            st.error("Embeddings not initialized. Cannot load document.")
            return False
            
        try:
            # Save the uploaded file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(file.getvalue())
                file_path = tmp_file.name
            
            # Load document based on file type
            if file.name.lower().endswith('.pdf'):
                loader = PyPDFLoader(file_path)
            elif file.name.lower().endswith('.csv'):
                loader = CSVLoader(file_path)
            else:
                # Default to text loader for other file types
                loader = TextLoader(file_path)
                
            documents = loader.load()
            
            # Split the documents into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=100
            )
            split_docs = text_splitter.split_documents(documents)
            
            # Store document info
            self.documents.append({
                "name": file.name,
                "path": file_path,
                "chunks": len(split_docs)
            })
            
            # Create or update vector store
            if self.vector_store is None:
                self.vector_store = Chroma.from_documents(
                    documents=split_docs,
                    embedding=self.embeddings,
                    persist_directory=self.db_path
                )
            else:
                self.vector_store.add_documents(split_docs)
                
            return True
            
        except Exception as e:
            st.error(f"Error loading document: {str(e)}")
            return False
    
    def get_document_info(self) -> List[Dict[str, Any]]:
        """Get information about loaded documents"""
        return self.documents
    
    def clear_documents(self) -> None:
        """Clear all loaded documents and the vector store"""
        try:
            if self.vector_store:
                # Delete the persistent storage
                import shutil
                if os.path.exists(self.db_path):
                    shutil.rmtree(self.db_path)
                
                self.vector_store = None
                self.documents = []
                self.chat_history = []
                
        except Exception as e:
            st.error(f"Error clearing documents: {str(e)}")
    
    def chat_with_documents(self, query: str, model_name: str = "gemini-2.0-flash") -> Optional[str]:
        """
        Chat with the loaded documents
        
        Args:
            query: The user's question
            model_name: The name of the Gemini model to use
            
        Returns:
            str: The response from the model
        """
        if not self.vector_store:
            return "Please load documents before asking questions."
            
        try:
            # Initialize the LLM
            llm = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=self.api_key,
                temperature=0.3
            )
            
            # Create a retrieval chain
            retrieval_chain = ConversationalRetrievalChain.from_llm(
                llm=llm,
                retriever=self.vector_store.as_retriever(
                    search_kwargs={"k": 5}
                ),
                return_source_documents=True
            )
            
            # Get response
            result = retrieval_chain.invoke({
                "question": query,
                "chat_history": self.chat_history
            })
            
            # Update chat history
            self.chat_history.append((query, result["answer"]))
            
            # Format response with sources
            response = result["answer"]
            
            # Add source information
            if "source_documents" in result:
                sources = set()
                for doc in result["source_documents"]:
                    if hasattr(doc, "metadata") and "source" in doc.metadata:
                        sources.add(doc.metadata["source"])
                
                if sources:
                    response += "\n\nSources:\n"
                    for i, source in enumerate(sources, 1):
                        response += f"{i}. {os.path.basename(source)}\n"
            
            return response
            
        except Exception as e:
            st.error(f"Error in chat: {str(e)}")
            return f"An error occurred: {str(e)}"
    
    def get_chat_history(self) -> List[tuple]:
        """Get the chat history"""
        return self.chat_history
    
    def clear_chat_history(self) -> None:
        """Clear the chat history"""
        self.chat_history = []
