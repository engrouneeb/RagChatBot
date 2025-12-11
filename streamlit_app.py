import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="RAG Question Answering System",
    page_icon="🤖",
    layout="wide"
)

# Title and description
st.title("🤖 RAG Question Answering System")
st.markdown("""
This application uses Retrieval Augmented Generation (RAG) to answer questions based on your documents.
Upload documents or use the sample data to get started!
""")

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

    # Model selection
    llm_model = st.selectbox(
        "LLM Model",
        ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama-3.1-8b-instant"],
        help="Select the language model to use"
    )

    # Number of results
    top_k = st.slider("Number of Results", min_value=1, max_value=10, value=3)

    # Vector store status
    st.header("📊 Vector Store Status")
    faiss_path = Path("faiss_store/faiss.index")
    if faiss_path.exists():
        st.success("✅ Vector store loaded")
        st.info("💡 Add new documents? Rebuild to include them.")
    else:
        st.warning("⚠️ Vector store not built yet")

    # Always show the build button
    if st.button("🔨 Build/Rebuild Vector Store", key="build_vector_store"):
        with st.spinner("Building vector store from documents..."):
            try:
                from src.data_loader import load_all_documents
                from src.vectorstore import FaissVectorStore

                docs = load_all_documents("data")
                if len(docs) == 0:
                    st.error("No documents found in the 'data' directory!")
                else:
                    store = FaissVectorStore("faiss_store")
                    store.build_from_documents(docs)
                    st.success(f"✅ Vector store built from {len(docs)} documents!")
                    st.rerun()
            except Exception as e:
                st.error(f"Error building vector store: {str(e)}")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.header("💬 Ask a Question")

    # Check if API key is set
    if not groq_api_key:
        st.warning("⚠️ Please enter your Groq API Key in the sidebar to use the system.")

    # Question input
    query = st.text_input(
        "Your Question",
        placeholder="e.g., What is attention mechanism?",
        help="Enter your question about the documents"
    )

    # Search button
    if st.button("🔍 Search & Answer", type="primary", disabled=not groq_api_key):
        if not query:
            st.warning("Please enter a question!")
        elif not faiss_path.exists():
            st.error("Please build the vector store first using the sidebar!")
        else:
            with st.spinner("Searching and generating answer..."):
                try:
                    from src.search import RAGSearch

                    # Initialize RAG search
                    rag_search = RAGSearch(
                        persist_dir="faiss_store",
                        llm_model=llm_model
                    )

                    # Get summary
                    summary = rag_search.search_and_summarize(query, top_k=top_k)

                    # Display answer
                    st.success("✅ Answer generated!")
                    st.markdown("### 📝 Answer:")
                    st.markdown(summary)

                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.exception(e)

with col2:
    st.header("📚 Sample Questions")
    st.markdown("""
    Try these sample questions:

    - What is attention mechanism?
    - How does self-attention work?
    - What are the applications of attention?
    - What are the benefits of attention mechanisms?
    """)

    st.header("📁 Document Upload")
    uploaded_file = st.file_uploader(
        "Upload a document",
        type=["txt", "pdf", "csv", "docx", "xlsx", "json"],
        help="Upload a document to add to the knowledge base"
    )

    if uploaded_file is not None:
        # Save uploaded file
        save_path = Path("data") / uploaded_file.name
        save_path.parent.mkdir(exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ File uploaded: {uploaded_file.name}")
        st.info("💡 Rebuild the vector store to include this document!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with Streamlit, LangChain, and FAISS | Powered by Groq</p>
</div>
""", unsafe_allow_html=True)
