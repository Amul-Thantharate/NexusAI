# NexusAI Architecture

This document provides an overview of the NexusAI system architecture, explaining how the different components interact and how the application is structured.

## System Overview

NexusAI is built as a Streamlit web application that integrates multiple AI services:

1. **Chat Service**: Powered by Groq's LLM API
2. **Image Analysis**: Uses Groq's multimodal capabilities
3. **Image Generation**: Leverages Azure OpenAI's DALL-E 3
4. **Text-to-Speech**: Utilizes Groq's TTS API
5. **Audio Transcription**: Employs Groq's Whisper implementation
6. **Document Chat**: Combines Google Gemini with ChromaDB for RAG

## Component Architecture

```
NexusAI
│
├── main.py                 # Main application entry point
├── document_chat.py        # Document chat functionality
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys)
└── .env.example            # Example environment file
```

## Data Flow

### Chat Service
1. User inputs a message
2. Application sends the message to Groq API
3. Groq processes the message and returns a response
4. Response is displayed to the user and stored in chat history

### Image Analysis
1. User uploads an image and provides an analysis prompt
2. Image is encoded to base64 and sent to Groq's multimodal API
3. Groq analyzes the image based on the prompt
4. Analysis results are displayed to the user and stored in history

### Image Generation
1. User provides a text prompt for image generation
2. Prompt is sent to Azure OpenAI's DALL-E 3 API
3. Generated image URL is returned
4. Image is displayed to the user and stored in history

### Text-to-Speech
1. User inputs text and selects voice, model, and format options
2. Request is sent to Groq's TTS API
3. Audio file is generated and returned
4. Audio is played for the user and made available for download

### Audio Transcription
1. User uploads an audio file
2. Audio is sent to Groq's Whisper API
3. Transcription is returned with timestamps
4. Text is displayed to the user and stored in history

### Document Chat
1. User uploads documents (PDF, TXT, CSV)
2. Documents are processed and split into chunks
3. Google Gemini embeddings are generated for each chunk
4. Embeddings are stored in ChromaDB vector database
5. User asks questions about the documents
6. System retrieves relevant chunks using similarity search
7. Google Gemini generates answers based on retrieved chunks
8. Answers are displayed to the user with source attribution

## Technical Components

### Frontend
- **Streamlit**: Provides the web interface and UI components
- **Session State**: Manages application state and history

### Backend Services
- **Groq API**: Provides LLM, multimodal, TTS, and transcription capabilities
- **Azure OpenAI**: Provides image generation with DALL-E 3
- **Google Gemini**: Provides embeddings and LLM for document chat
- **ChromaDB**: Vector database for document embeddings

### Document Processing
- **LangChain**: Framework for document processing and RAG
- **Document Loaders**: PDF, TXT, and CSV loaders
- **Text Splitter**: Splits documents into manageable chunks
- **Retrieval Chain**: Connects user queries to relevant document chunks

## Security Considerations

- API keys are stored in environment variables, not in code
- Temporary files are used for audio and document processing
- User data is stored in session state and not persisted between sessions

## Scalability

The current implementation is designed for individual use or small-scale deployment. For larger deployments, consider:

1. Implementing a proper database for persistent storage
2. Adding user authentication
3. Optimizing document processing for larger files
4. Implementing caching for API responses
5. Containerizing the application for easier deployment

## Future Enhancements

1. Add support for more document types (DOCX, PPTX, etc.)
2. Implement collaborative features for team use
3. Add custom training for domain-specific document understanding
4. Integrate with more AI providers for redundancy
5. Implement a feedback loop for improving responses
