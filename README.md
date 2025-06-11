# 🤖 NexusAI - AI-Powered Chat & Image Platform

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.45.1%2B-red)
![Groq](https://img.shields.io/badge/groq-1.0.0%2B-blue)
![OpenAI](https://img.shields.io/badge/openai-1.0.0%2B-blue)
![Azure OpenAI](https://img.shields.io/badge/azure_openai-1.0.0%2B-blue)
![Google Gemini](https://img.shields.io/badge/google_gemini-1.0.0%2B-blue)

NexusAI is a comprehensive AI platform that combines multiple AI capabilities into a single, user-friendly Streamlit dashboard. Built with Python and powered by Groq, OpenAI, Azure OpenAI, and Google Gemini, NexusAI offers chat, image analysis, image generation, text-to-speech, audio transcription, and document chat services.

## 🆕 New UI Features

The updated UI includes:

1. **Home Page** - Introduction and project overview with author information
2. **API Key Setup** - Dedicated page for configuring all API keys with instructions
3. **Chat** - Enhanced chat interface with Groq's LLMs
4. **Image Analysis** - Improved image analysis with multimodal models
5. **Image Generation** - Create images with OpenAI or Azure OpenAI DALL-E 3
6. **Text-to-Speech** - Convert text to natural speech with multiple voice options
7. **Speech-to-Text** - Transcribe audio with advanced Whisper models
8. **Document Chat** - Chat with your documents using Google Gemini
9. **Thank You Page** - Acknowledgment page with author information

## ✨ Features

- 💬 **AI Chat**: Engage in conversations with advanced LLMs like Llama 3
- 🖼️ **Image Analysis**: Upload and analyze images with multimodal AI models
- 🎨 **Image Generation**: Create stunning images with OpenAI or Azure OpenAI DALL-E 3
- 🗣️ **Text-to-Speech**: Convert text to natural-sounding speech
- 🎤 **Audio Transcription**: Transcribe audio files with Whisper models
- 📚 **Document Chat**: Chat with your documents using Google Gemini and ChromaDB
- 📱 **Responsive UI**: Clean, intuitive interface built with Streamlit

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- API keys for:
  - Groq (for chat, image analysis, TTS, and transcription)
  - OpenAI (for image generation with DALL-E 3)
  - Azure OpenAI (for alternative image generation with DALL-E 3)
  - Google Gemini (for document chat)

### 🔑 API Keys

NexusAI requires API keys to function. You can enter these directly in the application's API Setup page:

#### Groq API Key
1. Visit [Groq's website](https://console.groq.com/signup) and create an account
2. Navigate to the API section in your dashboard
3. Generate a new API key
4. Copy the key and add it to the application

#### OpenAI API Key
1. Visit [OpenAI's website](https://platform.openai.com/) and create an account
2. Navigate to the API section in your dashboard
3. Generate a new API key
4. Copy the key and add it to the application

#### Azure OpenAI API Key
1. Create an [Azure account](https://azure.microsoft.com/) if you don't have one
2. Set up an Azure OpenAI resource
3. Deploy a DALL-E 3 model
4. Get your API key, endpoint, and deployment name
5. Add these to the application

#### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and create an account
2. Create a new API key
3. Copy the key and add it to the application

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/NexusAI.git
cd NexusAI
```

2. **Setup and Run (Linux/Mac)**

```bash
# Make the run script executable
chmod +x run.sh

# Run the application
./run.sh
```

3. **Setup and Run (Windows PowerShell)**

```powershell
# You may need to set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Run the application
.\run.ps1
```

The script will:
- Create a virtual environment
- Install required dependencies
- Launch the Streamlit application

The application will be available at `http://localhost:8501` in your web browser.

## 🧩 Features in Detail

### AI Chat
- Engage with advanced language models
- Supports Llama 3 (8B and 70B) and Mixtral models
- Adjustable parameters for temperature and token limits

### Image Analysis
- Upload images in various formats (JPG, PNG, WEBP)
- Analyze images with multimodal AI models
- Customizable analysis prompts

### Image Generation
- Generate images with OpenAI DALL-E 3 or Azure OpenAI DALL-E 3
- Multiple size options (1024x1024, 1792x1024, 1024x1792)
- Download generated images

### Text-to-Speech
- Convert text to natural-sounding speech
- Multiple voice options
- Various output formats (WAV, MP3, AAC, FLAC, PCM)

### Audio Transcription
- Transcribe audio files with Whisper models
- Support for multiple languages
- Word-level timestamps

### Document Chat
- Upload and process documents (PDF, TXT, CSV)
- Chat with your documents using Google Gemini
- Vector storage with ChromaDB
- Source attribution for answers

## 📊 Application Structure

NexusAI is organized into a modular structure:

```
NexusAI/
├── main.py                  # Main application with navigation
├── chat_module.py           # Chat functionality
├── image_analysis_module.py # Image analysis functionality
├── image_generation_module.py # Image generation functionality
├── tts_module.py            # Text-to-speech functionality
├── stt_module.py            # Speech-to-text functionality
├── document_chat_module.py  # Document chat interface
├── document_chat.py         # Document chat backend
├── requirements.txt         # Python dependencies
├── run.sh                   # Linux/Mac launcher script
└── run.ps1                  # Windows PowerShell launcher script
```

## 🔧 Configuration

NexusAI supports various configuration options through model selection dropdowns and parameter sliders in the UI. Key configurable parameters include:

- Chat models (Llama 3, Mixtral)
- Image analysis models
- Image generation providers (OpenAI or Azure OpenAI)
- TTS voices and formats
- Transcription models and languages
- Temperature and other generation parameters
- Document processing options

## 🛠️ Technical Details

NexusAI is built with:

- **Streamlit**: For the web interface
- **Groq API**: For chat, image analysis, TTS, and transcription
- **OpenAI API**: For image generation with DALL-E 3
- **Azure OpenAI API**: For alternative image generation with DALL-E 3
- **Google Gemini API**: For document embeddings and chat
- **ChromaDB**: For vector storage
- **LangChain**: For document processing and retrieval
- **Python libraries**: Including Pillow, requests, and dotenv

For a detailed overview of the system architecture, please see the [ARCHITECTURE.md](ARCHITECTURE.md) document.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Make sure to read the [Code of Conduct](CODE_OF_CONDUCT.md) and [Contributing Guidelines](CONTRIBUTING.md).

## 👨‍💻 Authors

- **Amul Thantharate** - An AI enthusiast passionate about creating innovative solutions. [GitHub](https://github.com/Amul-Thantharate) | [LinkedIn](https://www.linkedin.com/in/amul-thantharate)
- **Avanti Nandanwar** - A dedicated AI developer contributing to this project. [GitHub](https://github.com/Avanti-ui) | [LinkedIn](https://www.linkedin.com/in/avanti-nandanwar-812b79266)

## 🙏 Acknowledgements

- [Groq](https://groq.com/) for their powerful AI APIs
- [OpenAI](https://openai.com/) for DALL-E 3 integration
- [Microsoft Azure](https://azure.microsoft.com/) for Azure OpenAI services
- [Google Gemini](https://ai.google.dev/) for document embeddings and chat
- [Streamlit](https://streamlit.io/) for the amazing web framework
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [LangChain](https://www.langchain.com/) for document processing

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
