
from langchain.tools import StructuredTool
from email_utils import send_email  
import re

def send_email_from_input(input_str: str) -> str:
    """
    Parses natural language input and sends email using Gmail API.
    Expects format: "send an email to <recipient> with subject <subject> and body <body>"
    """
    match = re.match(
        r"send an email to (.+?) with subject (.+?) and body (.+)", input_str, re.IGNORECASE
    )
    if not match:
        return ("Invalid input format.\n"
                "Example: send an email to someone@example.com with subject Hello and body How are you?")

    recipient, subject, body = match.groups()
    return send_email(to=recipient, subject=subject, body=body)

# Register tool
send_email_tool = StructuredTool.from_function(
    func=send_email_from_input,
    name="send_email_tool",
    description="Send an email from natural language input. Format: 'send an email to <email> with subject <subject> and body <body>'"
)
