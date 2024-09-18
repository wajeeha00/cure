import smtplib
from email.message import EmailMessage
import imghdr

SENDER = "ammadali1234@gmail.com"
PASSWORD = "dsoafjoasOJH2P3Jlk"
RECEIVER = "ammadali1234@gmail.com"

def send_email(img_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Costumer Showed Up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(img_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    
    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER,RECEIVER, email_message.as_string())
    gmail.quit

if __name__ == "__main__":
    send_email(img_path="images/0.png")
