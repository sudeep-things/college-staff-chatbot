# ============================================================
# S V L COLLEGE
# Professional College AI Assistant
# ChatGPT-inspired Streamlit UI
# ============================================================

import time
import streamlit as st

from chatbot import (
    COLLEGE_NAME,
    get_staff_names,
    generate_response,
)


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title=f"{COLLEGE_NAME} | AI Assistant",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_title" not in st.session_state:
    st.session_state.chat_title = "New chat"

if "last_response" not in st.session_state:
    st.session_state.last_response = None


# ============================================================
# THEME-AWARE PROFESSIONAL CSS
# ============================================================

st.markdown(
    """
<style>

:root {
    --border: rgba(128, 128, 128, 0.22);
    --muted: rgba(128, 128, 128, 0.72);
    --hover: rgba(128, 128, 128, 0.10);
}

/* ---------- Main application ---------- */

.stApp {
    background: var(--background-color);
}

.block-container {
    max-width: 900px;
    padding-top: 1rem;
    padding-bottom: 8rem;
}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"] {
    background: var(--secondary-background-color);
    border-right: 1px solid var(--border);
}

.sidebar-header {
    padding: 5px 4px 18px 4px;
}

.sidebar-name {
    font-size: 17px;
    font-weight: 700;
    letter-spacing: -0.2px;
}

.sidebar-caption {
    font-size: 12px;
    color: var(--muted);
    margin-top: 3px;
}

.sidebar-section {
    font-size: 12px;
    font-weight: 600;
    color: var(--muted);
    margin: 22px 4px 8px 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Sidebar buttons */

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 42px;
    border: 1px solid transparent;
    border-radius: 9px;
    background: transparent;
    color: var(--text-color);
    text-align: left;
    padding-left: 12px;
    transition: background 0.15s ease;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: var(--hover);
    border-color: var(--border);
}

section[data-testid="stSidebar"] .stTextInput input {
    border-radius: 9px;
}

/* ---------- Top title ---------- */

.topbar {
    text-align: center;
    padding: 8px 0 14px 0;
}

.topbar-title {
    font-size: 15px;
    font-weight: 600;
}

.topbar-subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-top: 2px;
}

/* ---------- Welcome ---------- */

.welcome {
    text-align: center;
    padding-top: 16vh;
    padding-bottom: 30px;
}

.welcome-title {
    font-size: 30px;
    line-height: 1.15;
    font-weight: 650;
    letter-spacing: -0.7px;
}

.welcome-subtitle {
    margin-top: 7px;
    font-size: 15px;
    color: var(--muted);
}

.welcome-question {
    margin-top: 28px;
    font-size: 18px;
    opacity: 0.88;
}

/* ---------- Prompt buttons ---------- */

.prompt-label {
    text-align: center;
    font-size: 12px;
    color: var(--muted);
    margin: 12px 0 9px;
}

.prompt-row .stButton > button {
    min-height: 44px;
    border-radius: 11px;
    font-size: 13px;
    background: transparent;
    border: 1px solid var(--border);
}

.prompt-row .stButton > button:hover {
    background: var(--hover);
}

/* ---------- Chat messages ---------- */

[data-testid="stChatMessage"] {
    border: none;
    padding-top: 10px;
    padding-bottom: 10px;
}

[data-testid="stChatMessageContent"] {
    max-width: 760px;
}

[data-testid="stChatMessageContent"] p {
    line-height: 1.65;
}

/* ---------- Chat input ---------- */

[data-testid="stChatInput"] {
    max-width: 900px;
}

[data-testid="stChatInput"] textarea {
    border-radius: 14px;
}

/* ---------- Staff profile card ---------- */

.profile-card {
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px;
    margin: 5px 0;
}

.profile-name {
    font-weight: 600;
}

.profile-role {
    font-size: 12px;
    color: var(--muted);
}

/* ---------- Footer ---------- */

.footer {
    text-align: center;
    font-size: 11px;
    color: var(--muted);
    padding: 18px 0 5px;
}

/* ---------- Mobile ---------- */

@media (max-width: 700px) {
    .block-container {
        padding-left: 0.8rem;
        padding-right: 0.8rem;
    }

    .welcome {
        padding-top: 11vh;
    }

    .welcome-title {
        font-size: 26px;
    }
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def start_new_chat():
    st.session_state.messages = []
    st.session_state.chat_title = "New chat"
    st.session_state.last_response = None


def submit_question(question: str):
    question = question.strip()

    if not question:
        return

    history = list(st.session_state.messages)

    response = generate_response(
        question,
        conversation=history,
    )

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    if st.session_state.chat_title == "New chat":
        clean_title = question.replace("\n", " ").strip()
        st.session_state.chat_title = (
            clean_title[:35] + "..."
            if len(clean_title) > 35
            else clean_title
        )

    st.session_state.last_response = response


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-header">
            <div class="sidebar-name">S V L COLLEGE</div>
            <div class="sidebar-caption">College AI Assistant</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "＋  New chat",
        use_container_width=True,
        key="new_chat",
    ):
        start_new_chat()
        st.rerun()

    st.markdown(
        '<div class="sidebar-section">Staff</div>',
        unsafe_allow_html=True,
    )

    search = st.text_input(
        "Search staff",
        placeholder="Search staff...",
        label_visibility="collapsed",
    )

    names = get_staff_names()

    if search:
        names = [
            name for name in names
            if search.lower() in name.lower()
        ]

    for name in names:
        if st.button(
            f"👤  {name}",
            key=f"staff_{name}",
            use_container_width=True,
        ):
            submit_question(f"Tell me about {name}")
            st.rerun()

    st.markdown(
        '<div class="sidebar-section">Conversation</div>',
        unsafe_allow_html=True,
    )

    if st.session_state.messages:
        st.caption(st.session_state.chat_title)

    if st.button(
        "🗑  Clear conversation",
        use_container_width=True,
        key="clear_chat",
    ):
        start_new_chat()
        st.rerun()

    st.markdown("---")

    st.caption(
        "Information is based on the college knowledge "
        "provided to this assistant."
    )


# ============================================================
# MAIN HEADER
# ============================================================

if st.session_state.messages:
    st.markdown(
        f"""
        <div class="topbar">
            <div class="topbar-title">{COLLEGE_NAME}</div>
            <div class="topbar-subtitle">College AI Assistant</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# WELCOME SCREEN
# ============================================================

if not st.session_state.messages:

    st.markdown(
        """
        <div class="welcome">
            <div class="welcome-title">S V L COLLEGE</div>
            <div class="welcome-subtitle">College AI Assistant</div>
            <div class="welcome-question">How can I help you today?</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="prompt-label">Try asking</div>',
        unsafe_allow_html=True,
    )

    prompt_col1, prompt_col2 = st.columns(2)

    with prompt_col1:
        if st.button(
            "How many teachers are there?",
            use_container_width=True,
            key="prompt_count",
        ):
            submit_question("How many teachers are there?")
            st.rerun()

    with prompt_col2:
        if st.button(
            "Who teaches Mathematics?",
            use_container_width=True,
            key="prompt_math",
        ):
            submit_question("Who teaches Mathematics?")
            st.rerun()

    prompt_col3, prompt_col4 = st.columns(2)

    with prompt_col3:
        if st.button(
            "Who is the founder?",
            use_container_width=True,
            key="prompt_founder",
        ):
            submit_question("Who is the founder?")
            st.rerun()

    with prompt_col4:
        if st.button(
            "Who teaches programming?",
            use_container_width=True,
            key="prompt_programming",
        ):
            submit_question("Who teaches programming?")
            st.rerun()


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])

    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Message S V L College Assistant..."
)

if user_input:
    submit_question(user_input)
    st.rerun()


# ============================================================
# FOOTER
# ============================================================

if st.session_state.messages:
    st.markdown(
        """
        <div class="footer">
            S V L COLLEGE · College AI Assistant
        </div>
        """,
        unsafe_allow_html=True,
    )
