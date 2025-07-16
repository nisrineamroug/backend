import imaplib, email
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def check_inbox():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        status, messages = mail.search(None, "UNSEEN")
        ids = messages[0].split()

        if not ids:
            print(" No new emails.")
            return

        for num in ids[:5]:  # Only process first 5 unread emails
            _, data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])
            print(f" {msg['From']}: {msg['Subject']}")
            mail.store(num, '+FLAGS', '\\Seen')  # Marks the email as read
        
        mail.logout()

    except Exception as e:
        print(" Error:", str(e))
