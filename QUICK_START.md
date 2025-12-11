# ⚡ Quick Start Guide

Get your RAG app running in 3 minutes!

## 🏃‍♂️ Super Fast Start

```bash
# 1. Clone or download this repo
cd RAG-Tutorials

# 2. Run the setup script (Mac/Linux)
./run_local.sh

# OR manually (Windows/Mac/Linux):
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🔑 Get Your Free API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up (it's free!)
3. Click "Create API Key"
4. Copy the key

## 📝 Add API Key

**Option 1: In the App** (Easiest)
- Just paste it in the sidebar when the app opens!

**Option 2: .env File** (For local development)
```bash
echo "GROQ_API_KEY=your_key_here" > .env
```

## 📚 Add Your Documents

```bash
# Copy your files to the data folder
cp your-document.pdf data/
cp your-notes.txt data/
cp your-research.docx data/
```

Supported formats: PDF, TXT, DOCX, CSV, XLSX, JSON

## ▶️ Use the App

1. **Open browser** at `http://localhost:8501`
2. **Enter API key** in sidebar
3. **Click "Build Vector Store"** in sidebar (first time only)
4. **Ask a question** like "What is attention mechanism?"
5. **Get instant AI answers!**

## 🌐 Deploy Online (Free)

### Streamlit Cloud (Easiest)

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "My RAG app"
git push

# 2. Go to share.streamlit.io
# 3. Click "New app"
# 4. Select your repo
# 5. Add GROQ_API_KEY in secrets
# 6. Deploy!
```

### Hugging Face Spaces

```bash
# 1. Go to huggingface.co/new-space
# 2. Choose Streamlit SDK
# 3. Upload files
# 4. Add GROQ_API_KEY secret
# 5. Done!
```

## 🆘 Common Issues

**"No module named 'streamlit'"**
```bash
pip install -r requirements.txt
```

**"Vector store not built"**
- Click "Build Vector Store" in the sidebar

**"GROQ_API_KEY not found"**
- Enter it in the sidebar OR create .env file

**"No documents found"**
- Add files to the `data/` folder

## 📞 Need Help?

Check these files:
- **Full Setup**: [README_SETUP.md](README_SETUP.md)
- **Deployment**: [DEPLOYMENT.md](DEPLOYMENT.md)
- **Main README**: [README.md](README.md)

## 🎯 Next Steps

1. ✅ Try the sample data (already included!)
2. ✅ Add your own documents
3. ✅ Customize the UI in `streamlit_app.py`
4. ✅ Deploy online to share with others
5. ✅ Star the repo if you find it useful!

---

**That's it! You're ready to go! 🚀**
