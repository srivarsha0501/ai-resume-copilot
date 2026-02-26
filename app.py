import streamlit as st
import os
from dotenv import load_dotenv

from utils.parser import extract_text
from utils.skills import extract_skills
from utils.chunker import chunk_text
from utils.embeddings import embed_text_list
from utils.vector_store import create_faiss_index, save_index, search_index
from utils.rag import generate_answer, score_resume, tailor_resume
from utils.job_matcher import match_jobs

# -------------------------------
# Page Config
# -------------------------------

load_dotenv()

st.set_page_config(
    page_title="AI Resume Copilot",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Resume Copilot")
st.caption("RAG powered resume analysis, job matching and AI tailoring")
st.divider()

# -------------------------------
# Upload Resume
# -------------------------------

uploaded_file = st.file_uploader("Upload resume", type="pdf")

if uploaded_file:

    # Save uploaded file
    file_path = "data/uploaded_resume.pdf"
    os.makedirs("data", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # -------------------------------
    # Extract Text
    # -------------------------------

    text = extract_text(file_path)

    st.subheader("📄 Extracted Text")
    st.write(text[:1000])

    # -------------------------------
    # Skill Extraction
    # -------------------------------

    skills = extract_skills(text)
    st.subheader("🛠️ Detected Skills")
    st.write(skills)

    # -------------------------------
    # Chunking + Embeddings
    # -------------------------------

    chunks = chunk_text(text)
    st.subheader("📦 Number of Chunks")
    st.write(len(chunks))

    vectors = embed_text_list(chunks)
    st.subheader("📊 Embedding Shape")
    st.write(vectors.shape)

    # -------------------------------
    # FAISS Index
    # -------------------------------

    index = create_faiss_index(vectors)
    save_index(index)

    st.subheader("🧠 FAISS Index Created")
    st.write(index.ntotal)

    # -------------------------------
    # Ask Resume + Score (Columns)
    # -------------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💡 Ask Resume")
        query = st.text_input("Ask anything about your resume")

        if query:
            query_vector = embed_text_list([query])
            results_idx = search_index(index, query_vector, top_k=3)
            retrieved_chunks = [chunks[i] for i in results_idx]

            with st.spinner("Generating answer..."):
                answer = generate_answer(query, retrieved_chunks)

            st.info(answer)

    with col2:
        st.subheader("⭐ Resume Score")

        if st.button("Evaluate Resume", key="score_btn"):
            with st.spinner("Evaluating resume..."):
                score = score_resume(text)

            st.success(score)

    # -------------------------------
    # Job Matching
    # -------------------------------

    st.subheader("🎯 Top Job Matches")
    job_matches = match_jobs(text)
    st.dataframe(job_matches, width="stretch")

    # -------------------------------
    # Tailor Resume Section
    # -------------------------------

    st.subheader("🎯 Tailor Resume To Job")

    job_desc = st.text_area("Paste job description here")

    if st.button("Generate Tailored Resume", key="tailor_btn"):
        if job_desc.strip() == "":
            st.warning("Please paste a job description first.")
        else:
            with st.spinner("Generating tailored resume..."):
                tailored = tailor_resume(text, job_desc)

            st.subheader("📝 Tailored Resume")
            st.write(tailored)