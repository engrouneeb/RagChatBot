# 📄 How to Upload and Query Your Documents

## 🎯 Quick Guide: Upload Your CV and Ask Questions

### Method 1: Using the Web Interface (Recommended)

#### Step 1: Upload Your Document
1. Open the Streamlit app in your browser
2. Look at the **right side** of the screen
3. Find the section **"📁 Document Upload"**
4. Click **"Browse files"** button
5. Select your CV (PDF, DOCX, TXT, CSV, XLSX, JSON)
6. Click "Open"
7. You'll see: "✅ File uploaded: your-cv.pdf"

#### Step 2: Build the Vector Store
1. Go to the **left sidebar**
2. Scroll to **"📊 Vector Store Status"**
3. Click **"Build Vector Store"** button
4. Wait while it processes (30 seconds to 2 minutes)
5. You'll see: "✅ Vector store built from X documents!"

#### Step 3: Ask Questions About Your CV
1. Enter your **Groq API key** in the sidebar (if not already entered)
2. In the main area, type a question in the text box
3. Click **"🔍 Search & Answer"**
4. Get your AI-powered answer!

---

## 💡 Example Questions for Your CV

### About Experience:
```
- What is my work experience?
- How many years of experience do I have?
- What was my role at [Company Name]?
- What are my key achievements?
- What projects have I worked on?
```

### About Skills:
```
- What are my technical skills?
- What programming languages do I know?
- What tools and technologies am I familiar with?
- What are my soft skills?
```

### About Education:
```
- What is my educational background?
- What degrees do I have?
- Where did I study?
- What certifications do I have?
```

### Summary Questions:
```
- Summarize my professional profile
- What makes me qualified for [Job Title]?
- What are my core competencies?
- Give me an elevator pitch based on my CV
```

---

## 📁 Method 2: Manual Copy to Data Folder

### Mac/Linux:
```bash
# Copy your CV to the data folder
cp ~/Documents/my-cv.pdf data/
cp ~/Downloads/resume.docx data/

# Or use Finder
# 1. Open Finder
# 2. Navigate to your project folder
# 3. Drag your CV into the "data" folder
```

### Windows:
```cmd
# Copy your CV to the data folder
copy "C:\Users\YourName\Documents\my-cv.pdf" data\

# Or use File Explorer
# 1. Open File Explorer
# 2. Navigate to your project folder
# 3. Drag your CV into the "data" folder
```

After copying files manually:
1. Open the Streamlit app
2. Click **"Build Vector Store"** in the sidebar
3. Start asking questions!

---

## 🔄 Workflow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    1. UPLOAD DOCUMENT                        │
│  • Use file uploader in app (right side)                   │
│  • Or copy file to data/ folder manually                    │
│                                                             │
│  Supported formats:                                         │
│  📄 PDF, 📝 DOCX, 📋 TXT, 📊 CSV, 📈 XLSX, 🔧 JSON         │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────────────────────┐
│                  2. BUILD VECTOR STORE                       │
│  • Click "Build Vector Store" button in sidebar             │
│  • System will:                                             │
│    - Load all documents from data/ folder                   │
│    - Split into chunks (1000 chars each)                    │
│    - Create embeddings (vector representations)             │
│    - Store in FAISS database                                │
│  • Wait for: "✅ Vector store built!"                       │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────────────────────┐
│                   3. ASK QUESTIONS                           │
│  • Enter your Groq API key (sidebar)                        │
│  • Type question in main area                               │
│  • Click "🔍 Search & Answer"                               │
│  • Get AI-powered answer in 3-5 seconds!                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎨 Visual Guide: Where to Find Everything

