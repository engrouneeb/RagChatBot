# 🤖 RAG Question Answering System

A production-ready Retrieval Augmented Generation (RAG) system with a beautiful web interface. Upload documents and ask questions - get AI-powered answers based on your content!

## ✨ Features

- 📄 **Multi-format Support**: PDF, TXT, CSV, DOCX, XLSX, JSON
- 🔍 **Semantic Search**: Powered by FAISS vector database
- 🤖 **AI Responses**: Uses Groq's fast LLM models
- 🌐 **Web Interface**: Beautiful Streamlit UI
- ☁️ **Free Deployment**: Deploy on Streamlit Cloud or Hugging Face Spaces
- 🚀 **Fast & Efficient**: Optimized for performance

## 🚀 Quick Start

### Option 1: One-Command Start (Mac/Linux)

```bash
./run_local.sh
```

### Option 2: Manual Start

```bash
# 1. Install dependencies
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Add your Groq API key to .env file
echo "GROQ_API_KEY=your_key_here" > .env

# 3. Run the app
streamlit run streamlit_app.py
```

## 📖 Detailed Setup

See [README_SETUP.md](README_SETUP.md) for complete installation and deployment instructions.

## 🌐 Live Demo

Deploy your own instance:
- **Streamlit Cloud**: [share.streamlit.io](https://share.streamlit.io) (Free)
- **Hugging Face Spaces**: [huggingface.co/spaces](https://huggingface.co/spaces) (Free)

## 📚 How to Use

1. **Get a free API key** from [console.groq.com](https://console.groq.com)
2. **Add documents** to the `data/` folder
3. **Build vector store** using the sidebar button
4. **Ask questions** about your documents
5. **Get AI-powered answers** instantly!

## 🏗️ Architecture

```
User Question → Embedding → Vector Search → Retrieve Context → LLM → Answer
```

- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2)
- **Vector DB**: FAISS (Facebook AI Similarity Search)
- **LLM**: Groq (Gemma2-9B, Llama-3.3-70B, Mixtral-8x7B)
- **Framework**: LangChain + Streamlit

## 📁 Project Structure

```
RAG-Tutorials/
├── streamlit_app.py      # Web interface ⭐
├── app.py                # CLI interface
├── src/                  # Core RAG components
│   ├── data_loader.py    # Document loading
│   ├── embedding.py      # Text embeddings
│   ├── search.py         # RAG search
│   └── vectorstore.py    # FAISS vector store
├── data/                 # Your documents
└── requirements.txt      # Dependencies
```

## 🎯 Use Cases

- 📚 **Document Q&A**: Ask questions about your PDFs, docs
- 🔬 **Research Assistant**: Query research papers
- 📖 **Knowledge Base**: Build a searchable knowledge base
- 🎓 **Study Helper**: Ask questions about textbooks
- 💼 **Business Intelligence**: Query company documents

## 🆓 Free Resources Used

- ✅ Groq API (free tier)
- ✅ Streamlit Cloud (free hosting)
- ✅ FAISS (open source)
- ✅ Sentence Transformers (open source)
- ✅ LangChain (open source)

## 📝 License

See [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions welcome! Feel free to open issues or submit PRs.

---

**Made with ❤️ using LangChain, FAISS, and Groq**