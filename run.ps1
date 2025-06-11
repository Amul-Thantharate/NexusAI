# NexusAI PowerShell Launcher Script
Write-Host "🤖 Starting NexusAI..." -ForegroundColor Cyan
Write-Host "------------------------------" -ForegroundColor Cyan

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python is not installed or not in PATH. Please install Python and try again." -ForegroundColor Red
    exit 1
}

# Check Python version
$pythonVersion = python --version
Write-Host "✅ Found $pythonVersion" -ForegroundColor Green

# Check if virtual environment exists
if (-not (Test-Path -Path ".\venv")) {
    Write-Host "🔧 Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    if (-not $?) {
        Write-Host "❌ Failed to create virtual environment. Please install venv package and try again." -ForegroundColor Red
        exit 1
    }
}

# Activate virtual environment
Write-Host "🔄 Activating virtual environment..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
if (-not $?) {
    Write-Host "❌ Failed to activate virtual environment." -ForegroundColor Red
    exit 1
}

# Install requirements
Write-Host "📦 Installing requirements..." -ForegroundColor Yellow
pip install -r requirements.txt
if (-not $?) {
    Write-Host "❌ Failed to install requirements." -ForegroundColor Red
    exit 1
}

# Run the application
Write-Host "🚀 Launching NexusAI..." -ForegroundColor Green
Write-Host "------------------------------" -ForegroundColor Cyan
streamlit run main.py

# Deactivate virtual environment when done
deactivate