```
┌──────────────────────────────────────────────────────────────────┐
│  Streamlit App Layout                                            │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SIDEBAR (Left)              │  MAIN AREA (Center/Right)         │
│  ═══════════════              │  ═══════════════════════         │
│                               │                                  │
│  ⚙️ Configuration             │  💬 Ask a Question               │
│  ├─ Groq API Key              │  ┌─────────────────────┐        │
│  ├─ LLM Model                 │  │ Your Question       │        │
│  └─ Number of Results         │  └─────────────────────┘        │
│                               │  [🔍 Search & Answer]            │
│  📊 Vector Store Status       │                                  │
│  ├─ ✅ Store loaded           │  📝 Answer appears here          │
│  └─ [Build Vector Store]     │                                  │
│                               │                                  │
│                               │  ─────────────────────           │
│                               │                                  │
│                               │  📚 Sample Questions             │
│                               │  • What is my experience?        │
│                               │  • List my skills                │
│                               │                                  │
│                               │  📁 Document Upload              │
│                               │  [Browse files...]               │
│                               │                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 📝 Supported File Formats

| Format | Extension | Example Use Case |
|--------|-----------|------------------|
| PDF | `.pdf` | CV/Resume, Research papers |
| Word | `.docx` | Cover letters, Reports |
| Text | `.txt` | Notes, Plain text docs |
| CSV | `.csv` | Data tables, Spreadsheets |
| Excel | `.xlsx` | Complex spreadsheets |
| JSON | `.json` | Structured data |

---

## ⚡ Quick Tips

### 1. **Multiple Documents**
You can upload multiple documents at once!
- Upload CV
- Upload cover letter
- Upload portfolio
- Build vector store once
- Ask questions across all documents!

### 2. **Update Documents**
When you add new documents:
- Upload the new file
- Click "Build Vector Store" again
- It will rebuild with ALL documents in data/ folder

### 3. **Better Results**
For best answers:
- Use clear, specific questions
- Increase "Number of Results" (top_k) for complex questions
- Try different phrasings if answer isn't good enough

### 4. **Model Selection**
Choose your LLM model in sidebar:
- **gemma2-9b-it**: Fast, good for simple questions
- **llama-3.3-70b-versatile**: Best quality, comprehensive answers
- **mixtral-8x7b-32768**: Large context window, good for long docs

---

## 🐛 Troubleshooting

### "No module named 'langchain_text_splitters'"
**Fixed!** This was resolved by updating the import in `embedding.py`

### "Vector store not built yet"
**Solution**: Click "Build Vector Store" button in the sidebar

### "No documents found"
**Solution**: Make sure files are in the `data/` folder
```bash
ls data/  # Should show your files
```

### "Failed to load PDF"
**Solution**: Make sure the PDF isn't password-protected or corrupted

### Upload button not visible
**Solution**: Look at the RIGHT side of the screen, scroll down to "📁 Document Upload"

---

## 🎯 Real-World Example: Querying Your CV

Let's say you upload your CV named `john-doe-cv.pdf`:

### Example Workflow:

1. **Upload CV**
   ```
   File: john-doe-cv.pdf (350 KB)
   Status: ✅ File uploaded successfully
   ```

2. **Build Vector Store**
   ```
   [INFO] Building vector store from 1 documents...
   [INFO] Split 1 documents into 5 chunks
   [INFO] Generating embeddings...
   [INFO] Added 5 vectors to FAISS index
   ✅ Vector store built!
   ```

3. **Ask Questions**

   **Question 1:** "What is my work experience?"

   **Answer:**
   ```
   Based on your CV, you have 5 years of professional experience
   as a Software Engineer. You worked at TechCorp from 2019-2022
   as a Senior Developer, where you led a team of 5 engineers and
   built scalable web applications. Currently, you're working at
   StartupXYZ as a Lead Engineer since 2022, focusing on cloud
   architecture and DevOps.
   ```

   **Question 2:** "What are my technical skills?"

   **Answer:**
   ```
   Your technical skills include:
   - Programming Languages: Python, JavaScript, TypeScript, Java
   - Frameworks: React, Node.js, Django, FastAPI
   - Cloud: AWS, Docker, Kubernetes
   - Databases: PostgreSQL, MongoDB, Redis
   - Tools: Git, CI/CD, Jenkins, GitHub Actions
   ```

---

## 🚀 Advanced Usage

### Combine Multiple Documents

Upload multiple files for comprehensive Q&A:

1. **Your CV** - `cv.pdf`
2. **Cover Letter** - `cover-letter.docx`
3. **Portfolio** - `projects.txt`
4. **References** - `references.csv`

Then ask questions like:
- "Create a summary of my professional profile based on all my documents"
- "What project from my portfolio best demonstrates my Python skills?"
- "Combine my CV and cover letter to explain why I'm a good fit for [role]"

### Export Vector Store

The vector store is saved in `faiss_store/` folder:
- You only need to build it once
- It persists across app restarts
- Rebuild when you add new documents

---

## 📞 Need More Help?

Check these guides:
- **Quick Start**: [QUICK_START.md](QUICK_START.md)
- **Full Setup**: [README_SETUP.md](README_SETUP.md)
- **Deployment**: [DEPLOYMENT.md](DEPLOYMENT.md)

---

**Happy document querying! 🎉**
