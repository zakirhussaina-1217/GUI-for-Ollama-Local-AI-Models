# 🚀 GUI for Ollama Local AI Models

A modern, user-friendly **Streamlit-based GUI** for interacting with **Ollama Local AI Models**. This project provides a ChatGPT-inspired interface for running Large Language Models (LLMs) completely offline on your own machine.

Whether you're experimenting with AI, writing code, brainstorming ideas, or testing local models, this application makes interacting with Ollama simple and intuitive.

---

## ✨ Features

* 🤖 Run multiple Ollama local AI models
* 💬 ChatGPT-style conversational interface
* 📂 Multi-chat support
* 📝 Persistent chat history
* 🔄 Start new conversations anytime
* 🗑️ Delete previous chats
* 📌 Automatic model detection from Ollama
* ⚡ Real-time streaming AI responses
* 🎨 Clean and responsive Streamlit UI
* 🔒 Completely offline (your data stays on your device)
* 💻 Cross-platform support (Windows, Linux, macOS)

---

## 🖼️ Screenshots

> *(Add screenshots inside the `assets/screenshots/` folder and update the paths below.)*

### Main Interface

![Main UI](assets/screenshots/main-ui.png)

### Chat History

![Chat History](assets/screenshots/chat-history.png)

### Model Selection

![Model Selection](assets/screenshots/model-selection.png)

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Ollama**
* **JSON**
* **HTML/CSS (Streamlit components)**

---

## 📦 Requirements

* Python 3.10+
* Ollama installed
* Streamlit
* Any Ollama model (Llama, Qwen, Mistral, Phi, Gemma, etc.)

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/GUI-for-Ollama-Local-AI-Models.git
cd GUI-for-Ollama-Local-AI-Models
```

### Create a virtual environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

Start Ollama first:

```bash
ollama serve
```

Then launch the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

## 🤖 Supported Models

Works with any Ollama-compatible model, including:

* Llama 3
* Qwen
* Mistral
* Gemma
* Phi
* CodeLlama
* DeepSeek
* And many more...

---

## 📁 Project Structure

```text
GUI-for-Ollama-Local-AI-Models/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── assets/
│   └── screenshots/
│
├── chats/
│
├── utils/
│
└── .streamlit/
```

---

## 🎯 Roadmap

Planned improvements include:

* [ ] PDF Chat (RAG)
* [ ] Image/Vision Model Support
* [ ] Voice Input & Speech Output
* [ ] Drag & Drop File Upload
* [ ] Chat Export (PDF/Markdown)
* [ ] Theme Customization
* [ ] Prompt Library
* [ ] Model Parameter Controls
* [ ] Token Usage Statistics
* [ ] Plugin Support
* [ ] Conversation Search
* [ ] Multi-user Profiles

---

## 🤝 Contributing

Contributions, ideas, bug reports, and feature requests are always welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future development.

---

## 👨‍💻 Author

**Zakir Hussain A**

B.E. Computer Science Engineering (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, and Full-Stack Development.
