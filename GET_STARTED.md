# 🎯 GET STARTED - Your Complete Guide

Welcome! This guide will walk you through everything you need to know.

## 📚 Documentation Map

Choose the guide that fits your needs:

| Guide | Best For | Time Needed |
|-------|----------|-------------|
| **[QUICK_START.md](QUICK_START.md)** | Just want to run it now! | 3 minutes |
| **[README_SETUP.md](README_SETUP.md)** | Detailed local setup | 15 minutes |
| **[DEPLOYMENT.md](DEPLOYMENT.md)** | Deploy online | 10 minutes |
| **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** | Understand what's built | 5 minutes |
| **This file** | Complete walkthrough | 20 minutes |

## 🎬 Complete Walkthrough

### Step 1: Understand What This Is (2 min)

This is a **RAG (Retrieval Augmented Generation) Question Answering System** that:

1. **Loads your documents** (PDFs, Word docs, text files, etc.)
2. **Converts them to embeddings** (vector representations)
3. **Stores in a vector database** (FAISS)
4. **Answers your questions** using retrieved context + AI

**Example:**
- You upload a PDF about machine learning
- You ask: "What is attention mechanism?"
- The system finds relevant sections
- AI generates an answer based on YOUR document

### Step 2: Install Prerequisites (5 min)

#### Required:
- **Python 3.10+**
  ```bash
  python3 --version  # Should be 3.10 or higher
  ```

