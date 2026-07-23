import streamlit as st
import requests
import json
import os
from datetime import datetime

# -------------------------
# CONFIG
# -------------------------
OLLAMA_URL = "http://localhost:11434"
CHAT_DIR = "chats"

os.makedirs(CHAT_DIR, exist_ok=True)

st.set_page_config(
    page_title="Local AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# OLLAMA FUNCTIONS
# -------------------------
def get_models():
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags")
        data = response.json()

        if "models" in data:
            return [model["name"] for model in data["models"]]

        return []

    except:
        return []

def generate_response(model, messages):
    payload = {
        "model": model,
        "messages": messages,
        "stream": True
    }

    response = requests.post(
        f"{OLLAMA_URL}/api/chat",
        json=payload,
        stream=True
    )

    full_response = ""

    for line in response.iter_lines():
        if line:
            data = json.loads(line)

            if "message" in data:
                chunk = data["message"]["content"]
                full_response += chunk
                yield full_response

# -------------------------
# CHAT FUNCTIONS
# -------------------------
def list_chats():
    files = []

    for file in os.listdir(CHAT_DIR):
        if file.endswith(".json"):
            files.append(file)

    files.sort(reverse=True)
    return files

def save_chat(chat_name, messages):
    path = os.path.join(CHAT_DIR, chat_name)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            messages,
            f,
            ensure_ascii=False,
            indent=4
        )

def load_chat(chat_name):
    path = os.path.join(CHAT_DIR, chat_name)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def create_new_chat():
    timestamp = datetime.now().strftime(
        "%Y-%m-%d_%H-%M-%S"
    )

    filename = f"chat_{timestamp}.json"

    st.session_state.current_chat = filename
    st.session_state.messages = []

    save_chat(filename, [])

# -------------------------
# SESSION STATE
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_chat" not in st.session_state:

    chats = list_chats()

    if chats:
        st.session_state.current_chat = chats[0]
        st.session_state.messages = load_chat(chats[0])

    else:
        create_new_chat()

# -------------------------
# SIDEBAR
# -------------------------
with st.sidebar:

    st.title("💬 Chats")

    if st.button("➕ New Chat"):
        create_new_chat()
        st.rerun()

    st.divider()

    chats = list_chats()

    for chat in chats:

        col1, col2 = st.columns([4,1])

        with col1:
            if st.button(
                chat.replace(".json", ""),
                key=f"load_{chat}"
            ):
                st.session_state.current_chat = chat
                st.session_state.messages = load_chat(chat)
                st.rerun()

        with col2:
            if st.button(
                "🗑️",
                key=f"delete_{chat}"
            ):
                os.remove(
                    os.path.join(CHAT_DIR, chat)
                )
                st.rerun()

    st.divider()

    models = get_models()

    if models:

        selected_model = st.selectbox(
            "Model",
            models
        )

    else:
        st.error("No Ollama models found")
        st.stop()

    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful AI assistant."
    )

# -------------------------
# HEADER
# -------------------------
st.title("🤖 Local AI Assistant")

st.caption(
    f"Current Chat: {st.session_state.current_chat}"
)

# -------------------------
# DISPLAY CHAT
# -------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# USER INPUT
# -------------------------
prompt = st.chat_input("Ask anything...")

if prompt:

    user_message = {
        "role": "user",
        "content": prompt
    }

    st.session_state.messages.append(
        user_message
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    conversation = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    conversation.extend(
        st.session_state.messages
    )

    with st.chat_message("assistant"):

        placeholder = st.empty()

        final_response = ""

        for response in generate_response(
            selected_model,
            conversation
        ):
            final_response = response
            placeholder.markdown(
                final_response
            )

    assistant_message = {
        "role": "assistant",
        "content": final_response
    }

    st.session_state.messages.append(
        assistant_message
    )

    save_chat(
        st.session_state.current_chat,
        st.session_state.messages
    )