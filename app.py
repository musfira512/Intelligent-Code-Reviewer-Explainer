import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Intelligent Code Reviewer", page_icon="🤖", layout="wide")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found in .env")
    st.stop()

client = Groq(api_key=api_key)

st.title("🤖 Intelligent Code Reviewer & Explainer")
st.write("Upload a source code file and let AI review it.")

with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Model", ["llama-3.3-70b-versatile","llama-3.1-8b-instant"])
    temperature = st.slider("Temperature",0.0,1.0,0.3,0.1)
    top_p = st.slider("Top P",0.1,1.0,0.9,0.1)

uploaded = st.file_uploader("Upload Code", type=["py","js","java","cpp","c"])

lang_map={"py":"python","js":"javascript","java":"java","cpp":"cpp","c":"c"}

if uploaded:
    ext=uploaded.name.split(".")[-1].lower()
    language=lang_map.get(ext,"text")
    code=uploaded.read().decode("utf-8")
    st.subheader("Original Code")
    st.code(code, language=language)

    if st.button("Review Code", use_container_width=True):
        prompt=f"""
You are an expert software engineer.

Analyze this {language} code.

Return Markdown with these headings:
# Summary
# Code Explanation
# Bugs Found
# Optimization Suggestions
# Best Practices
# Improved Code

Code:
```{language}
{code}
```
"""
        with st.spinner("Reviewing..."):
            try:
                resp=client.chat.completions.create(
                    model=model,
                    temperature=temperature,
                    top_p=top_p,
                    messages=[
                        {"role":"system","content":"You are an expert code reviewer."},
                        {"role":"user","content":prompt}
                    ]
                )
                result=resp.choices[0].message.content
                st.markdown(result)
                st.download_button("Download Report",result,"code_review.md","text/markdown")
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("Built with Python • Streamlit • Groq API")
