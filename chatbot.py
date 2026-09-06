# ============================================================
# S V L COLLEGE
# College AI Assistant - Chatbot Logic
# ============================================================

import re


# ============================================================
# COLLEGE INFORMATION
# ============================================================

COLLEGE_NAME = "S V L COLLEGE"


# ============================================================
# STAFF DATABASE
# ============================================================

STAFF_DATA = {
    "Uma Maheshwara Rao": {
        "role": "Founder",
        "subjects": [],
        "keywords": ["founder", "college founder"],
        "information": [
            "Founder of our college.",
            "Guides and inspires students.",
            "Encourages a bright future."
        ]
    },

    "Durga Prasad": {
        "role": "Faculty",
        "subjects": [],
        "keywords": ["degree students"],
        "information": [
            "In-charge of degree students.",
            "Guides students in academics.",
            "A supportive well-wisher."
        ]
    },

    "Suresh": {
        "role": "Faculty",
        "subjects": [],
        "keywords": [],
        "information": [
            "Experienced faculty member.",
            "Motivates students to learn.",
            "Improves knowledge and confidence."
        ]
    },

    "Amala": {
        "role": "Faculty",
        "subjects": ["Accounts"],
        "keywords": ["accounts"],
        "information": [
            "College anchor.",
            "Teaches Accounts.",
            "Explains concepts clearly."
        ]
    },

    "Valli": {
        "role": "Faculty",
        "subjects": ["Programming Languages"],
        "keywords": [
            "programming",
            "coding",
            "computer programming"
        ],
        "information": [
            "Teaches programming languages.",
            "Develops coding skills.",
            "Encourages practical learning."
        ]
    },

    "Pawan": {
        "role": "Professional Skills Trainer",
        "subjects": ["Professional Skills"],
        "keywords": [
            "professional skills",
            "personal skills",
            "leadership"
        ],
        "information": [
            "Professional skills trainer.",
            "Develops personal skills.",
            "Builds confidence and leadership."
        ]
    },

    "Yoga Sri": {
        "role": "Faculty",
        "subjects": ["Communication Skills"],
        "keywords": [
            "communication",
            "speaking"
        ],
        "information": [
            "Guides students.",
            "Improves communication skills.",
            "Motivates confident speaking."
        ]
    },

    "Surya": {
        "role": "Computer Faculty",
        "subjects": ["Computer Subjects"],
        "keywords": [
            "computer",
            "computers",
            "technical"
        ],
        "information": [
            "Expert in computer subjects.",
            "Explains technical concepts.",
            "Improves practical knowledge."
        ]
    },

    "Nagendramma": {
        "role": "English Faculty",
        "subjects": ["English"],
        "keywords": ["english"],
        "information": [
            "English faculty.",
            "Makes classes interesting.",
            "Improves communication skills."
        ]
    },

    "Jagadish": {
        "role": "Telugu Faculty",
        "subjects": ["Telugu"],
        "keywords": ["telugu"],
        "information": [
            "Telugu faculty.",
            "Explains lessons clearly.",
            "Encourages language learning."
        ]
    },

    "Emmanuel": {
        "role": "Faculty",
        "subjects": ["Reasoning", "Arithmetic"],
        "keywords": [
            "reasoning",
            "arithmetic"
        ],
        "information": [
            "Teaches Reasoning and Arithmetic.",
            "Motivates students.",
            "Inspires future success.",
            "Future police officer."
        ]
    },

    "Prasanna": {
        "role": "Mathematics Faculty",
        "subjects": ["Mathematics"],
        "keywords": [
            "math",
            "maths",
            "mathematics"
        ],
        "information": [
            "Mathematics faculty.",
            "Explains concepts simply.",
            "Supports students in learning."
        ]
    }
}


# ============================================================
# BASIC FUNCTIONS
# ============================================================

def get_staff_names():
    """Return all staff names."""
    return list(STAFF_DATA.keys())


def get_staff_count():
    """Return total number of staff members."""
    return len(STAFF_DATA)


