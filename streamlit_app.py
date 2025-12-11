import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="RAG ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_search" not in st.session_state:
    st.session_state.rag_search = None

# Custom CSS for chat interface
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .chat-container {
        max-height: 600px;
        overflow-y: auto;
    }
    .user-message {
        background-color: #e3f2fd;
        text-align: right;
    }
    .assistant-message {
        background-color: #f5f5f5;
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
    if faiss_path.exists():
        st.success("✅ Ready")
        st.caption("Vector store is loaded and ready")
    else:
        st.warning("⚠️ Not built")
        st.caption("Build the vector store to start chatting")

    # Always show the build button
    if st.button("🔨 Build/Rebuild Store", key="build_vector_store", use_container_width=True):
        with st.spinner("Building vector store..."):
            try:
                from src.data_loader import load_all_documents
                from src.vectorstore import FaissVectorStore

                docs = load_all_documents("data")
                if len(docs) == 0:
                    st.error("No documents found in the 'data' directory!")
                else:
                    store = FaissVectorStore("faiss_store")
                    store.build_from_documents(docs)
                    st.success(f"✅ Built from {len(docs)} documents!")
                    st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")

    st.markdown("---")

    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.rag_search = None
        st.rerun()

    st.markdown("---")

    # Document Upload
    st.header("📁 Upload Documents")
    uploaded_file = st.file_uploader(
        "Add documents",
        type=["txt", "pdf", "csv", "docx", "xlsx", "json"],
        help="Upload a document to add to the knowledge base",
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        # Save uploaded file
        save_path = Path("data") / uploaded_file.name
        save_path.parent.mkdir(exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ Uploaded: {uploaded_file.name}")
        st.info("💡 Rebuild store to include it!")

    st.markdown("---")

    # Stats
    if faiss_path.exists():
        st.caption(f"💬 Chat messages: {len(st.session_state.messages)}")
        data_files = list(Path("data").glob("*.*"))
        st.caption(f"📄 Documents: {len(data_files)}")

# Main chat interface
st.title("🤖 RAG ChatBot")
st.markdown("Ask questions about your documents in a natural conversation!")

# Check if API key is set
if not groq_api_key:
    st.warning("⚠️ Please enter your Groq API Key in the sidebar to start chatting.")
    st.info("Get your free API key at: https://console.groq.com/")
    st.stop()

# Check if vector store exists
if not faiss_path.exists():
    st.error("⚠️ Vector store not built yet!")
    st.info("👈 Use the sidebar to build the vector store from your documents first.")
    st.stop()

# Initialize RAG search if not already done
if st.session_state.rag_search is None:
    try:
        from src.search import RAGSearch
        st.session_state.rag_search = RAGSearch(
            persist_dir="faiss_store",
            llm_model=llm_model
        )
    except Exception as e:
        st.error(f"Error initializing RAG: {str(e)}")
        st.stop()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "timestamp" in message:
            st.caption(message["timestamp"])

# Chat input
if prompt := st.chat_input("Ask a question about your documents..."):
    # Add user message to chat history
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

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Get conversation context (last 3 exchanges)
                context_messages = st.session_state.messages[-6:] if len(st.session_state.messages) > 6 else st.session_state.messages
                conversation_context = "\n".join([
                    f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
                    for msg in context_messages[:-1]  # Exclude current message
                ])

                # Create enhanced query with context
                if conversation_context:
                    enhanced_query = f"Previous conversation:\n{conversation_context}\n\nCurrent question: {prompt}"
                else:
                    enhanced_query = prompt

                # Get answer from RAG
                answer = st.session_state.rag_search.search_and_summarize(
                    enhanced_query,
                    top_k=top_k
                )

                # Display answer
                st.markdown(answer)
                response_timestamp = datetime.now().strftime("%I:%M %p")
                st.caption(response_timestamp)

                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "timestamp": response_timestamp
                })

            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg,
                    "timestamp": datetime.now().strftime("%I:%M %p")
                })

# Show helpful hints if no messages yet
if len(st.session_state.messages) == 0:
    st.info("👋 Welcome! Start by asking a question about your documents.")

    # Sample questions
    st.markdown("### 💡 Sample Questions:")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📄 What documents do you have?", use_container_width=True):
            st.rerun()
        if st.button("🎯 What is attention mechanism?", use_container_width=True):
            st.rerun()

    with col2:
        if st.button("💼 Summarize my work experience", use_container_width=True):
            st.rerun()
        if st.button("🔍 What are my technical skills?", use_container_width=True):
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with ❤️ using Streamlit, LangChain, FAISS, and Groq |
    <a href='https://github.com/engrouneeb/RagChatBot' target='_blank'>View on GitHub</a></p>
</div>
""", unsafe_allow_html=True)
