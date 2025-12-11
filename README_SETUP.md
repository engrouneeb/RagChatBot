# RAG Tutorial - Setup Guide

This guide will help you run the RAG (Retrieval Augmented Generation) application locally and deploy it online.

## 📋 Prerequisites

- Python 3.10 or higher
- Groq API Key (free tier available at [https://console.groq.com/](https://console.groq.com/))

## 🚀 Quick Start - Local Setup

### 1. Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 2. Configure Environment Variables

1. Copy the `.env` file and add your API key:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

2. Get a free Groq API key:
   - Go to [https://console.groq.com/](https://console.groq.com/)
   - Sign up for a free account
   - Create an API key
   - Copy it to your `.env` file

### 3. Add Your Documents

Place your documents in the `data/` folder. Supported formats:
- PDF (`.pdf`)
- Text files (`.txt`)
- CSV (`.csv`)
- Word documents (`.docx`)
- Excel files (`.xlsx`)
- JSON (`.json`)

A sample document is already included in `data/sample.txt`.

### 4. Run the Streamlit App

```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Run the app
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

### 5. Using the App

1. **Enter your Groq API Key** in the sidebar
2. **Build the vector store** by clicking "Build Vector Store" in the sidebar
3. **Ask questions** about your documents in the main area
4. **Upload additional documents** using the file uploader

## 🌐 Deploy to Free Hosting

### Option 1: Streamlit Community Cloud (Recommended)

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Add RAG application"
   git push origin main
   ```

2. **Deploy on Streamlit**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `streamlit_app.py`
   - Click "Deploy"

3. **Add Secrets** (in Streamlit Cloud dashboard):
   - Go to App Settings → Secrets
   - Add your API key:
     ```toml
     GROQ_API_KEY = "your_groq_api_key_here"
     ```

### Option 2: Hugging Face Spaces

1. **Create a new Space**:
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose "Streamlit" as the SDK
   - Name your space

2. **Upload files**:
   - Upload `streamlit_app.py`, `requirements.txt`, and the `src/` folder
   - Create a `README.md` with:
     ```yaml
     ---
     title: RAG QA System
     emoji: 🤖
     colorFrom: blue
     colorTo: green
     sdk: streamlit
     sdk_version: 1.52.1
     app_file: streamlit_app.py
     pinned: false
     ---
     ```

3. **Add secrets**:
   - Go to Settings → Repository secrets
   - Add `GROQ_API_KEY` with your API key

## 🔧 Alternative: Command Line Usage

You can also use the RAG system from the command line:

```bash
# Activate virtual environment
source venv/bin/activate

# Run the example script
python app.py
```

## 📚 Project Structure

```
RAG-Tutorials/
├── data/                    # Your documents go here
│   └── sample.txt          # Sample document
├── src/                     # Source code
│   ├── data_loader.py      # Document loading
│   ├── embedding.py        # Text embedding
│   ├── search.py           # RAG search
│   └── vectorstore.py      # FAISS vector store
├── faiss_store/            # Vector database (auto-generated)
├── streamlit_app.py        # Web interface
├── app.py                  # Command line interface
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (you create this)
```

## 🎯 Features

- **Multi-format document support**: PDF, TXT, CSV, DOCX, XLSX, JSON
- **Semantic search**: Uses sentence transformers for embeddings
- **Fast retrieval**: FAISS vector database for efficient search
- **AI-powered answers**: Groq LLM for generating responses
- **Web interface**: Easy-to-use Streamlit UI
- **Free deployment**: Deploy on Streamlit Cloud or Hugging Face Spaces

## 🐛 Troubleshooting

### "Vector store not built yet"
- Click "Build Vector Store" in the sidebar
- Make sure you have documents in the `data/` folder

### "GROQ_API_KEY not found"
- Make sure you've added your API key to the `.env` file
- Or enter it directly in the Streamlit sidebar

### Dependencies installation fails
- Make sure you're using Python 3.10 or higher
- Try upgrading pip: `pip install --upgrade pip`

### Port already in use
- Streamlit default port is 8501
- Run on a different port: `streamlit run streamlit_app.py --server.port 8502`

## 📖 How It Works

1. **Document Loading**: Loads documents from the `data/` folder
2. **Text Chunking**: Splits documents into smaller chunks
3. **Embedding**: Converts chunks to vector embeddings
4. **Vector Store**: Stores embeddings in FAISS for fast retrieval
5. **Query Processing**: Converts your question to an embedding
6. **Retrieval**: Finds most relevant document chunks
7. **Generation**: Uses Groq LLM to generate an answer based on retrieved context

## 🔑 Free Resources

- **Groq API**: Free tier with generous limits
- **Streamlit Cloud**: Free hosting for public apps
- **Hugging Face Spaces**: Free hosting with GPU options
- **FAISS**: Free, open-source vector database
- **Sentence Transformers**: Free, open-source embeddings

## 🎉 Next Steps

1. Add your own documents to the `data/` folder
2. Customize the UI in `streamlit_app.py`
3. Try different LLM models (available in sidebar)
4. Deploy your app to share with others
5. Add more features like chat history, file management, etc.

Happy building! 🚀
