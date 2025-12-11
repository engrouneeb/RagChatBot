#!/bin/bash

# Quick start script for running the RAG application locally

echo "🚀 Starting RAG Application..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please create a .env file with your GROQ_API_KEY"
    echo ""
fi

# Check if data directory has files
if [ -z "$(ls -A data)" ]; then
    echo "⚠️  Warning: No documents found in data/ directory"
    echo "Please add some documents to the data/ folder"
    echo ""
fi

# Run Streamlit app
echo "🌐 Starting Streamlit app..."
echo "The app will open at http://localhost:8501"
echo ""
streamlit run streamlit_app.py
