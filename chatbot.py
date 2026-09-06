# College Staff Chatbot - Data and Logic

STAFF_DATA = {
    "Uma Maheshwara Rao": [
        "Founder of our college.",
        "Guides and inspires students.",
        "Encourages a bright future."
    ],

    "Durga Prasad": [
        "In-charge of degree students.",
        "Guides students in academics.",
        "A supportive well-wisher."
    ],

    "Suresh": [
        "Experienced faculty member.",
        "Motivates students to learn.",
        "Improves knowledge and confidence."
    ],

    "Amala": [
        "College anchor.",
        "Teaches Accounts.",
        "Explains concepts clearly."
    ],

    "Valli": [
        "Teaches programming languages.",
        "Develops coding skills.",
        "Encourages practical learning."
    ],

    "Pawan": [
        "Professional skills trainer.",
        "Develops personal skills.",
        "Builds confidence and leadership."
    ],

    "Yoga Sri": [
        "Guides students.",
        "Improves communication skills.",
        "Motivates confident speaking."
    ],

    "Surya": [
        "Expert in computer subjects.",
        "Explains technical concepts.",
        "Improves practical knowledge."
    ],

    "Nagendramma": [
        "English faculty.",
        "Makes classes interesting.",
        "Improves communication skills."
    ],

    "Jagadish": [
        "Telugu faculty.",
        "Explains lessons clearly.",
        "Encourages language learning."
    ],

    "Emmanuel": [
        "Teaches Reasoning and Arithmetic.",
        "Motivates students.",
        "Inspires future success.",
        "Future police officer."
    ],

    "Prasanna": [
        "Mathematics faculty.",
        "Explains concepts simply.",
        "Supports students in learning."
    ]
}


def get_staff_names():
    """Return the list of staff members."""
    return list(STAFF_DATA.keys())


def get_staff_info(name):
    """Return information about a staff member."""
    return STAFF_DATA.get(name, [])


def find_staff(user_input):
    """
    Find a staff member from the user's message.
    Works with both exact names and questions containing names.
    """

    text = user_input.strip().lower()

    # Check exact name
    for name in STAFF_DATA:
        if text == name.lower():
            return name

    # Check whether the name appears inside the question
    for name in STAFF_DATA:
        if name.lower() in text:
            return name

    return None