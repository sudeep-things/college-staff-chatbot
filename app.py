# ============================================================
# S V L COLLEGE
# Premium College AI Assistant - Chat Engine
# ============================================================

import re
import difflib
from typing import Optional, List, Dict


# ============================================================
# COLLEGE
# ============================================================

COLLEGE_NAME = "S V L COLLEGE"


# ============================================================
# COLLEGE KNOWLEDGE BASE
# ============================================================

STAFF_DATA = {
    "Uma Maheshwara Rao": {
        "role": "Founder",
        "subjects": [],
        "keywords": [
            "founder",
            "college founder",
            "started college",
            "founder of college",
        ],
        "information": [
            "Founder of our college.",
            "Guides and inspires students.",
            "Encourages a bright future.",
        ],
    },

    "Durga Prasad": {
        "role": "Faculty",
        "subjects": [],
        "keywords": [
            "degree students",
            "degree",
            "academics",
        ],
        "information": [
            "In-charge of degree students.",
            "Guides students in academics.",
            "A supportive well-wisher.",
        ],
    },

    "Suresh": {
        "role": "Faculty",
        "subjects": [],
        "keywords": [],
        "information": [
            "Experienced faculty member.",
            "Motivates students to learn.",
            "Improves knowledge and confidence.",
        ],
    },

    "Amala": {
        "role": "College Anchor & Faculty",
        "subjects": [
            "Accounts",
        ],
        "keywords": [
            "accounts",
            "accounting",
        ],
        "information": [
            "College anchor.",
            "Teaches Accounts.",
            "Explains concepts clearly.",
        ],
    },

    "Valli": {
        "role": "Programming Faculty",
        "subjects": [
            "Programming Languages",
        ],
        "keywords": [
            "programming",
            "coding",
            "code",
            "computer programming",
        ],
        "information": [
            "Teaches programming languages.",
            "Develops coding skills.",
            "Encourages practical learning.",
        ],
    },

    "Pawan": {
        "role": "Professional Skills Trainer",
        "subjects": [
            "Professional Skills",
        ],
        "keywords": [
            "professional skills",
            "personal skills",
            "leadership",
        ],
        "information": [
            "Professional skills trainer.",
            "Develops personal skills.",
            "Builds confidence and leadership.",
        ],
    },

    "Yoga Sri": {
        "role": "Communication Skills Faculty",
        "subjects": [
            "Communication Skills",
        ],
        "keywords": [
            "communication",
            "speaking",
            "communication skills",
        ],
        "information": [
            "Guides students.",
            "Improves communication skills.",
            "Motivates confident speaking.",
        ],
    },

    "Surya": {
        "role": "Computer Faculty",
        "subjects": [
            "Computer Subjects",
        ],
        "keywords": [
            "computer",
            "computers",
            "technical",
            "computer subjects",
        ],
        "information": [
            "Expert in computer subjects.",
            "Explains technical concepts.",
            "Improves practical knowledge.",
        ],
    },

    "Nagendramma": {
        "role": "English Faculty",
        "subjects": [
            "English",
        ],
        "keywords": [
            "english",
        ],
        "information": [
            "English faculty.",
            "Makes classes interesting.",
            "Improves communication skills.",
        ],
    },

    "Jagadish": {
        "role": "Telugu Faculty",
        "subjects": [
            "Telugu",
        ],
        "keywords": [
            "telugu",
        ],
        "information": [
            "Telugu faculty.",
            "Explains lessons clearly.",
            "Encourages language learning.",
        ],
    },

    "Emmanuel": {
        "role": "Reasoning & Arithmetic Faculty",
        "subjects": [
            "Reasoning",
            "Arithmetic",
        ],
        "keywords": [
            "reasoning",
            "arithmetic",
            "aptitude",
        ],
        "information": [
            "Teaches Reasoning and Arithmetic.",
            "Motivates students.",
            "Inspires future success.",
            "Future police officer.",
        ],
    },

    "Prasanna": {
        "role": "Mathematics Faculty",
        "subjects": [
            "Mathematics",
        ],
        "keywords": [
            "math",
            "maths",
            "mathematics",
        ],
        "information": [
            "Mathematics faculty.",
            "Explains concepts simply.",
            "Supports students in learning.",
        ],
    },
}


# ============================================================
# SUBJECT ALIASES
# ============================================================

