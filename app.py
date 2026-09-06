# ============================================================
# S V L COLLEGE
# College AI Assistant
# ChatGPT-Style Responsive Interface
# ============================================================

import streamlit as st

from chatbot import (
    COLLEGE_NAME,
    get_staff_names,
    generate_response,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="S V L COLLEGE | AI Assistant",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="auto",
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_title" not in st.session_state:
    st.session_state.chat_title = "New chat"


# ============================================================
# CUSTOM CSS
# ============================================================
#
# IMPORTANT:
# This is ONLY styling.
# There is no visible HTML UI inside the application.
#
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       MAIN APPLICATION
       ====================================================== */

    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }


    /* ======================================================
       CONTENT WIDTH
       ====================================================== */

    .block-container {
        max-width: 900px;
        margin: auto;
        padding-top: 1rem;
        padding-bottom: 7rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }


    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.18);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    section[data-testid="stSidebar"] .stButton button {
        width: 100%;
        text-align: left;
        border-radius: 9px;
        border: 1px solid transparent;
        background: transparent;
        min-height: 42px;
        transition: 0.15s ease;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background: rgba(128, 128, 128, 0.12);
        border-color: rgba(128, 128, 128, 0.20);
    }


    /* ======================================================
       SIDEBAR TITLE
       ====================================================== */

    section[data-testid="stSidebar"] h2 {
        font-size: 1.25rem;
        margin-bottom: 0.15rem;
    }


    /* ======================================================
       CHAT HEADER
       ====================================================== */

    .chat-header {
        text-align: center;
        padding-top: 0.5rem;
        padding-bottom: 1rem;
    }


    /* ======================================================
       WELCOME SCREEN
       ====================================================== */

    .welcome-space {
        min-height: 28vh;
    }


    /* ======================================================
       WELCOME TITLE
       ====================================================== */

    .welcome-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 650;
        letter-spacing: -0.8px;
        margin-top: 1rem;
        margin-bottom: 0.25rem;
    }


    .welcome-subtitle {
        text-align: center;
        opacity: 0.62;
        font-size: 1rem;
        margin-bottom: 1.8rem;
    }


    /* ======================================================
       QUICK QUESTIONS
       ====================================================== */

    .quick-title {
        text-align: center;
        opacity: 0.55;
        font-size: 0.82rem;
        margin-bottom: 0.5rem;
    }


    .quick-question button {
        min-height: 48px;
        border-radius: 12px;
        font-size: 0.88rem;
    }


    /* ======================================================
       CHAT MESSAGES
       ====================================================== */

    [data-testid="stChatMessage"] {
        padding-top: 0.65rem;
        padding-bottom: 0.65rem;
    }


    [data-testid="stChatMessageContent"] {
        max-width: 760px;
        overflow-wrap: anywhere;
    }


    [data-testid="stChatMessageContent"] p {
        line-height: 1.65;
    }


    /* ======================================================
       CHAT INPUT
       ====================================================== */

    [data-testid="stChatInput"] {
        max-width: 900px;
        margin-left: auto;
        margin-right: auto;
    }


    [data-testid="stChatInput"] textarea {
        border-radius: 15px !important;
        min-height: 52px !important;
        font-size: 15px !important;
    }


    /* ======================================================
       FOOTER
       ====================================================== */

    .footer-text {
        text-align: center;
        opacity: 0.45;
        font-size: 0.72rem;
        margin-top: 1rem;
    }


    /* ======================================================
       MOBILE
       ====================================================== */

    @media (max-width: 700px) {

        .block-container {
            max-width: 100%;
            padding-left: 0.75rem;
            padding-right: 0.75rem;
            padding-top: 0.5rem;
            padding-bottom: 6rem;
        }


        .welcome-space {
            min-height: 10vh;
        }


        .welcome-title {
            font-size: 1.75rem;
            letter-spacing: -0.5px;
            margin-top: 1.5rem;
        }


        .welcome-subtitle {
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
        }


        /*
           Turn the two-column quick-question layout
           into a single column on phones.
        */

        [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
        }


        [data-testid="column"] {
            min-width: 100% !important;
            flex: 1 1 100% !important;
        }


        .quick-question button {
            width: 100%;
            min-height: 46px;
            margin-bottom: 0.35rem;
        }


        [data-testid="stChatMessage"] {
            padding-left: 0;
            padding-right: 0;
        }


        [data-testid="stChatMessageContent"] {
            max-width: calc(100vw - 80px);
            font-size: 15px;
        }


        [data-testid="stChatInput"] textarea {
            font-size: 15px !important;
        }


        section[data-testid="stSidebar"] {
            width: 82vw;
            max-width: 320px;
        }
    }


    /* ======================================================
       SMALL MOBILE
       ====================================================== */

    @media (max-width: 400px) {

        .welcome-title {
            font-size: 1.55rem;
        }


        .welcome-subtitle {
            font-size: 0.85rem;
        }


        [data-testid="stChatMessageContent"] {
            font-size: 14px;
            max-width: calc(100vw - 70px);
        }


        .quick-question button {
            font-size: 0.82rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def new_chat():
    """Start a completely new conversation."""

    st.session_state.messages = []
    st.session_state.chat_title = "New chat"


def ask_question(question):
    """Send a question to the chatbot."""

    question = question.strip()

    if not question:
        return

    # Save current conversation before generating response.
    history = list(st.session_state.messages)

    # Generate chatbot answer.
    answer = generate_response(
        question,
        conversation=history,
    )

    # Store user message.
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    # Store assistant message.
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    # Automatically create conversation title.
    if st.session_state.chat_title == "New chat":

        title = question.replace(
            "\n",
            " ",
        ).strip()

        if len(title) > 40:
            title = title[:40] + "..."

        st.session_state.chat_title = title


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # College name
    st.header("S V L COLLEGE")

    st.caption("College AI Assistant")


    # New chat
    if st.button(
        "＋  New chat",
        use_container_width=True,
    ):

        new_chat()
        st.rerun()


    st.divider()


    # ========================================================
    # STAFF SEARCH
    # ========================================================

    st.caption("STAFF")

    search = st.text_input(
        "Search staff",
        placeholder="Search staff...",
        label_visibility="collapsed",
    )


    staff_names = get_staff_names()


    # Filter staff.
    if search.strip():

        staff_names = [
            name
            for name in staff_names
            if search.lower() in name.lower()
        ]


    # ========================================================
    # STAFF LIST
    # ========================================================

    for staff_name in staff_names:

        if st.button(
            f"👤  {staff_name}",
            key=f"staff_{staff_name}",
            use_container_width=True,
        ):

            ask_question(
                f"Tell me about {staff_name}"
            )

            st.rerun()


    st.divider()


    # ========================================================
    # CURRENT CHAT
    # ========================================================

    st.caption("CURRENT CHAT")

    if st.session_state.messages:

        st.caption(
            st.session_state.chat_title
        )

    else:

        st.caption(
            "No messages yet"
        )


    # Clear conversation.
    if st.button(
        "🗑️  Clear chat",
        use_container_width=True,
    ):

        new_chat()
        st.rerun()


    st.divider()


    st.caption(
        "S V L COLLEGE AI Assistant"
    )


# ============================================================
# TOP HEADER
# ============================================================

if st.session_state.messages:

    st.markdown(
        f"### {COLLEGE_NAME}"
    )

    st.caption(
        "College AI Assistant"
    )


# ============================================================
# WELCOME SCREEN
# ============================================================

if not st.session_state.messages:

    # Space above welcome area.
    st.markdown(
        '<div class="welcome-space"></div>',
        unsafe_allow_html=True,
    )


    st.markdown(
        '<div class="welcome-title">S V L COLLEGE</div>',
        unsafe_allow_html=True,
    )


    st.markdown(
        '<div class="welcome-subtitle">'
        'College AI Assistant'
        '</div>',
        unsafe_allow_html=True,
    )


    st.markdown(
        '<div class="quick-title">'
        'What can I help you with?'
        '</div>',
        unsafe_allow_html=True,
    )


    # ========================================================
    # QUICK QUESTION 1 + 2
    # ========================================================

    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "How many teachers are there?",
            use_container_width=True,
            key="quick_1",
        ):

            ask_question(
                "How many teachers are there?"
            )

            st.rerun()


    with col2:

        if st.button(
            "Who teaches Mathematics?",
            use_container_width=True,
            key="quick_2",
        ):

            ask_question(
                "Who teaches Mathematics?"
            )

            st.rerun()


    # ========================================================
    # QUICK QUESTION 3 + 4
    # ========================================================

    col3, col4 = st.columns(2)


    with col3:

        if st.button(
            "Who is the founder?",
            use_container_width=True,
            key="quick_3",
        ):

            ask_question(
                "Who is the founder?"
            )

            st.rerun()


    with col4:

        if st.button(
            "Who teaches programming?",
            use_container_width=True,
            key="quick_4",
        ):

            ask_question(
                "Who teaches programming?"
            )

            st.rerun()


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    role = message["role"]
    content = message["content"]


    # --------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------

    if role == "user":

        with st.chat_message(
            "user",
            avatar="👤",
        ):

            st.markdown(content)


    # --------------------------------------------------------
    # ASSISTANT MESSAGE
    # --------------------------------------------------------

    elif role == "assistant":

        with st.chat_message(
            "assistant",
            avatar="🤖",
        ):

            st.markdown(content)


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Message S V L College Assistant..."
)


if user_input:

    ask_question(user_input)

    st.rerun()


# ============================================================
# FOOTER
# ============================================================

if st.session_state.messages:

    st.caption(
        "S V L COLLEGE · AI Assistant"
    )
