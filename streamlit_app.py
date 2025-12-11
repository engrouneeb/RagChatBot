import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import time

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="RAG ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_search" not in st.session_state:
    st.session_state.rag_search = None

if "show_upload" not in st.session_state:
    st.session_state.show_upload = False

# Custom CSS
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .upload-section {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .doc-card {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")

    # API Key input
    groq_api_key = st.text_input(
        "Groq API Key",
        value=os.getenv("GROQ_API_KEY", ""),
        type="password",
        help="Get your API key from https://console.groq.com/"
    )

    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key

    st.markdown("---")

    # Model selection
    llm_model = st.selectbox(
        "🤖 LLM Model",
        ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama-3.1-8b-instant"],
        help="Select the language model to use"
    )

    # Number of results
    top_k = st.slider("📊 Context Chunks", min_value=1, max_value=10, value=5,
                      help="Number of relevant document chunks to retrieve")

    st.markdown("---")

    # Vector store status
    st.header("📊 Vector Store")
    faiss_path = Path("faiss_store/faiss.index")

    # Show documents in vector store
    if faiss_path.exists():
        st.success("✅ Ready")
        data_files = list(Path("data").glob("*.*"))
        st.metric("Documents", len(data_files))

        if len(data_files) > 0:
            with st.expander("📄 View Documents"):
                for file in data_files:
                    file_size = file.stat().st_size / 1024  # KB
                    st.text(f"• {file.name} ({file_size:.1f} KB)")
    else:
        st.warning("⚠️ Not built")
        st.caption("Upload documents and build the store")

    # Build vector store button
    if st.button("🔨 Build/Rebuild Vector Store", key="build_vector_store",
                 use_container_width=True, type="primary"):
        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            status_text.text("📂 Loading documents...")
            progress_bar.progress(20)

            from src.data_loader import load_all_documents
            from src.vectorstore import FaissVectorStore

            docs = load_all_documents("data")

            if len(docs) == 0:
                st.error("❌ No documents found in the 'data' directory!")
                st.info("👆 Upload some documents first!")
            else:
                status_text.text(f"📝 Processing {len(docs)} documents...")
                progress_bar.progress(40)

                status_text.text("🔢 Creating embeddings...")
                progress_bar.progress(60)

                store = FaissVectorStore("faiss_store")
                store.build_from_documents(docs)

                status_text.text("💾 Saving vector store...")
                progress_bar.progress(80)

                time.sleep(0.5)
                progress_bar.progress(100)
                status_text.text("✅ Complete!")

                st.success(f"✅ Vector store built from {len(docs)} documents!")
                time.sleep(1)
                st.rerun()

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            progress_bar.empty()
            status_text.empty()

    st.markdown("---")

    # Clear chat button
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.session_state.rag_search = None
        st.success("Chat cleared!")
        time.sleep(0.5)
        st.rerun()

    st.markdown("---")

    # Chat Stats
    if len(st.session_state.messages) > 0:
        st.metric("💬 Messages", len(st.session_state.messages))

    # Footer
    st.markdown("---")
    st.caption("Built with Streamlit, LangChain, FAISS & Groq")

# Main area
st.title("🤖 RAG ChatBot")
st.markdown("Chat with your documents using AI - powered by Groq LLM")

# Check API key
if not groq_api_key:
    st.warning("⚠️ Please enter your Groq API Key in the sidebar")
    st.info("👉 Get your free API key at: https://console.groq.com/")

    with st.expander("ℹ️ How to get API key"):
        st.markdown("""
        1. Visit [console.groq.com](https://console.groq.com/)
        2. Sign up for a free account
        3. Go to API Keys section
        4. Create a new API key
        5. Copy and paste it in the sidebar
        """)
    st.stop()

# Check vector store
if not faiss_path.exists():
    st.error("⚠️ Vector store not built yet!")
    st.info("👈 Upload documents in the sidebar, then click 'Build Vector Store'")
    st.session_state.show_upload = True

# Document Upload Section (collapsible in main area)
with st.expander("📤 Upload Documents", expanded=st.session_state.show_upload):
    st.markdown("### Upload Your Documents")
    st.markdown("Supported formats: PDF, TXT, CSV, DOCX, XLSX, JSON")

    # File uploader with multiple files
    uploaded_files = st.file_uploader(
        "Choose files",
        type=["txt", "pdf", "csv", "docx", "xlsx", "json"],
        accept_multiple_files=True,
        help="Select one or more documents to upload"
    )

    if uploaded_files:
        st.markdown(f"**📁 {len(uploaded_files)} file(s) selected**")

        # Show upload progress
        upload_progress = st.progress(0)
        upload_status = st.empty()

        uploaded_count = 0
        total_files = len(uploaded_files)

        for idx, uploaded_file in enumerate(uploaded_files):
            # Save file
            save_path = Path("data") / uploaded_file.name
            save_path.parent.mkdir(exist_ok=True)

            upload_status.text(f"📥 Uploading {uploaded_file.name}...")

            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            uploaded_count += 1
            progress = int((uploaded_count / total_files) * 100)
            upload_progress.progress(progress)

            time.sleep(0.2)  # Visual feedback

        upload_status.empty()
        upload_progress.empty()

        st.success(f"✅ Successfully uploaded {uploaded_count} file(s)!")

        # Show uploaded files
        st.markdown("**📄 Uploaded Files:**")
        for file in uploaded_files:
            file_size = len(file.getvalue()) / 1024  # KB
            st.markdown(f"- **{file.name}** ({file_size:.1f} KB)")

        st.info("💡 **Next Step:** Click 'Build/Rebuild Vector Store' in the sidebar to process these documents")
        st.session_state.show_upload = False

# Initialize RAG search
if faiss_path.exists() and st.session_state.rag_search is None:
    try:
        with st.spinner("🔄 Initializing RAG system..."):
            from src.search import RAGSearch
            st.session_state.rag_search = RAGSearch(
                persist_dir="faiss_store",
                llm_model=llm_model
            )
    except Exception as e:
        st.error(f"❌ Error initializing RAG: {str(e)}")
        st.stop()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "timestamp" in message:
            st.caption(message["timestamp"])

# Chat input
if prompt := st.chat_input("💬 Ask a question about your documents...",
                           disabled=not faiss_path.exists()):
    # Add user message
    timestamp = datetime.now().strftime("%I:%M %p")
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "timestamp": timestamp
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(timestamp)

    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        with st.spinner("🤔 Thinking..."):
            try:
                # Get conversation context
                context_messages = st.session_state.messages[-6:] if len(st.session_state.messages) > 6 else st.session_state.messages
                conversation_context = "\n".join([
                    f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
                    for msg in context_messages[:-1]
                ])

                # Enhanced query with context
                if conversation_context:
                    enhanced_query = f"Previous conversation:\n{conversation_context}\n\nCurrent question: {prompt}"
                else:
                    enhanced_query = prompt

                # Get answer
                answer = st.session_state.rag_search.search_and_summarize(
                    enhanced_query,
                    top_k=top_k
                )

                # Display answer
                message_placeholder.markdown(answer)
                response_timestamp = datetime.now().strftime("%I:%M %p")
                st.caption(response_timestamp)

                # Save to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "timestamp": response_timestamp
                })

            except Exception as e:
                error_msg = f"❌ Sorry, I encountered an error: {str(e)}"
                message_placeholder.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg,
                    "timestamp": datetime.now().strftime("%I:%M %p")
                })

# Welcome message and sample questions
if len(st.session_state.messages) == 0 and faiss_path.exists():
    st.info("👋 **Welcome!** Start by asking a question about your documents.")

    st.markdown("### 💡 Sample Questions:")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📄 What documents do I have?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "What documents do I have?",
                "timestamp": datetime.now().strftime("%I:%M %p")
            })
            st.rerun()

    with col2:
        if st.button("💼 Summarize my experience", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "Summarize my work experience",
                "timestamp": datetime.now().strftime("%I:%M %p")
            })
            st.rerun()

    with col3:
        if st.button("🔍 What are my skills?", use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": "What are my technical skills?",
                "timestamp": datetime.now().strftime("%I:%M %p")
            })
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 14px;'>
    <p>🤖 Built with Streamlit, LangChain, FAISS, and Groq |
    <a href='https://github.com/engrouneeb/RagChatBot' target='_blank' style='color: #4CAF50;'>⭐ View on GitHub</a></p>
</div>
""", unsafe_allow_html=True)