SUBJECT_ALIASES = {
    "math": "Mathematics",
    "maths": "Mathematics",
    "mathematics": "Mathematics",

    "english": "English",

    "telugu": "Telugu",

    "account": "Accounts",
    "accounts": "Accounts",
    "accounting": "Accounts",

    "programming": "Programming Languages",
    "programming language": "Programming Languages",
    "programming languages": "Programming Languages",
    "coding": "Programming Languages",
    "code": "Programming Languages",

    "computer": "Computer Subjects",
    "computers": "Computer Subjects",
    "computer subject": "Computer Subjects",
    "computer subjects": "Computer Subjects",
    "technical": "Computer Subjects",

    "reasoning": "Reasoning",
    "arithmetic": "Arithmetic",
    "aptitude": "Reasoning",

    "communication": "Communication Skills",
    "communication skill": "Communication Skills",
    "communication skills": "Communication Skills",
    "speaking": "Communication Skills",

    "professional skill": "Professional Skills",
    "professional skills": "Professional Skills",
    "personal skills": "Professional Skills",
    "leadership": "Professional Skills",
}


# ============================================================
# TEXT PROCESSING
# ============================================================

def normalize(text: str) -> str:
    """
    Convert text into a clean form for understanding questions.
    """

    if not text:
        return ""

    text = text.lower().strip()

    # Common informal spellings.
    replacements = {
        "techer": "teacher",
        "teachr": "teacher",
        "tacher": "teacher",
        "facutly": "faculty",
        "maths": "maths",
        "helo": "hello",
        "hii": "hi",
        "hai": "hi",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def get_staff_names() -> List[str]:
    return list(STAFF_DATA.keys())


def get_staff_count() -> int:
    return len(STAFF_DATA)


# ============================================================
# STAFF FINDING
# ============================================================

def find_staff(text: str) -> Optional[str]:
    """
    Find a staff member using exact matching, partial matching,
    or basic fuzzy matching.
    """

    normalized = normalize(text)

    # Exact/substring match.
    for name in sorted(
        STAFF_DATA.keys(),
        key=len,
        reverse=True
    ):
        if normalize(name) in normalized:
            return name

    # Fuzzy match individual words.
    words = normalized.split()

    for name in STAFF_DATA:

        name_words = normalize(name).split()

        for name_word in name_words:

            matches = difflib.get_close_matches(
                name_word,
                words,
                n=1,
                cutoff=0.78,
            )

            if matches:
                return name

    return None


# ============================================================
# SUBJECT FINDING
# ============================================================

def find_subject(text: str) -> Optional[str]:
    """
    Identify a subject from ordinary language.
    """

    normalized = normalize(text)

    # Longest aliases first.
    aliases = sorted(
        SUBJECT_ALIASES.keys(),
        key=len,
        reverse=True,
    )

    for alias in aliases:

        pattern = rf"\b{re.escape(alias)}\b"

        if re.search(pattern, normalized):
            return SUBJECT_ALIASES[alias]

    return None


def find_staff_by_subject(
    subject: str
) -> List[str]:

    results = []

    for name, data in STAFF_DATA.items():

        if subject in data["subjects"]:
            results.append(name)

    return results


# ============================================================
# INTENT DETECTION
# ============================================================

def is_greeting(text: str) -> bool:

    normalized = normalize(text)

    greetings = {
        "hi",
        "hello",
        "hey",
        "hi there",
        "hello there",
        "good morning",
        "good afternoon",
        "good evening",
        "howdy",
    }

    return normalized in greetings


def is_thanks(text: str) -> bool:

    normalized = normalize(text)

    return any(
        phrase in normalized
        for phrase in [
            "thank you",
            "thanks",
            "thank u",
            "thx",
        ]
    )


def is_help(text: str) -> bool:

    normalized = normalize(text)

    return (
        normalized == "help"
        or "what can you do" in normalized
        or "what can i ask" in normalized
        or "how can you help" in normalized
    )


def is_count_question(text: str) -> bool:

    normalized = normalize(text)

    count_words = [
        "how many",
        "number of",
        "total",
        "count",
    ]

    staff_words = [
        "teacher",
        "teachers",
        "staff",
        "faculty",
        "members",
        "professors",
    ]

    return (
        any(word in normalized for word in count_words)
        and any(word in normalized for word in staff_words)
    )


def is_staff_list_question(text: str) -> bool:

    normalized = normalize(text)

    list_words = [
        "list",
        "show",
        "names",
        "who are",
        "give me all",
        "all teachers",
        "all staff",
        "all faculty",
    ]

    return any(
        phrase in normalized
        for phrase in list_words
    )


def is_founder_question(text: str) -> bool:

    normalized = normalize(text)

    return any(
        phrase in normalized
        for phrase in [
            "founder",
            "who founded",
            "who started the college",
            "who started college",
            "college founder",
        ]
    )


def is_subject_teacher_question(text: str) -> bool:

    normalized = normalize(text)

    return any(
        phrase in normalized
        for phrase in [
            "who teaches",
            "who teach",
            "who handles",
            "who takes",
            "who is teaching",
            "teacher for",
            "faculty for",
            "which teacher",
            "which faculty",
        ]
    )


def is_subject_question(text: str) -> bool:

    normalized = normalize(text)

    return any(
        phrase in normalized
        for phrase in [
            "what does",
            "what do",
            "what subject",
            "what subjects",
            "teach",
            "teaches",
        ]
    )


def is_role_question(text: str) -> bool:

    normalized = normalize(text)

    return any(
        phrase in normalized
        for phrase in [
            "role",
            "position",
            "designation",
            "job",
        ]
    )


def is_subject_list_question(text: str) -> bool:

    normalized = normalize(text)

    return any(
        phrase in normalized
        for phrase in [
            "what subjects",
            "which subjects",
            "subjects are taught",
            "what is taught",
            "what are taught",
        ]
    )


# ============================================================
# RESPONSE FORMATTERS
# ============================================================

def format_staff_profile(name: str) -> str:

    data = STAFF_DATA[name]

    response = f"### {name}\n\n"

    response += (
        f"**Role:** {data['role']}\n\n"
    )

    if data["subjects"]:

        response += (
            "**Subjects:** "
            + ", ".join(data["subjects"])
            + "\n\n"
        )

    response += "**About:**\n\n"

    for item in data["information"]:

        response += f"- {item}\n"

    return response


def format_staff_list() -> str:

    response = "### S V L COLLEGE Staff\n\n"

    for index, (name, data) in enumerate(
        STAFF_DATA.items(),
        start=1,
    ):

        response += (
            f"{index}. **{name}** — "
            f"{data['role']}\n"
        )

    return response


def format_subject_list() -> str:

    subjects = []

    for data in STAFF_DATA.values():

        for subject in data["subjects"]:

            if subject not in subjects:
                subjects.append(subject)

    response = "### Subjects & Areas\n\n"

    for subject in subjects:

        response += f"- **{subject}**\n"

    return response


def format_subject_teacher(
    subject: str
) -> str:

    teachers = find_staff_by_subject(subject)

    if not teachers:

        return (
            f"I couldn't find a faculty member specifically "
            f"listed for **{subject}** in my current "
            f"{COLLEGE_NAME} information."
        )

    if len(teachers) == 1:

        return (
            f"**{teachers[0]}** teaches "
            f"**{subject}** at **{COLLEGE_NAME}**."
        )

    names = ", ".join(
        f"**{name}**"
        for name in teachers
    )

    return (
        f"The faculty listed for **{subject}** are: "
        f"{names}."
    )


def help_response() -> str:

    return (
        "### How can I help?\n\n"
        f"I'm the **{COLLEGE_NAME} Assistant**. "
        "I can answer questions using the college "
        "information available to me.\n\n"
        "**Try asking:**\n\n"
        "- How many teachers are there?\n"
        "- Who are the staff members?\n"
        "- Who teaches maths?\n"
        "- Who teaches coding?\n"
        "- What does Valli teach?\n"
        "- Tell me about Emmanuel.\n"
        "- Who is the founder?\n"
        "- What subjects are taught?\n"
    )


# ============================================================
# FOLLOW-UP CONTEXT
# ============================================================

def get_previous_staff(
    conversation: Optional[List[Dict]]
) -> Optional[str]:

    if not conversation:
        return None

    for message in reversed(conversation):

        if message.get("role") != "user":
            continue

        content = message.get(
            "content",
            "",
        )

        staff = find_staff(content)

        if staff:
            return staff

    return None


# ============================================================
# MAIN RESPONSE ENGINE
# ============================================================

def generate_response(
    user_input: str,
    conversation: Optional[List[Dict]] = None,
) -> str:
    """
    Main chatbot function.

    This function is intentionally local and deterministic:
    it answers from the S V L COLLEGE knowledge base instead
    of inventing information.
    """

    if not user_input or not user_input.strip():

        return (
            "Please type a question and I'll help."
        )

    text = normalize(user_input)

    # --------------------------------------------------------
    # Greeting
    # --------------------------------------------------------

    if is_greeting(text):

        return (
            f"Hello! 👋\n\n"
            f"I'm the **{COLLEGE_NAME} Assistant**. "
            "What would you like to know?"
        )

    # --------------------------------------------------------
    # Thanks
    # --------------------------------------------------------

    if is_thanks(text):

        return (
            "You're welcome! 😊\n\n"
            f"Feel free to ask me anything about "
            f"**{COLLEGE_NAME}**."
        )

    # --------------------------------------------------------
    # Help
    # --------------------------------------------------------

    if is_help(text):

        return help_response()

    # --------------------------------------------------------
    # Staff count
    # --------------------------------------------------------

    if is_count_question(text):

        count = get_staff_count()

        return (
            f"There are **{count} staff members** "
            f"in the current **{COLLEGE_NAME}** staff list."
        )

    # --------------------------------------------------------
    # Staff list
    # --------------------------------------------------------

    if is_staff_list_question(text):

        return format_staff_list()

    # --------------------------------------------------------
    # Subject list
    # --------------------------------------------------------

    if is_subject_list_question(text):

        return format_subject_list()

    # --------------------------------------------------------
    # Founder
    # --------------------------------------------------------

    if is_founder_question(text):

        return format_staff_profile(
            "Uma Maheshwara Rao"
        )

    # --------------------------------------------------------
    # Specific staff member
    # --------------------------------------------------------

    staff = find_staff(text)

    if staff:

        data = STAFF_DATA[staff]

        # Subject/teaching question.
        if is_subject_question(text):

            if data["subjects"]:

                subjects = ", ".join(
                    f"**{subject}**"
                    for subject in data["subjects"]
                )

                return (
                    f"**{staff}** teaches "
                    f"{subjects}."
                )

            return (
                f"The current college information does not "
                f"specify a subject taught by **{staff}**."
            )

        # Role question.
        if is_role_question(text):

            return (
                f"**{staff}** is a "
                f"**{data['role']}** at "
                f"**{COLLEGE_NAME}**."
            )

        # General profile.
        return format_staff_profile(staff)

    # --------------------------------------------------------
    # Subject → Teacher
    # --------------------------------------------------------

    subject = find_subject(text)

    if subject:

        if (
            is_subject_teacher_question(text)
            or "teacher" in text
            or "faculty" in text
            or "teaches" in text
            or "teach" in text
        ):

            return format_subject_teacher(
                subject
            )

    # --------------------------------------------------------
    # Follow-up questions
    # --------------------------------------------------------

    previous_staff = get_previous_staff(
        conversation
    )

    if previous_staff:

        follow_up_words = [
            "he",
            "him",
            "his",
            "she",
            "her",
            "that teacher",
            "this teacher",
            "that faculty",
            "this faculty",
        ]

        if any(
            word in text
            for word in follow_up_words
        ):

            return format_staff_profile(
                previous_staff
            )

    # --------------------------------------------------------
    # General college question
    # --------------------------------------------------------

    if "college" in text:

        return (
            f"I can help with the information currently "
            f"available about **{COLLEGE_NAME}**, especially "
            "staff members, subjects, roles, and faculty "
            "information.\n\n"
            "Try asking:\n"
            "- How many teachers are there?\n"
            "- Who teaches Mathematics?\n"
            "- Who is Valli?\n"
            "- Who is the founder?"
        )

    # --------------------------------------------------------
    # Unknown question
    # --------------------------------------------------------

    return (
        "I don't have enough information to answer that "
        "accurately from my current college knowledge base.\n\n"
        f"I can help with **{COLLEGE_NAME} staff, subjects, "
        "faculty roles, the founder, and other information "
        "contained in my knowledge base**.\n\n"
        "For example, try:\n"
        "- **How many teachers are there?**\n"
        "- **Who teaches maths?**\n"
        "- **Tell me about Valli.**"
    )
