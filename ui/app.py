import streamlit as st

st.set_page_config(
    page_title="ClauseLens — Contract Intelligence Assistant",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📄 ClauseLens — Contract Intelligence Assistant")
st.caption("Bilingual (English & Arabic) Contract Understanding · Grounded Citations · Human Review")

with st.sidebar:
    st.header("Settings & Navigation")
    api_url = st.text_input("API Base URL", value="http://localhost:8000")
    st.divider()
    st.markdown("""
    **Pipeline Status:**
    - OCR Engine: `EasyOCR (ar+en)`
    - Foundation Model: `IFM API (MBZUAI)`
    - Vector Store: `PostgreSQL + pgvector`
    """)

tab_review, tab_qa, tab_deadlines, tab_eval = st.tabs([
    "🔍 Review Queue",
    "💬 Grounded Q&A",
    "⏰ Deadlines & Alerts",
    "📊 Evaluation Harness",
])

with tab_review:
    st.subheader("Contract Field Review Queue")
    st.info("System is initializing. Upload contracts or run evaluations via the API.")

with tab_qa:
    st.subheader("Grounded Contract Q&A")
    st.info("Ask specific questions about clauses. Citations and page numbers will appear here.")

with tab_deadlines:
    st.subheader("Upcoming Notice & Expiry Deadlines")
    st.info("Track 30/60/90-day renewal windows across all ingested contracts.")

with tab_eval:
    st.subheader("Repeatable Model Evaluation")
    st.info("CUAD and Arabic benchmark metrics with bootstrap confidence intervals.")
