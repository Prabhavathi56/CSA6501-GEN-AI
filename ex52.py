import streamlit as st
import google.generativeai as genai

# -------------------------------
# Configure Gemini API
# -------------------------------
API_KEY = ""

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

# -------------------------------
# Streamlit Page
# -------------------------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 AI-Based Research Assistance Application")
st.write("Enter a research topic to generate information, keywords, and a concise summary.")

# -------------------------------
# Input
# -------------------------------
topic = st.text_input(
    "Enter Research Topic",
    placeholder="Example: Artificial Intelligence in Healthcare"
)

# -------------------------------
# Generate Button
# -------------------------------
if st.button("🔍 Generate Research Information"):

    if topic.strip() == "":
        st.warning("Please enter a research topic.")

    else:
        with st.spinner("Generating research information..."):

            prompt = f"""
            You are an AI research assistant.

            Research Topic: {topic}

            Provide the following:

            1. Relevant Information:
            Give 5 important points about the research topic.

            2. Keywords:
            Give 8 important keywords related to the topic.

            3. Concise Summary:
            Give a short summary of the topic in 4-5 sentences.

            Format the answer clearly using headings.
            """

            try:
                response = model.generate_content(prompt)

                st.success("Research information generated successfully!")

                st.subheader("📖 Research Information")
                st.write(response.text)

            except Exception as e:
                st.error("Error while generating response.")
                st.write(e)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("AI-Based Research Assistance Application")
