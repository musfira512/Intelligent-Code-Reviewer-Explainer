# 🤖 Intelligent Code Reviewer & Explainer

An AI-powered developer assistant built with **Python**, **Streamlit**, and the **Groq API** that analyzes source code, explains its functionality, identifies potential bugs, suggests improvements, and generates optimized code.

This project was developed as part of the **DecodeLabs Internship Program**.

---

## 📌 Features

- 📂 Upload source code files
  - Python (.py)
  - Java (.java)
  - JavaScript (.js)
  - C++ (.cpp)
  - C (.c)

- 🧠 AI-powered code analysis
- 📝 Plain-English code explanation
- 🐞 Bug detection and reporting
- ⚡ Performance optimization suggestions
- 📚 Coding best practices
- 🔄 AI-generated improved code
- 🎛️ Adjustable AI parameters
  - Temperature
  - Top-p
- 📄 Download AI review report
- 💻 Clean and responsive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- Markdown

---

## 📁 Project Structure

```
AI-Code-Reviewer/
│
├── app.py
├── requirements.txt
├── README.md

```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Code-Reviewer.git
```

### 2. Navigate to the project directory

```bash
cd AI-Code-Reviewer
```

### 3. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Launch the Streamlit application.
2. Upload a supported source code file.
3. Select AI generation parameters (Temperature and Top-p).
4. Click **Review Code**.
5. The AI analyzes the uploaded code and generates:
   - Code Summary
   - Code Explanation
   - Bug Report
   - Optimization Suggestions
   - Best Practices
   - Improved Code
6. Download the generated review report if needed.

---


## 🎯 Supported Languages

- Python
- Java
- JavaScript
- C
- C++

---

## 📌 Future Improvements

- Support additional programming languages
- GitHub repository analysis
- Complexity analysis
- Security vulnerability detection
- Code quality score
- Export reports as PDF
- Multiple AI model support
- Dark/Light mode toggle

---

## 👨‍💻 Author

**Musfira Zainab**

BS Electrical Engineering Student

---

## 📜 License

This project is developed for educational and internship purposes.

---

## 🙏 Acknowledgements

- DecodeLabs Internship Program
- Groq API
- Streamlit
- Meta Llama Models

---

⭐ If you found this project useful, consider giving it a star on GitHub!
