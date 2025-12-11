# 🚀 Deployment Guide

This guide will help you deploy your RAG application to free hosting platforms.

## 📋 Pre-Deployment Checklist

- ✅ Test app locally with `streamlit run streamlit_app.py`
- ✅ Get your Groq API key from [console.groq.com](https://console.groq.com)
- ✅ Create a GitHub account (if deploying to Streamlit Cloud)
- ✅ Verify all files are committed to your repository

## 🎯 Option 1: Streamlit Community Cloud (Recommended)

**Advantages**:
- Easiest setup
- Automatic updates from GitHub
- Free tier includes 1GB RAM
- Custom domain support

### Step-by-Step Instructions

#### 1. Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: RAG QA System"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

#### 2. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Select your repository
4. Configure:
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
   - **Python version**: 3.10 (or higher)
5. Click **"Advanced settings"**
6. Add secrets (Environment variables):
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
7. Click **"Deploy"**

Your app will be live at: `https://your-app-name.streamlit.app`

#### 3. Update Your App

Every time you push to GitHub, Streamlit Cloud will automatically redeploy!

```bash
git add .
git commit -m "Update app"
git push
```

---

## 🤗 Option 2: Hugging Face Spaces

**Advantages**:
- GPU support available
- Easy sharing in AI community
- Automatic Docker builds

### Step-by-Step Instructions

#### 1. Create a New Space

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Fill in details:
   - **Owner**: Your username
   - **Space name**: `rag-qa-system` (or your choice)
   - **License**: Apache 2.0 (or your choice)
   - **Select SDK**: **Streamlit**
   - **SDK version**: 1.52.1
   - **Visibility**: Public (free) or Private (Pro)
3. Click **"Create Space"**

#### 2. Prepare Files

Create a `README.md` in your repository with this header:

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
license: apache-2.0
---

# RAG Question Answering System

Ask questions about your documents using AI!

## How to use

1. Enter your Groq API key in the sidebar
2. Upload documents or use the sample data
3. Build the vector store
4. Ask questions!

Get a free API key at [console.groq.com](https://console.groq.com)
```

#### 3. Upload Files

**Option A: Git Clone and Push**

```bash
# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/rag-qa-system
cd rag-qa-system

# Copy your files
cp -r /path/to/your/project/* .

# Push to Hugging Face
git add .
git commit -m "Initial commit"
git push
```

**Option B: Web Interface**

1. Click **"Files and versions"** tab
2. Click **"Add file"** → **"Upload files"**
3. Upload:
   - `streamlit_app.py`
   - `requirements.txt`
   - `src/` folder (all files)
   - `data/` folder (your sample data)
   - `.streamlit/config.toml`
   - `packages.txt`
   - `README.md`

#### 4. Add Secrets

1. Go to **Settings** tab
2. Scroll to **Repository secrets**
3. Click **"New secret"**
4. Add:
   - **Name**: `GROQ_API_KEY`
   - **Value**: Your Groq API key
5. Click **"Add secret"**

**Important**: Update your `streamlit_app.py` to read from secrets:

```python
import os
import streamlit as st

# For Hugging Face Spaces
if 'GROQ_API_KEY' in os.environ:
    groq_api_key = os.environ['GROQ_API_KEY']
else:
    groq_api_key = st.text_input("Groq API Key", type="password")
```

Your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/rag-qa-system`

---

## 🔧 Option 3: Render.com (Alternative)

**Advantages**:
- Free tier available
- Supports Docker
- PostgreSQL database included

### Quick Setup

1. Create a `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Deploy on [Render](https://render.com):
   - Connect your GitHub repository
   - Select "Web Service"
   - Use Docker environment
   - Add environment variables (GROQ_API_KEY)

---

## 🌍 Option 4: Railway.app

**Advantages**:
- $5 free credit monthly
- Simple deployment
- Custom domains

### Quick Setup

1. Go to [railway.app](https://railway.app)
2. Click **"Start a New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your repository
5. Add environment variables:
   - `GROQ_API_KEY`: your_key_here
6. Railway will auto-detect and deploy

---

## 📊 Comparison Table

| Platform | Cost | RAM | Storage | GPU | Custom Domain | Auto-Deploy |
|----------|------|-----|---------|-----|---------------|-------------|
| **Streamlit Cloud** | Free | 1GB | 1GB | ❌ | ✅ | ✅ |
| **HF Spaces** | Free | 16GB | 50GB | ✅ (Paid) | ✅ | ✅ |
| **Render** | Free | 512MB | Limited | ❌ | ✅ | ✅ |
| **Railway** | $5/mo credit | 512MB | 1GB | ❌ | ✅ | ✅ |

---

## 🐛 Troubleshooting

### Build Fails

**Problem**: Dependencies won't install

**Solution**:
```bash
# Pin specific versions in requirements.txt
langchain==1.1.3
streamlit==1.52.1
```

### Out of Memory

**Problem**: App crashes due to memory limits

**Solution**:
- Use smaller embedding models
- Reduce chunk size in `vectorstore.py`
- Use HF Spaces (more RAM)

### Secrets Not Working

**Problem**: API key not found

**Solution**:
```python
# In streamlit_app.py, add fallback:
import os
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
```

### App Won't Start

**Problem**: Streamlit won't run

**Solution**:
- Verify `streamlit_app.py` is in root directory
- Check Python version (3.10+ required)
- Review deployment logs

---

## 🎉 Post-Deployment

### Share Your App

- **Streamlit**: `https://your-app.streamlit.app`
- **HF Spaces**: `https://huggingface.co/spaces/username/app-name`
- **Custom Domain**: Configure in platform settings

### Monitor Usage

- Check deployment logs regularly
- Monitor API usage on Groq dashboard
- Set up error notifications

### Update Your App

```bash
# Make changes locally
git add .
git commit -m "Update: new features"
git push

# App automatically redeploys!
```

---

## 💡 Pro Tips

1. **Use .gitignore**: Don't commit sensitive files
   ```
   .env
   faiss_store/
   __pycache__/
   ```

2. **Add Analytics**: Track usage with Streamlit's built-in analytics

3. **Enable Caching**: Speed up your app
   ```python
   @st.cache_resource
   def load_model():
       return RAGSearch()
   ```

4. **Add Rate Limiting**: Prevent abuse of your API key

5. **Custom Branding**: Add your logo and colors in `.streamlit/config.toml`

---

## 📞 Support

- **Streamlit**: [docs.streamlit.io](https://docs.streamlit.io)
- **Hugging Face**: [huggingface.co/docs/hub](https://huggingface.co/docs/hub)
- **Groq**: [console.groq.com/docs](https://console.groq.com/docs)

Happy Deploying! 🚀
