import smtplib
from email.message import EmailMessage

def send_email(attachment_path):
    email = "#######@gmail.com"
    app_password = "#####"

    msg = EmailMessage()
    msg["Subject"] = "Daily Report"
    msg["From"] = email
    msg["To"] = email
    msg.set_content("Attached is your daily report.")

    with open(attachment_path, "rb") as f:
        file_data = f.read()
        file_name = attachment_path.split("/")[-1]

    msg.add_attachment(
        file_data,
        maintype="image",
        subtype="png",
        filename=file_name
    )

    # SMTP SETUP (THIS IS STEP 4)
    smtp = smtplib.SMTP("smtp.gmail.com", 587)   # server + port
    smtp.ehlo()                                  # identify client (safe to include)
    smtp.starttls()                              # secure connection
    smtp.ehlo()                                  # re-identify after TLS

    smtp.login(email, app_password)              # authentication
    smtp.send_message(msg)
    smtp.quit()
