import streamlit as st

from chatbot import get_staff_names, get_staff_info, find_staff


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="College Staff Chatbot",
    page_icon="🎓",
    layout="centered"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🎓 College Staff Chatbot")

st.write(
    "Welcome! Ask me about any college staff member."
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("👥 Available Staff")

    staff_names = get_staff_names()

    for name in staff_names:
        st.write(f"• {name}")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()


# --------------------------------------------------
# Initialize Chat History
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋\n\n"
                "I am the College Staff Chatbot. "
                "You can ask me about any staff member."
            )
        }
    ]


# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# User Input
# --------------------------------------------------

user_input = st.chat_input(
    "Ask about a staff member..."
)


# --------------------------------------------------
# Process User Message
# --------------------------------------------------

if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Find staff member
    staff_name = find_staff(user_input)

    # Generate response
    if staff_name:

        staff_info = get_staff_info(staff_name)

        response = f"### 👤 {staff_name}\n\n"

        for information in staff_info:
            response += f"- {information}\n"

    elif user_input.strip().lower() in [
        "hi",
        "hello",
        "hey",
        "hai"
    ]:

        response = (
            "Hello! 👋\n\n"
            "You can ask me about any staff member."
        )

    elif user_input.strip().lower() in [
        "help",
        "what can you do"
    ]:

        response = (
            "I can provide information about the college staff.\n\n"
            "Try asking something like:\n\n"
            "- Tell me about Valli\n"
            "- Who is Emmanuel?\n"
            "- What does Suresh teach?"
        )

    else:

        response = (
            "❌ I couldn't find that staff member.\n\n"
            "Please enter a staff name from the list "
            "shown in the sidebar."
        )

    # Add chatbot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Refresh page
    st.rerun()