def get_staff_info(name):
    """Return information about a staff member."""
    if name not in STAFF_DATA:
        return []

    return STAFF_DATA[name]["information"]


def find_staff(user_input):
    """Find a staff member mentioned in a question."""

    if not user_input:
        return None

    text = user_input.lower().strip()

    # Longest names first
    names = sorted(
        STAFF_DATA.keys(),
        key=len,
        reverse=True
    )

    for name in names:

        if name.lower() in text:
            return name

    return None


# ============================================================
# STAFF PROFILE
# ============================================================

def get_staff_profile(name):

    if name not in STAFF_DATA:
        return None

    return STAFF_DATA[name]


# ============================================================
# SUBJECT SEARCH
# ============================================================

def find_staff_by_subject(user_input):

    if not user_input:
        return []

    text = user_input.lower()

    matches = []

    for name, data in STAFF_DATA.items():

        # Check subject names
        for subject in data["subjects"]:

            if subject.lower() in text:

                matches.append(name)
                break

        # Check alternative keywords
        if name not in matches:

            for keyword in data["keywords"]:

                if keyword.lower() in text:

                    matches.append(name)
                    break

    return matches


# ============================================================
# FORMAT STAFF INFORMATION
# ============================================================

def format_staff_info(name):

    if name not in STAFF_DATA:
        return None

    data = STAFF_DATA[name]

    response = f"### 👤 {name}\n\n"

    response += f"**Role:** {data['role']}\n\n"

    if data["subjects"]:

        response += "**Subjects / Areas:** "

        response += ", ".join(data["subjects"])

        response += "\n\n"

    response += "**About:**\n\n"

    for item in data["information"]:

        response += f"- {item}\n"

    return response


# ============================================================
# LIST STAFF
# ============================================================

def list_all_staff():

    response = "### 👥 Staff at S V L COLLEGE\n\n"

    for index, (name, data) in enumerate(
        STAFF_DATA.items(),
        start=1
    ):

        response += (
            f"{index}. **{name}** — "
            f"{data['role']}\n"
        )

    return response


# ============================================================
# SUBJECT LIST
# ============================================================

def list_subjects():

    subjects = []

    for data in STAFF_DATA.values():

        for subject in data["subjects"]:

            if subject not in subjects:
                subjects.append(subject)

    response = "### 📚 Subjects / Areas\n\n"

    for subject in subjects:

        response += f"- {subject}\n"

    return response


# ============================================================
# COUNT QUESTIONS
# ============================================================

def is_count_question(text):

    patterns = [
        r"\bhow many\b",
        r"\bhow much\b",
        r"\bnumber of\b",
        r"\btotal\b",
        r"\bcount\b"
    ]

    return any(
        re.search(pattern, text)
        for pattern in patterns
    )


# ============================================================
# LIST QUESTIONS
# ============================================================

def is_list_question(text):

    patterns = [
        "list",
        "show",
        "names",
        "who are",
        "give me all",
        "all teachers",
        "all staff",
        "all faculty"
    ]

    return any(
        phrase in text
        for phrase in patterns
    )


# ============================================================
# FOUNDER QUESTIONS
# ============================================================

def is_founder_question(text):

    patterns = [
        "founder",
        "who founded",
        "college founder",
        "who started the college",
        "who is the founder"
    ]

    return any(
        phrase in text
        for phrase in patterns
    )


# ============================================================
# SUBJECT QUESTION
# ============================================================

def is_subject_question(text):

    patterns = [
        "who teaches",
        "who teach",
        "who handles",
        "who takes",
        "who is teaching",
        "teacher for",
        "faculty for",
        "who teaches"
    ]

    return any(
        phrase in text
        for phrase in patterns
    )


# ============================================================
# GREETING
# ============================================================

