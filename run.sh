#!/bin/bash

# NexusAI Launcher Script
echo "🤖 Starting NexusAI..."
echo "------------------------------"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Failed to create virtual environment. Please install venv package and try again."
        exit 1
    fi
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "❌ Failed to activate virtual environment."
    exit 1
fi

# Install requirements
echo "📦 Installing requirements..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install requirements."
    exit 1
fi

# Run the application
echo "🚀 Launching NexusAI..."
echo "------------------------------"
streamlit run main.py

# Deactivate virtual environment when done
deactivate
