# ============================================================
# S V L COLLEGE
# College AI Assistant
# ChatGPT-style Streamlit Interface
# ============================================================

import streamlit as st

from chatbot import (
    COLLEGE_NAME,
    get_staff_names,
    generate_response
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="S V L COLLEGE | AI Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


if "chat_started" not in st.session_state:

    st.session_state.chat_started = False


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

    /* =====================================================
       GLOBAL
       ===================================================== */

    .stApp {
        background: var(--background-color);
    }

    .block-container {
        max-width: 900px;
        padding-top: 1rem;
        padding-bottom: 6rem;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(128,128,128,0.20);
    }

    .sidebar-brand {
        font-size: 20px;
        font-weight: 700;
        padding: 8px 0 2px 0;
    }

    .sidebar-subtitle {
        font-size: 13px;
        opacity: 0.60;
        margin-bottom: 18px;
    }


    /* =====================================================
       WELCOME SCREEN
       ===================================================== */

    .welcome {
        text-align: center;
        padding-top: 18vh;
        padding-bottom: 30px;
    }

    .welcome-logo {
        font-size: 52px;
        margin-bottom: 15px;
    }

    .welcome-title {
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .welcome-subtitle {
        font-size: 16px;
        opacity: 0.60;
    }


    /* =====================================================
       QUICK PROMPTS
       ===================================================== */

    .prompt-title {
        text-align: center;
        font-size: 14px;
        opacity: 0.60;
        margin-top: 20px;
        margin-bottom: 10px;
    }


    /* =====================================================
       CHAT
       ===================================================== */

    [data-testid="stChatMessage"] {
        padding-top: 12px;
        padding-bottom: 12px;
    }

    [data-testid="stChatMessageContent"] {
        max-width: 760px;
    }


    /* =====================================================
       CHAT INPUT
       ===================================================== */

    [data-testid="stChatInput"] {
        max-width: 900px;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {
        text-align: center;
        font-size: 12px;
        opacity: 0.45;
        margin-top: 30px;
        padding: 10px;
    }

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-brand">🎓 S V L COLLEGE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'College AI Assistant'
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # New Chat
    # --------------------------------------------------------

    if st.button(
        "＋  New chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.session_state.chat_started = False

        st.rerun()


    st.divider()


    # --------------------------------------------------------
    # Staff Search
    # --------------------------------------------------------

    st.markdown("### 👥 Staff")

    search = st.text_input(
        "Search",
        placeholder="Search staff...",
        label_visibility="collapsed"
    )


    staff_names = get_staff_names()


    if search:

        filtered_staff = [
            name
            for name in staff_names
            if search.lower() in name.lower()
        ]

    else:

        filtered_staff = staff_names


    for name in filtered_staff:

        if st.button(
            f"👤 {name}",
            key=f"staff_{name}",
            use_container_width=True
        ):

            question = (
                f"Tell me about {name}"
            )

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            response = generate_response(
                question
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

            st.session_state.chat_started = True

            st.rerun()


    st.divider()


    # --------------------------------------------------------
    # Clear Chat
    # --------------------------------------------------------

    if st.button(
        "🗑️ Clear conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.session_state.chat_started = False

        st.rerun()


    # --------------------------------------------------------
    # Sidebar footer
    # --------------------------------------------------------

    st.markdown("---")

    st.caption(
        "S V L COLLEGE\n\n"
        "College Staff Assistant"
    )


# ============================================================
# WELCOME SCREEN
# ============================================================

if not st.session_state.messages:

    st.markdown(
        """
        <div class="welcome">

            <div class="welcome-logo">
                🎓
            </div>

            <div class="welcome-title">
                S V L COLLEGE
            </div>

            <div class="welcome-subtitle">
                College AI Assistant
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # Quick prompts
    # --------------------------------------------------------

    st.markdown(
        '<div class="prompt-title">'
        'Try asking'
        '</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "How many teachers are there?",
            use_container_width=True
        ):

            question = (
                "How many teachers are there?"
            )

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": generate_response(
                        question
                    )
                }
            )

            st.session_state.chat_started = True

            st.rerun()


    with col2:

        if st.button(
            "Who teaches Mathematics?",
            use_container_width=True
        ):

            question = (
                "Who teaches Mathematics?"
            )

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": generate_response(
                        question
                    )
                }
            )

            st.session_state.chat_started = True

            st.rerun()


    col3, col4 = st.columns(2)


    with col3:

        if st.button(
            "Who is the founder?",
            use_container_width=True
        ):

            question = "Who is the founder?"

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": generate_response(
                        question
                    )
                }
            )

            st.session_state.chat_started = True

            st.rerun()


    with col4:

        if st.button(
            "Who teaches programming?",
            use_container_width=True
        ):

            question = (
                "Who teaches programming?"
            )

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": generate_response(
                        question
                    )
                }
            )

            st.session_state.chat_started = True

            st.rerun()


# ============================================================
# CHAT HISTORY
# ============================================================

else:

    for message in st.session_state.messages:

        if message["role"] == "user":

            with st.chat_message(
                "user",
                avatar="🧑"
            ):

                st.markdown(
                    message["content"]
                )

        else:

            with st.chat_message(
                "assistant",
                avatar="🎓"
            ):

                st.markdown(
                    message["content"]
                )


# ============================================================
# CHAT INPUT
# ============================================================

user_input = st.chat_input(
    "Message S V L College Assistant..."
)


if user_input:

    # --------------------------------------------------------
    # Add user message
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    # --------------------------------------------------------
    # Generate response
    # --------------------------------------------------------

    response = generate_response(
        user_input
    )


    # --------------------------------------------------------
    # Add assistant message
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


    st.session_state.chat_started = True

    st.rerun()


# ============================================================
# FOOTER
# ============================================================

if st.session_state.messages:

    st.markdown(
        """
        <div class="footer">
            S V L COLLEGE • AI College Assistant
        </div>
        """,
        unsafe_allow_html=True
    )
