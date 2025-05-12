from fastapi import HTTPException
from pydantic import EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
from iam_app.core.config import settings


def send_otp_email(to_email: EmailStr, otp: str):
    sender_email = settings.SENDER_EMAIL
    sender_password = settings.SENDER_PASSWORD
    subject = "Your OTP Code"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    body = f"Your OTP is: {otp}. It will expire in 10 minutes."
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending email: {e}")


def generate_otp():
    return str(randint(1000, 9999))
