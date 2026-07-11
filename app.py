import os
from io import StringIO

import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="🤖 Intelligent Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------------------------
# Load Environment Variables
# -----------------------------------------------------
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -----------------------------------------------------
# Check API Key
# -----------------------------------------------------
if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY not found in .env file.")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# -----------------------------------------------------
# Custom CSS
# -----------------------------------------------------
st.markdown("""
<style>
.main-title{
    font-size:38px;
    font-weight:bold;
    color:#4F8BF9;
}

.section-title{
    font-size:24px;
    font-weight:bold;
    margin-top:20px;
}

.stButton>button{
    width:100%;
    border-radius:10px;
    height:50px;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# Header
# -----------------------------------------------------
st.markdown(
    "<div class='main-title'>🤖 Intelligent Code Reviewer & Explainer</div>",
    unsafe_allow_html=True,
)

st.write(
    "Upload your source code file and let AI explain it, detect bugs, "
    "suggest improvements, and generate an optimized version."
)

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------
st.sidebar.title("⚙️ Settings")

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.1,
)

top_p = st.sidebar.slider(
    "Top P",
    min_value=0.1,
    max_value=1.0,
    value=0.9,
    step=0.1,
)

model_name = st.sidebar.selectbox(
    "Model",
    [
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant"
    ]
)

# -----------------------------------------------------
# File Upload
# -----------------------------------------------------
uploaded_file = st.file_uploader(
    "📂 Upload Source Code",
    type=["py", "java", "js", "cpp", "c"]
)

# -----------------------------------------------------
# Detect Language
# -----------------------------------------------------
def detect_language(filename: str) -> str:
    ext = filename.split(".")[-1].lower()

    mapping = {
        "py": "python",
        "java": "java",
        "js": "javascript",
        "cpp": "cpp",
        "c": "c"
    }

    return mapping.get(ext, "text")


# -----------------------------------------------------
# Read Uploaded File
# -----------------------------------------------------
code = ""
language = "text"

if uploaded_file:

    language = detect_language(uploaded_file.name)

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    code = stringio.read()

    st.success(f"Uploaded: {uploaded_file.name}")

    st.subheader("📄 Original Code")

    st.code(code, language=language)

# -----------------------------------------------------
# Prompt Builder
# -----------------------------------------------------
def build_prompt(language, code):

    return f"""
You are an expert Senior Software Engineer and Code Reviewer.

Analyze the following {language} code.

Your response MUST contain exactly these sections.

# Summary

Provide a short summary.

# Code Explanation

Explain the code in simple language.

# Bugs Found

Mention all bugs.
If there are no bugs write:
"No bugs found."

# Optimization Suggestions

Provide improvements.

# Best Practices

Mention coding best practices.

# Improved Code

Return the complete optimized code inside one Markdown code block.

Code:

```{language}
{code}

# -----------------------------------------------------
# AI Code Review
# -----------------------------------------------------
if review_button:

    if not uploaded_file:
        st.warning("⚠️ Please upload a source code file first.")
        st.stop()

    with st.spinner("🔍 Reviewing your code..."):

        try:

            prompt = build_prompt(language, code)

            response = client.chat.completions.create(
                model=model_name,
                temperature=temperature,
                top_p=top_p,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert software engineer, code reviewer, "
                            "and programming mentor. Always respond using Markdown "
                            "headings and fenced code blocks."
                        ),
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )

            ai_response = response.choices[0].message.content

        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.stop()

    st.success("✅ Code review completed successfully!")

    st.divider()

    st.subheader("🤖 AI Review")

    st.markdown(ai_response)

    st.divider()

    # -------------------------------------------------
    # Download Report
    # -------------------------------------------------
    st.download_button(
        label="📥 Download Review Report",
        data=ai_response,
        file_name="code_review_report.md",
        mime="text/markdown",
    )

    # -------------------------------------------------
    # Metrics
    # -------------------------------------------------
    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Language",
            language.upper()
        )

    with col2:
        st.metric(
            "Characters",
            len(code)
        )

    with col3:
        st.metric(
            "Lines",
            len(code.splitlines())
        )

# -----------------------------------------------------
# Footer
# -----------------------------------------------------
# -----------------------------------------------------
# Footer
# -----------------------------------------------------
st.divider()

st.markdown(
    """
    <center>
        <p style="color:gray;">
            Built with Python, Streamlit, and Groq API
        </p>
    </center>
    """,
    unsafe_allow_html=True,
)
