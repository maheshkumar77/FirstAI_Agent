from langchain.tools import tool


@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid mathematical expression."


@tool
def study_planner(subject: str, minutes: int) -> str:
    """Create a simple study plan for a subject based on available minutes."""

    if minutes < 30:
        return f"Study {subject} for {minutes} minutes focusing only on the most important concepts."

    if minutes <= 60:
        return (
            f"Study plan for {subject}:\n"
            f"1. 10 minutes - Review previous concepts\n"
            f"2. 30 minutes - Learn new concepts\n"
            f"3. 10 minutes - Practice questions\n"
            f"4. 10 minutes - Review what you learned"
        )

    return (
        f"Study plan for {subject} ({minutes} minutes):\n"
        f"1. 15 minutes - Review previous concepts\n"
        f"2. {minutes // 2} minutes - Learn new concepts\n"
        f"3. 20 minutes - Practice problems\n"
        f"4. 15 minutes - Review and summarize"
    )


@tool
def save_note(note: str) -> str:
    """
    Save the user's note to notes.txt.

    Use this tool whenever the user asks to save, remember, store,
    or keep a piece of information as a note.

    The entire text that the user wants to save should be passed
    as the 'note' argument.
    """

    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")

    return "Note saved successfully."