import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def _get_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

def send_email_smtp(to_email: str, subject: str, body: str) -> None:
    msg = MIMEMultipart()
    msg["From"] = _get_env("EMAIL_FROM")
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(_get_env("SMTP_HOST"), int(_get_env("SMTP_PORT"))) as server:
        server.starttls()
        server.login(
            _get_env("SMTP_USERNAME"),
            _get_env("SMTP_PASSWORD")
        )
        server.send_message(msg)
