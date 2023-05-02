import smtplib
import os


class NotificationManager:
    def __init__(self):
        self.email_address = os.getenv("EMAIL_ADDRESS")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.to_email_address = os.getenv("TO_EMAIL_ADDRESS")
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = os.getenv("SMTP_PORT")

    def send_email(self, message_str, to_email_address=None):
        with smtplib.SMTP(self.smtp_server, port=int(self.smtp_port)) as connection:
            connection.starttls()
            connection.login(user=self.email_address, password=self.email_password)
            if not to_email_address:
                to_email_address = self.to_email_address
            connection.sendmail(from_addr=self.email_address,
                                to_addrs=to_email_address,
                                msg="Subject:Flight Deal\n\n" + message_str)
