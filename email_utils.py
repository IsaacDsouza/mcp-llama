# email_utils.py

import base64
import os
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
TOKEN_PATH = "token.json"
CREDS_PATH = "credentials.json"

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDS_PATH):
                raise FileNotFoundError("Missing 'credentials.json'.")
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token_file:
            token_file.write(creds.to_json())
    return creds

def send_email(to: str, subject: str, body: str) -> str:
    """Send an email using the Gmail API."""
    try:
        creds = get_credentials()
        service = build("gmail", "v1", credentials=creds)

        msg = MIMEText(body)
        msg["to"] = to
        msg["subject"] = subject

        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        message = {"raw": raw}

        sent_msg = service.users().messages().send(userId="me", body=message).execute()
        return f"✅ Email sent to {to} (ID: {sent_msg['id']})"
    except Exception as e:
        return f"❌ Failed to send email: {e}"