def is_greeting(text):

    greetings = [
        "hi",
        "hello",
        "hey",
        "hai",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    return text in greetings


# ============================================================
# THANK YOU
# ============================================================

def is_thanks(text):

    phrases = [
        "thank you",
        "thanks",
        "thank u",
        "thx"
    ]

    return any(
        phrase in text
        for phrase in phrases
    )


# ============================================================
# HELP
# ============================================================

def help_response():

    return """
### 💡 How I can help

I'm the **S V L COLLEGE Assistant**.

You can ask me things like:

- **How many teachers are there?**
- **Who are the staff members?**
- **Who teaches Mathematics?**
- **Who teaches English?**
- **Who teaches Accounts?**
- **Who teaches programming?**
- **Who teaches Reasoning?**
- **Who is the founder?**
- **Tell me about Valli.**
- **What does Emmanuel teach?**
- **What subjects are taught?**

Just ask naturally. 😊
"""


# ============================================================
# MAIN CHATBOT ENGINE
# ============================================================

def generate_response(user_input):

    if not user_input:
        return "Please type a question."


    text = user_input.lower().strip()


    # --------------------------------------------------------
    # Greeting
    # --------------------------------------------------------

    if is_greeting(text):

        return (
            "Hello! 👋\n\n"
            "I'm the **S V L COLLEGE Assistant**.\n\n"
            "How can I help you?"
        )


    # --------------------------------------------------------
    # Thanks
    # --------------------------------------------------------

    if is_thanks(text):

        return (
            "You're welcome! 😊\n\n"
            "Feel free to ask me anything about "
            "S V L COLLEGE."
        )


    # --------------------------------------------------------
    # Help
    # --------------------------------------------------------

    if (
        text == "help"
        or "what can you do" in text
        or "how can you help" in text
    ):

        return help_response()


    # --------------------------------------------------------
    # Staff count
    # --------------------------------------------------------

    if is_count_question(text):

        # Teacher / faculty / staff count
        if any(word in text for word in [
            "teacher",
            "teachers",
            "staff",
            "faculty",
            "people",
            "members"
        ]):

            count = get_staff_count()

            return (
                "### 👥 Staff Count\n\n"
                f"There are **{count} staff members** "
                "in the current S V L COLLEGE staff list."
            )


    # --------------------------------------------------------
    # List staff
    # --------------------------------------------------------

    if is_list_question(text):

        if any(word in text for word in [
            "staff",
            "teacher",
            "teachers",
            "faculty",
            "members",
            "people"
        ]):

            return list_all_staff()


    # --------------------------------------------------------
    # List subjects
    # --------------------------------------------------------

    if (
        "subjects" in text
        or "what is taught" in text
        or "what are taught" in text
        or "what do they teach" in text
    ):

        return list_subjects()


    # --------------------------------------------------------
    # Founder
    # --------------------------------------------------------

    if is_founder_question(text):

        return format_staff_info(
            "Uma Maheshwara Rao"
        )


    # --------------------------------------------------------
    # Specific staff member
    # --------------------------------------------------------

    staff_name = find_staff(user_input)

    if staff_name:

        return format_staff_info(staff_name)


    # --------------------------------------------------------
    # Subject question
    # --------------------------------------------------------

    if is_subject_question(text):

        matches = find_staff_by_subject(
            user_input
        )

        if matches:

            response = "### 📚 Faculty\n\n"

            for name in matches:

                data = STAFF_DATA[name]

                subjects = ", ".join(
                    data["subjects"]
                )

                response += (
                    f"**{name}** — "
                    f"{subjects}\n\n"
                )

            return response


    # --------------------------------------------------------
    # Subject keyword without "who teaches"
    # --------------------------------------------------------

    matches = find_staff_by_subject(
        user_input
    )

    if matches:

        response = "### 📚 Related Faculty\n\n"

        for name in matches:

            response += f"- **{name}**\n"

        return response


    # --------------------------------------------------------
    # Default
    # --------------------------------------------------------

    return (
        "I'm not sure about that yet. 🤔\n\n"
        "I can answer questions about the staff, "
        "subjects, roles, and founder of "
        "**S V L COLLEGE**.\n\n"
        "Try asking:\n"
        "- How many teachers are there?\n"
        "- Who teaches Mathematics?\n"
        "- Who is the founder?\n"
        "- Tell me about Valli."
    )
