# 🤖 Groq LLM Models Guide

## 🎯 Available Models (Updated)

### 1. **llama-3.3-70b-versatile** ⭐ Default & Recommended
- **Size**: 70 billion parameters
- **Speed**: Fast (optimized by Groq)
- **Quality**: Excellent, comprehensive answers
- **Context**: 128k tokens
- **Best For**:
  - Complex questions requiring detailed answers
  - Professional documents (CVs, reports)
  - Multi-step reasoning
  - High-quality summaries
- **Use When**: You need the best quality answers

### 2. **mixtral-8x7b-32768**
- **Size**: 8x7B Mixture of Experts
- **Speed**: Very fast
- **Quality**: Great balance of speed and quality
- **Context**: 32,768 tokens (32k)
- **Best For**:
  - Long documents
  - Large context windows needed
  - Multiple document queries
  - Good quality with fast response
- **Use When**: You have very long documents or need large context

### 3. **llama-3.1-8b-instant**
- **Size**: 8 billion parameters
- **Speed**: Ultra fast (instant responses)
- **Quality**: Good for straightforward questions
- **Context**: 128k tokens
- **Best For**:
  - Simple Q&A
  - Quick lookups
  - Factual questions
  - When speed is priority
- **Use When**: You need instant responses for simple questions

---

## 📊 Model Comparison

| Model | Speed | Quality | Context | Best Use Case |
|-------|-------|---------|---------|---------------|
| **llama-3.3-70b-versatile** | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 128k | Professional docs, complex Q&A |
| **mixtral-8x7b-32768** | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 32k | Long documents, good balance |
| **llama-3.1-8b-instant** | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | 128k | Quick answers, simple queries |

---

## 🎨 When to Use Which Model

### Use **llama-3.3-70b-versatile** for:
```
✅ Analyzing CVs and resumes
✅ Professional document Q&A
✅ Complex research papers
✅ Detailed explanations needed
✅ Multi-aspect questions
✅ High-stakes answers (interviews, reports)
```

**Example Questions:**
- "Summarize my professional experience and highlight key achievements"
- "What makes me qualified for a senior developer position?"
- "Explain the methodology used in this research paper"

### Use **mixtral-8x7b-32768** for:
```
✅ Very long documents (> 10,000 words)
✅ Multiple document analysis
✅ Code documentation
✅ Technical manuals
✅ When you need large context window
```

**Example Questions:**
- "Compare the approaches mentioned across all three research papers"
- "What are the common themes in these 5 articles?"
- "Analyze this 50-page technical manual"

### Use **llama-3.1-8b-instant** for:
```
✅ Quick factual lookups
✅ Simple yes/no questions
✅ Extracting specific information
✅ When speed matters most
✅ High-volume queries
```

**Example Questions:**
- "What is my email address?"
- "How many years of experience do I have?"
- "List my technical skills"
- "What university did I attend?"

---

## 🔄 How to Change Models

### In the Streamlit App:
1. Look at the **left sidebar**
2. Find **"⚙️ Configuration"**
3. Under **"LLM Model"** dropdown
4. Select your preferred model
5. The change takes effect immediately!

### In Code:
```python
# Option 1: When initializing RAGSearch
rag_search = RAGSearch(
    persist_dir="faiss_store",
    llm_model="llama-3.3-70b-versatile"  # Change model here
)

# Option 2: In streamlit_app.py
llm_model = st.selectbox(
    "LLM Model",
    ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama-3.1-8b-instant"]
)
```

---

## 🚫 Decommissioned Models

These models are **NO LONGER AVAILABLE**:
- ❌ `gemma2-9b-it` - Decommissioned
- ❌ `gemma-7b-it` - Decommissioned
- ❌ Old Llama 2 models - Replaced by Llama 3.x

If you see errors about these models, update to one of the models listed above.

---

## 💰 Pricing & Rate Limits (Free Tier)

All models on Groq's free tier:
- **Rate Limit**: 30 requests per minute
- **Daily Limit**: 6,000 requests per day
- **Cost**: FREE ✨

**Tips to Stay Within Limits:**
1. Cache common questions
2. Use smaller models for simple queries
3. Batch similar questions together
4. Optimize `top_k` (number of results retrieved)

---

## 🎯 Recommendations by Use Case

### For CV/Resume Analysis:
```
🥇 First Choice: llama-3.3-70b-versatile
🥈 Second Choice: mixtral-8x7b-32768
🥉 Third Choice: llama-3.1-8b-instant
```

### For Research Papers:
```
🥇 First Choice: llama-3.3-70b-versatile
🥈 Second Choice: mixtral-8x7b-32768 (if very long)
```

### For Quick Lookups:
```
🥇 First Choice: llama-3.1-8b-instant
🥈 Second Choice: llama-3.3-70b-versatile
```

### For Long Documents (> 20 pages):
```
🥇 First Choice: mixtral-8x7b-32768
🥈 Second Choice: llama-3.3-70b-versatile
```

---

## 🔧 Troubleshooting

### "Model has been decommissioned"
**Solution**: Update to a current model:
```python
# OLD (doesn't work anymore)
llm_model = "gemma2-9b-it"

# NEW (works!)
llm_model = "llama-3.3-70b-versatile"
```

### "Rate limit exceeded"
**Solution**:
1. Wait 1 minute (rate limit resets)
2. Use a smaller model for less critical queries
3. Reduce number of requests

### "Context too large"
**Solution**:
1. Use `mixtral-8x7b-32768` (largest context window)
2. Reduce `chunk_size` in vectorstore
3. Lower `top_k` (retrieve fewer results)

---

## 🆕 Latest Updates

**December 2024:**
- ✅ Llama 3.3 70B added (best quality)
- ✅ Llama 3.1 8B instant (fastest)
- ❌ Gemma 2 9B retired

**What Changed:**
- Default model changed from `gemma2-9b-it` to `llama-3.3-70b-versatile`
- Better quality answers with Llama 3.3
- Faster responses with Llama 3.1 instant

---

## 📚 Additional Resources

- **Groq Console**: [console.groq.com](https://console.groq.com)
- **Model Docs**: [console.groq.com/docs/models](https://console.groq.com/docs/models)
- **API Reference**: [console.groq.com/docs/api-reference](https://console.groq.com/docs/api-reference)
- **Rate Limits**: [console.groq.com/docs/rate-limits](https://console.groq.com/docs/rate-limits)

---

**Updated: December 2024** 🚀
