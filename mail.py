import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def detect_suicidal_thoughts(text):
    keywords = ["suicide", "self-harm", "end my life", "worthless", "hopeless","suicidal"]
    if any(keyword in text.lower() for keyword in keywords):
        return True
    return False

def send_alert_email(to_email, subject, body, PASSWORD):
    from_email = "kironmoy.agilisium@gmail.com"  # Your email          

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Connect to the email server and send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, PASSWORD)
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_text_and_alert(text, alert_email, PASSWORD):
    if detect_suicidal_thoughts(text):
        send_alert_email(
            to_email=alert_email,
            subject="Mental Health Alert",
            body=f"An employee may be at risk based on the following input:\n\n{text}",
            PASSWORD=PASSWORD
        )