#### Get Your Free API Key:
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (it's FREE!)
3. Click "API Keys" → "Create API Key"
4. **Copy the key** - you'll need it!

### Step 3: Set Up Locally (5 min)

#### Mac/Linux (Easy Way):
```bash
cd RAG-Tutorials
./run_local.sh
```

#### Windows/Mac/Linux (Manual Way):
```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate it
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 3. Install packages
pip install -r requirements.txt

# 4. Run the app
streamlit run streamlit_app.py
```

The app will open at: `http://localhost:8501`

### Step 4: Configure the App (2 min)

#### Option A: Use the Sidebar (Easiest)
1. Open the app in your browser
2. Look at the left sidebar
3. Paste your Groq API key in the text box
4. Done!

#### Option B: Use .env File (For Development)
1. Open the `.env` file
2. Replace `your_groq_api_key_here` with your actual key:
   ```
   GROQ_API_KEY=gsk_your_actual_key_here
   ```
3. Save the file

### Step 5: Add Your Documents (2 min)

#### Use Sample Data:
A sample document is already in `data/sample.txt` - you can start right away!

#### Add Your Own Documents:
```bash
# Copy files to the data folder
cp ~/Documents/myfile.pdf data/
cp ~/Documents/notes.txt data/
cp ~/Documents/research.docx data/
```

**Supported formats:**
- 📄 PDF (`.pdf`)
- 📝 Text (`.txt`)
- 📊 CSV (`.csv`)
- 📄 Word (`.docx`)
- 📈 Excel (`.xlsx`)
- 🔧 JSON (`.json`)

### Step 6: Build the Knowledge Base (1 min)

1. In the app sidebar, click **"Build Vector Store"**
2. Wait while it processes (may take 30 seconds to 2 minutes)
3. You'll see "✅ Vector store built from X documents!"

**What's happening?**
- Documents are split into chunks
- Each chunk is converted to embeddings
- Embeddings are stored in FAISS database

### Step 7: Ask Questions! (1 min)

1. Type a question in the main area
2. Click "🔍 Search & Answer"
3. Wait 3-5 seconds
4. Get your AI-powered answer!

**Try these sample questions:**
- "What is attention mechanism?"
- "How does self-attention work?"
- "What are the applications of attention?"
- "Explain the benefits of attention mechanisms"

### Step 8: Deploy Online (10 min)

Choose your platform:

#### 🟢 Streamlit Cloud (Recommended - Easiest)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "My RAG app"
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. **Deploy:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Main file: `streamlit_app.py`
   - Click "Advanced settings"
   - Add secret: `GROQ_API_KEY = "your_key"`
   - Click "Deploy"

3. **Share:**
   Your app is now live at: `https://your-app.streamlit.app`

#### 🤗 Hugging Face Spaces (More Features)

1. **Create Space:**
   - Go to [huggingface.co/new-space](https://huggingface.co/new-space)
   - Choose Streamlit SDK
   - Name your space

2. **Upload Files:**
   - Upload all files from your project
   - Or clone and push via Git

3. **Add Secrets:**
   - Settings → Repository secrets
   - Add `GROQ_API_KEY`

4. **Share:**
   Your app is live at: `https://huggingface.co/spaces/username/app-name`

## 🎨 Customization Ideas

### Easy Customizations:

1. **Change Colors:**
   Edit `.streamlit/config.toml`:
   ```toml
   [theme]
   primaryColor = "#FF4B4B"  # Change to your color
   ```

2. **Change App Title:**
   Edit `streamlit_app.py` line 12:
   ```python
   st.title("🤖 Your Custom Title")
   ```

3. **Add Logo:**
   ```python
   st.sidebar.image("your-logo.png")
   ```

### Advanced Customizations:

1. **Use Different LLM:**
   Edit `src/search.py` to use OpenAI, Anthropic, etc.

2. **Change Embedding Model:**
   Edit `src/vectorstore.py` line 16:
   ```python
   self.model = SentenceTransformer("your-model-name")
   ```

3. **Add Chat History:**
   Use `st.session_state` to store conversation history

## 🐛 Troubleshooting

### Common Issues:

**1. "ModuleNotFoundError: No module named 'streamlit'"**

**Solution:**
```bash
pip install -r requirements.txt
```

**2. "Vector store not built yet"**

**Solution:**
- Click "Build Vector Store" in the sidebar
- Make sure you have files in `data/` folder

**3. "GROQ_API_KEY not found"**

**Solution:**
- Enter key in sidebar, OR
- Add to `.env` file

**4. "Failed to load PDF"**

**Solution:**
- Install additional dependencies:
  ```bash
  pip install pypdf pymupdf
  ```

**5. App is slow**

**Solutions:**
- Use smaller documents
- Reduce `chunk_size` in `vectorstore.py`
- Use faster embedding model
- Deploy to platform with more RAM

**6. Out of memory**

**Solutions:**
- Reduce number of documents
- Use smaller embedding model
- Deploy to Hugging Face Spaces (16GB RAM)

## 📊 Understanding the Architecture

```
┌──────────────────────────────────────────────────────┐
│                    USER INTERFACE                     │
│              (Streamlit Web App)                     │
│  • Upload documents                                  │
│  • Ask questions                                     │
│  • View answers                                      │
└─────────────────────┬────────────────────────────────┘
                      │
                      ↓
┌──────────────────────────────────────────────────────┐
│              DOCUMENT PROCESSING                      │
│                                                       │
│  1. Load documents (data_loader.py)                  │
│     • PDF, DOCX, TXT, CSV, XLSX, JSON               │
│                                                       │
│  2. Split into chunks (embedding.py)                 │
│     • Default: 1000 chars, 200 overlap              │
│                                                       │
│  3. Create embeddings (sentence-transformers)        │
│     • Model: all-MiniLM-L6-v2                       │
│     • Output: 384-dimension vectors                  │
└─────────────────────┬────────────────────────────────┘
                      │
                      ↓
┌──────────────────────────────────────────────────────┐
│              VECTOR STORAGE (FAISS)                   │
│                                                       │
│  • Stores embeddings + metadata                      │
│  • Fast similarity search (< 100ms)                  │
│  • Persisted to disk (faiss_store/)                 │
└─────────────────────┬────────────────────────────────┘
                      │
                      ↓
┌──────────────────────────────────────────────────────┐
│              QUESTION ANSWERING                       │
│                                                       │
│  1. User asks question                               │
│  2. Question → embedding                             │
│  3. Search FAISS for similar chunks                  │
│  4. Retrieve top K results                           │
│  5. Send to Groq LLM with context                   │
│  6. Return AI-generated answer                       │
└──────────────────────────────────────────────────────┘
```

## 💡 Best Practices

### For Best Results:

1. **Document Quality:**
   - Use well-formatted documents
   - Clear headings and structure
   - Avoid scanned PDFs with poor OCR

2. **Chunk Size:**
   - Default (1000 chars) works for most cases
   - Increase for technical docs with long explanations
   - Decrease for FAQ-style content

3. **Number of Results (top_k):**
   - Start with 3-5 results
   - Increase if answers lack context
   - Decrease if answers are too generic

4. **Model Selection:**
   - `gemma2-9b-it`: Fast, good for simple questions
   - `llama-3.3-70b-versatile`: Best quality, slower
   - `mixtral-8x7b-32768`: Large context window

### Production Tips:

1. **Add Monitoring:**
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   ```

2. **Cache Results:**
   ```python
   @st.cache_data
   def search_documents(query):
       # Your search code
   ```

3. **Rate Limiting:**
   Implement to prevent API abuse

4. **Error Handling:**
   Add try-catch blocks for robustness

## 🎓 Learning Path

### Beginner:
1. Run the app locally
2. Try sample questions
3. Upload your own documents
4. Deploy to Streamlit Cloud

### Intermediate:
1. Customize the UI
2. Try different LLM models
3. Adjust chunk sizes
4. Add new features (chat history, etc.)

### Advanced:
1. Implement hybrid search
2. Add re-ranking
3. Use custom embedding models
4. Build conversation memory
5. Add evaluation metrics

## 📞 Getting Help

### Documentation:
- **Quick Start**: [QUICK_START.md](QUICK_START.md)
- **Setup Guide**: [README_SETUP.md](README_SETUP.md)
- **Deployment**: [DEPLOYMENT.md](DEPLOYMENT.md)
- **Project Info**: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

### External Resources:
- **Streamlit**: [docs.streamlit.io](https://docs.streamlit.io)
- **LangChain**: [python.langchain.com](https://python.langchain.com)
- **Groq**: [console.groq.com/docs](https://console.groq.com/docs)
- **FAISS**: [faiss.ai](https://faiss.ai)

### Community:
- **Streamlit Forum**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **LangChain Discord**: [discord.gg/langchain](https://discord.gg/langchain)

## 🎉 Success Checklist

Mark these off as you complete them:

- [ ] Installed Python 3.10+
- [ ] Got Groq API key
- [ ] Created virtual environment
- [ ] Installed dependencies
- [ ] Added API key to app
- [ ] Added sample documents
- [ ] Built vector store
- [ ] Asked first question
- [ ] Got AI answer
- [ ] Deployed online
- [ ] Shared with others

## 🚀 What's Next?

Now that you're set up:

1. **Use it for real work:**
   - Upload your research papers
   - Add company documentation
   - Index your notes

2. **Customize it:**
   - Add your branding
   - Change colors and layout
   - Add new features

3. **Share it:**
   - Deploy to the cloud
   - Share with your team
   - Add to your portfolio

4. **Learn more:**
   - Explore LangChain docs
   - Try advanced RAG techniques
   - Build new features

## 🎊 Congratulations!

You now have a fully functional RAG system that you can:
- ✅ Run locally
- ✅ Deploy for free
- ✅ Customize completely
- ✅ Scale as needed

**Go build something amazing! 🚀**

---

*Questions? Check the other guides or create an issue on GitHub!*
