from fastapi import HTTPException
from pydantic import EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint

def send_otp_email(to_email: EmailStr, otp: str):
    sender_email = "no-reply@example.com"
    smtp_username = "0098678e864681"
    smtp_password = "9d15e7806aa59b"
    smtp_host = "sandbox.smtp.mailtrap.io"
    smtp_port = 587

    subject = "Your OTP Code"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    body = f"Your OTP is: {otp}. It will expire in 10 minutes."
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending email: {e}")

def generate_otp():
        return str(randint(1000, 9999))