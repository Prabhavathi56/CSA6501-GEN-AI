
import streamlit as st
import PyPDF2
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI-Based Resume Screening Application")
st.write(
    "Upload candidate resumes and enter an engineering job description "
    "to automatically rank candidates."
)


# -----------------------------
# Extract text from PDF
# -----------------------------
def extract_pdf_text(uploaded_file):
    text = ""

    try:
        reader = PyPDF2.PdfReader(uploaded_file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        st.error(f"Error reading {uploaded_file.name}: {e}")

    return text


# -----------------------------
# Clean text
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text


# -----------------------------
# Extract skills
# -----------------------------
def extract_skills(text):

    skills = [
        "python",
        "java",
        "c",
        "c++",
        "sql",
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",
        "data analysis",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "pandas",
        "numpy",
        "opencv",
        "nlp",
        "computer vision",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "mysql",
        "mongodb",
        "flask",
        "django"
    ]

    found = []

    text = text.lower()

    for skill in skills:
        if skill.lower() in text:
            found.append(skill)

    return found


# -----------------------------
# Main Application
# -----------------------------

st.sidebar.header("Job Description")

job_description = st.sidebar.text_area(
    "Enter Engineering Job Description",
    height=300,
    placeholder="""
Example:

We are looking for a Machine Learning Engineer.

Required skills:
Python, Machine Learning, SQL, Pandas,
NumPy, Scikit-learn, TensorFlow and Data Analysis.

Candidates should have experience in developing
machine learning models and data preprocessing.
"""
)


st.sidebar.header("Upload Resumes")

uploaded_resumes = st.sidebar.file_uploader(
    "Upload candidate resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)


# -----------------------------
# Screening
# -----------------------------

if st.button("🔍 Screen Resumes"):

    if not job_description.strip():

        st.warning("Please enter a job description.")

    elif not uploaded_resumes:

        st.warning("Please upload at least one resume.")

    else:

        with st.spinner("Analysing resumes..."):

            resume_texts = []
            resume_names = []

            for resume in uploaded_resumes:

                text = extract_pdf_text(resume)

                if text.strip():

                    resume_texts.append(clean_text(text))
                    resume_names.append(resume.name)

            if len(resume_texts) == 0:

                st.error("No readable text was found in the uploaded resumes.")

            else:

                # Clean job description
                job_text = clean_text(job_description)

                # Combine job description and resumes
                documents = [job_text] + resume_texts

                # TF-IDF vectorization
                vectorizer = TfidfVectorizer(
                    stop_words="english"
                )

                tfidf_matrix = vectorizer.fit_transform(documents)

                # Calculate similarity
                similarity_scores = cosine_similarity(
                    tfidf_matrix[0:1],
                    tfidf_matrix[1:]
                )[0]

                results = []

                # Extract job skills
                job_skills = extract_skills(job_description)

                for i in range(len(resume_names)):

                    resume_skills = extract_skills(
                        resume_texts[i]
                    )

                    matched_skills = list(
                        set(job_skills) &
                        set(resume_skills)
                    )

                    missing_skills = list(
                        set(job_skills) -
                        set(resume_skills)
                    )

                    # TF-IDF score
                    similarity_score = similarity_scores[i] * 100

                    # Skill score
                    if len(job_skills) > 0:

                        skill_score = (
                            len(matched_skills) /
                            len(job_skills)
                        ) * 100

                    else:

                        skill_score = 0

                    # Final score
                    final_score = (
                        0.7 * similarity_score +
                        0.3 * skill_score
                    )

                    results.append({
                        "Candidate": resume_names[i],
                        "Match Score": round(final_score, 2),
                        "Similarity": round(
                            similarity_score, 2
                        ),
                        "Skill Match": round(
                            skill_score, 2
                        ),
                        "Matched Skills": ", ".join(
                            matched_skills
                        ),
                        "Missing Skills": ", ".join(
                            missing_skills
                        )
                    })

                # Convert to DataFrame
                df = pd.DataFrame(results)

                # Sort candidates
                df = df.sort_values(
                    by="Match Score",
                    ascending=False
                )

                df = df.reset_index(drop=True)

                # Ranking
                df.insert(
                    0,
                    "Rank",
                    range(1, len(df) + 1)
                )


                # -----------------------------
                # Display Results
                # -----------------------------

                st.success("Resume screening completed!")

                st.subheader("🏆 Candidate Ranking")

                st.dataframe(
                    df,
                    use_container_width=True
                )


                # -----------------------------
                # Top Candidate
                # -----------------------------

                top_candidate = df.iloc[0]

                st.subheader("🥇 Top Candidate")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Candidate",
                        top_candidate["Candidate"]
                    )

                with col2:
                    st.metric(
                        "Match Score",
                        f"{top_candidate['Match Score']}%"
                    )

                with col3:
                    st.metric(
                        "Skill Match",
                        f"{top_candidate['Skill Match']}%"
                    )


                # -----------------------------
                # Skills
                # -----------------------------

                st.subheader("🛠️ Top Candidate Skills")

                st.write(
                    "**Matched Skills:**",
                    top_candidate["Matched Skills"]
                    if top_candidate["Matched Skills"]
                    else "None"
                )

                st.write(
                    "**Missing Skills:**",
                    top_candidate["Missing Skills"]
                    if top_candidate["Missing Skills"]
                    else "None"
                )


                # -----------------------------
                # Score Chart
                # -----------------------------

                st.subheader("📊 Candidate Match Scores")

                chart_data = df[
                    ["Candidate", "Match Score"]
                ].set_index("Candidate")

                st.bar_chart(chart_data)


                # -----------------------------
                # Download Results
                # -----------------------------

                csv_data = df.to_csv(
                    index=False
                ).encode("utf-8")

                st.download_button(
                    label="⬇️ Download Screening Report",
                    data=csv_data,
                    file_name="resume_screening_results.csv",
                    mime="text/csv"
                )


# -----------------------------
# Information Section
# -----------------------------

st.divider()

st.subheader("ℹ️ How the Application Works")

st.write("""
1. Enter the engineering job description.
2. Upload candidate resumes in PDF format.
3. The application extracts text from each resume.
4. TF-IDF converts the job description and resumes into numerical vectors.
5. Cosine similarity measures how closely each resume matches the job description.
6. Required technical skills are extracted and compared.
7. A final match score is calculated.
8. Candidates are ranked from highest to lowest.
9. The screening report can be downloaded as a CSV file.
""")
